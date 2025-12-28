import torch

class DINOv2Base(torch.nn.Module):
    """
    Minimal DINOv2 placeholder using ViT-L/14 backbone (frozen).
    """
    def __init__(self, model_name="dinov2_vitl14"):
        super().__init__()
        # Load pretrained DINOv2 large ViT backbone
        self.dinov2 = torch.hub.load(
            'facebookresearch/dinov2', model_name, pretrained=True
        )
        # Freeze the backbone
        for param in self.dinov2.parameters():
            param.requires_grad = False

    def forward(self, x):
        """
        Forward pass: extract patch embeddings
        x: torch.Tensor of shape (B, 3, H, W)
        returns: patch embeddings of shape (B, num_patches, embedding_dim)
        """
        with torch.no_grad():
            features = self.dinov2.forward_features(x)
        return features['x_norm_patchtokens']


if __name__ == "__main__":
    # Quick test with random tensor
    model = DINOv2Base()
    dummy_input = torch.randn(1, 3, 224, 224)
    embeddings = model(dummy_input)
    print("DINOv2 ViT-L/14 patch embeddings shape:", embeddings.shape)
