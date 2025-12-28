import torch
from models.dinov2_base import DINOv2Base

# Initialize DINOv2 large backbone
model = DINOv2Base()

# Example input: batch of 2 random images
x = torch.randn(2, 3, 224, 224)

# Extract features
features = model(x)
print("Features shape:", features.shape)  # (B, num_patches, embedding_dim)

