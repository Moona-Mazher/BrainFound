# BrainFound
BrainFound is a 3D foundation model for neuroimaging. This model extends the DINOv2 self-supervised learning framework from 2D images to volumetric, multimodal brain MRI. BrainFound learns rich, generalizable representations from unlabeled data, supporting simultaneous disease classification and anatomical segmentation. This unified, multitask approach advances scalable and annotation-efficient brain imaging analysis, with potential impact on clinical diagnosis and personalized care.

The code will be made publicly available soon.
(Code is coming soon!)

brainfound/
└── preprocessing/
    ├── dicom_to_nifti.py       # Your dataset-agnostic DICOM → NIfTI conversion
    └── transforms.py           # MRI preprocessing pipeline (resampling, normalization, etc.)






# Requirements

Install dependencies with:

pip install -r requirements.txt


# Key packages: torch, albumentations, SimpleITK, pandas, numpy, mripreprocessor.






# Citation
@article{mazher2025towards,
  title={Towards Generalisable Foundation Models for 3D Brain MRI},
  author={Mazher, Moona and Parker, Geoff JM and Alexander, Daniel C},
  journal={arXiv preprint arXiv:2510.23415},
  year={2025}
}

