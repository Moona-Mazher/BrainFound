from brainfound.datasets.multimodal_mri_dataset import BrainFoundDataset
from torch.utils.data import DataLoader
import albumentations as A

# Replace these paths with your own dataset paths
data_dir = "<path_to_preprocessed_data>"
csv_train = "<path_to_train_csv>"
csv_val = "<path_to_val_csv>"

# Define transforms
transform_train = A.Compose([
    A.Resize(224, 224),
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5)
])
transform_val = A.Compose([A.Resize(224, 224)])

# User-defined slices
slice_indices = list(range(10, 51))  # slices 10–50

# Create datasets
modalities = ["FLAIR", "T1", "T2"]
train_dataset = BrainFoundDataset(data_dir, csv_train, modalities, transform_train, slice_indices)
val_dataset = BrainFoundDataset(data_dir, csv_val, modalities, transform_val, slice_indices)

# DataLoaders
batch_size = 10
dataloaders = {
    "train": DataLoader(train_dataset, batch_size=batch_size, shuffle=True, pin_memory=True),
    "val": DataLoader(val_dataset, batch_size=batch_size, shuffle=False, pin_memory=True)
}

# Test a batch
images, labels = next(iter(dataloaders["train"]))
print(images.shape, labels.shape)  # (10, 3, 224, 224), (10,)
