# BrainFound
BrainFound is a 3D foundation model for neuroimaging. This model extends the DINOv2 self-supervised learning framework from 2D images to volumetric, multimodal brain MRI. BrainFound learns rich, generalizable representations from unlabeled data, supporting simultaneous disease classification and anatomical segmentation. This unified, multitask approach advances scalable and annotation-efficient brain imaging analysis, with potential impact on clinical diagnosis and personalized care.

The code will be made publicly available soon.
(Code is coming soon!)

brainfound/
└── preprocessing/
    ├── dicom_to_nifti.py       # Your dataset-agnostic DICOM → NIfTI conversion
    └── transforms.py           # MRI preprocessing pipeline (resampling, normalization, etc.)





# Citation
@article{BrainFound2025,
  title={BrainFound: 3D Self-Supervised Foundation Model for Brain MRI},
  author={...},
  journal={arXiv preprint arXiv:2510.23415},
  year={2025}
}

