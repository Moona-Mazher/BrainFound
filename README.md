# BrainFound

BrainFound is a 3D foundation model for neuroimaging. It extends the DINOv2 self-supervised learning framework from 2D images to volumetric, multimodal brain MRI. BrainFound learns rich, generalizable representations from unlabeled data, supporting simultaneous disease classification and anatomical segmentation.

This unified, multitask approach advances scalable and annotation-efficient brain imaging analysis, with potential impact on clinical diagnosis and personalized care.


![BrainFound Workflow](docs/brainfound_workflow.png)



# Repository Structure
brainfound/
└── preprocessing/
    ├── dicom_to_nifti.py       # Dataset-agnostic DICOM → NIfTI conversion
    └── transforms.py           # MRI preprocessing pipeline (resampling, normalization, etc.)

# Requirements & Setup
1️⃣ Clone the repository
git clone https://github.com/Moona-Mazher/BrainFound.git
cd BrainFound

2️⃣ Create a Python environment (recommended)

Using conda:

conda create -n brainfound python=3.11
conda activate brainfound


Or using virtualenv:

python -m venv brainfound_env
brainfound_env\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt


Key packages included: torch, torchvision, albumentations, SimpleITK, pandas, numpy, mripreprocessor, scikit-learn, matplotlib.

4️⃣ Verify installation
python -c "import torch, albumentations, SimpleITK, pandas, numpy; print('Packages loaded!')"

# Citation

If you use BrainFound in your work, please cite:

@article{mazher2025towards,
  title={Towards Generalisable Foundation Models for 3D Brain MRI},
  author={Mazher, Moona and Parker, Geoff JM and Alexander, Daniel C},
  journal={arXiv preprint arXiv:2510.23415},
  year={2025}
}
