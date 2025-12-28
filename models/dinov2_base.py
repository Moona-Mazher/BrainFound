import torch

# Load DINOv2 ViT-S/14 from Facebook Research
# (frozen backbone, no training)
class DINOv2Base(torch.nn.Module):
    def __init__(self, model_name="dinov2_vits14"):
        super().__init__()
        # Load pretrained model
        self.dinov2 = torch.hub.load(
            'facebookresearch/dinov2', model_name, pretrained=True
        )
        # Freeze backbone
        for param in self.dinov2.parameters():
            param.requires_grad = False

    def forward(self, x):
        """
        x: torch.Tensor of shape (B, 3, H, W), e.g., random tensor or image batch
        returns: patch embeddings of shape (B, num_patches, embedding_dim)
        """
        with torch.no_grad():
            features = self.dinov2.forward_features(x)
        return features['x_norm_patchtokens']


# Quick test
if __name__ == "__main__":
    model = DINOv2Base()
    dummy_input = torch.randn(1, 3, 224, 224)
    embeddings = model(dummy_input)
    print("DINOv2 patch embeddings shape:", embeddings.shape)
