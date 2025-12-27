# brainfound/preprocessing/dicom_to_nifti.py

import os
from glob import glob
import dicom2nifti
from typing import Union, List

def create_folder(directory: str) -> None:
    """
    Create a directory if it does not exist.

    Args:
        directory (str): Path to create.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError as e:
        print(f"Error creating directory {directory}: {e}")


def convert_dicom_to_nifti(dicom_input: Union[str, List[str]], output_directory: str) -> None:
    """
    Convert DICOM files or a DICOM directory to NIfTI format.

    Args:
        dicom_input (str or list[str]): Path to a DICOM folder or a single DICOM file.
        output_directory (str): Directory to save the converted NIfTI files.
    """
    create_folder(output_directory)
    
    try:
        if isinstance(dicom_input, list):
            # If a list of files, use the first element (dicom2nifti expects folder/file path)
            dicom_input = dicom_input[0]
        dicom2nifti.convert_directory(dicom_input, output_directory)
        print(f"NIfTI files successfully saved to {output_directory}")
    except Exception as e:
        print(f"Conversion failed for {dicom_input}: {e}")


def convert_dataset(dicom_root: str, output_root: str, modality_folder: str = 't1_mprage') -> None:
    """
    Convert all subjects in a dataset from DICOM to NIfTI.

    Args:
        dicom_root (str): Root directory containing subject folders with DICOM files.
        output_root (str): Root directory to save NIfTI outputs.
        modality_folder (str): Name of modality folder inside each subject (default: 't1_mprage').
    """
    create_folder(output_root)
    subjects = os.listdir(dicom_root)

    for subj in subjects:
        subj_path = os.path.join(dicom_root, subj)
        dicom_path = glob(os.path.join(subj_path, modality_folder, '*', '*'))
        
        if not dicom_path:
            print(f"No DICOM files found for subject {subj}, skipping...")
            continue
        
        save_path = os.path.join(output_root, subj)
        create_folder(save_path)
        
        convert_dicom_to_nifti(dicom_path, save_path)
