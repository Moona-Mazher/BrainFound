# BrainFound
BrainFound is a 3D foundation model for neuroimaging. This model extends the DINOv2 self-supervised learning framework from 2D images to volumetric, multimodal brain MRI. BrainFound learns rich, generalizable representations from unlabeled data, supporting simultaneous disease classification and anatomical segmentation. This unified, multitask approach advances scalable and annotation-efficient brain imaging analysis, with potential impact on clinical diagnosis and personalized care.

The code will be made publicly available soon.
(Code is coming soon!)

brainfound/
└── preprocessing/
    ├── dicom_to_nifti.py       # Your dataset-agnostic DICOM → NIfTI conversion
    └── transforms.py           # MRI preprocessing pipeline (resampling, normalization, etc.)








# Requirements & Setup

1. Clone the repository
```bash
git clone https://github.com/Moona-Mazher/BrainFound.git
cd BrainFound

2. Create a Python environment (recommended)
Using conda:

bash
Copy code
conda create -n brainfound python=3.11
conda activate brainfound
Or using virtualenv:

bash
Copy code
python -m venv brainfound_env
brainfound_env\Scripts\activate   # Windows

3. Install dependencies
bash
Copy code
pip install -r requirements.txt

4. Verify installation
bash
Copy code
python -c "import torch, albumentations, SimpleITK, pandas, numpy; print('Packages loaded!')"
Install dependencies with:

# Key packages: torch, albumentations, SimpleITK, pandas, numpy, mripreprocessor.






## Citation
@article{mazher2025towards,
  title={Towards Generalisable Foundation Models for 3D Brain MRI},
  author={Mazher, Moona and Parker, Geoff JM and Alexander, Daniel C},
  journal={arXiv preprint arXiv:2510.23415},
  year={2025}
}

