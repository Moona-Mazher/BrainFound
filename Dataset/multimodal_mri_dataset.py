# brainfound/datasets/multimodal_mri_dataset.py

import os
from glob import glob
from typing import List, Optional

import torch
from torch.utils.data import Dataset
import numpy as np
import SimpleITK as sitk
import pandas as pd
import albumentations as A


class BrainFoundDataset(Dataset):
    """
    Slice-level PyTorch Dataset for multimodal MRI data.
    Supports T1, T2, FLAIR (or other modalities), optional transforms,
    and user-defined slice selection.
    """
    def __init__(
        self,
        data_dir: str,
        csv_file,
        modalities: List[str] = ["T1", "T2", "FLAIR"],
        transform: Optional[A.Compose] = None,
        slice_indices: Optional[List[int]] = None
    ):
        self.data_dir = data_dir
        self.modalities = modalities
        self.transform = transform
        self.slice_indices = slice_indices

        # Load CSV
        if isinstance(csv_file, str):
            self.csv = pd.read_csv(csv_file)
        else:
            self.csv = csv_file

        self.slice_info = []

        # Build slice-level index
        for idx, row in self.csv.iterrows():
            subject_id = row['ID']
            label = row['Label']
            subject_path = os.path.join(self.data_dir, subject_id)

            # Find modality files
            modality_paths = {}
            for mod in self.modalities:
                files = glob(os.path.join(subject_path, "skullstripping", f"*{mod}.nii.gz"))
                if len(files) == 0:
                    raise FileNotFoundError(f"No {mod} file found for subject {subject_id}")
                modality_paths[mod] = files[0]

            # Read first modality to get number of slices
            vol = sitk.GetArrayFromImage(sitk.ReadImage(modality_paths[self.modalities[0]]))
            num_slices = vol.shape[1] if vol.ndim == 4 else vol.shape[0]

            # Determine slices to use
            if self.slice_indices is None:
                slices_to_use = [j + 10 for j in range(min(140, num_slices - 10))]
            else:
                slices_to_use = [s for s in self.slice_indices if s < num_slices]

            # Store slice-level info
            for slice_idx in slices_to_use:
                self.slice_info.append({
                    "subject_id": subject_id,
                    "modality_paths": modality_paths,
                    "slice_idx": slice_idx,
                    "label": label
                })

    def __len__(self):
        return len(self.slice_info)

    def __getitem__(self, idx):
        info = self.slice_info[idx]
        slice_idx = info["slice_idx"]
        label = info["label"]
        modality_paths = info["modality_paths"]

        slices = []
        for mod in self.modalities:
            vol = sitk.GetArrayFromImage(sitk.ReadImage(modality_paths[mod]))

            if vol.ndim == 4:
                slice_img = np.squeeze(vol[:, slice_idx, :, :], axis=0)
            elif vol.ndim == 3:
                slice_img = vol[slice_idx, :, :]
            else:
                raise ValueError(f"Unexpected volume shape: {vol.shape}")

            slice_img = slice_img.astype(np.float32)
            slices.append(slice_img)

        image = np.stack(slices, axis=0)

        if self.transform:
            transformed = self.transform(image=np.transpose(image, (1, 2, 0)))
            image = np.transpose(transformed["image"], (2, 0, 1))

        image_tensor = torch.from_numpy(image).float()
        label_tensor = torch.tensor(label).long()

        return image_tensor, label_tensor
