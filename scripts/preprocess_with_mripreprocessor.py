"""
BrainFound Preprocessing Script
--------------------------------
Preprocess MRI data using MRIPreprocessor.

Features:
- Reads all subjects in a raw MRI directory (DICOM or NIfTI)
- Applies coregistration, cropping, skull-stripping
- Supports multiple MRI sequences (T1, T2, FLAIR)
- Saves outputs in a structure compatible with BrainFoundDataset

Usage:
python scripts/preprocess_mri.py --input <raw_data> --output <preprocessed_data> --sequences T1 T2 FLAIR
"""

import os
import argparse
from mripreprocessor.preprocessor import preprocess_dataset

# ------------------ Argument parser ------------------
parser = argparse.ArgumentParser(description="Preprocess MRI dataset using MRIPreprocessor")
parser.add_argument('--input', type=str, required=True,
                    help='Path to raw MRI data (DICOM/NIfTI)')
parser.add_argument('--output', type=str, required=True,
                    help='Path to save preprocessed data')
parser.add_argument('--sequences', nargs='+', default=["T1", "T2", "FLAIR"],
                    help='MRI sequences to preprocess (default: T1 T2 FLAIR)')
args = parser.parse_args()

input_dir = args.input
output_dir = args.output
sequences = args.sequences

# ------------------ Create output folder ------------------
os.makedirs(output_dir, exist_ok=True)

# ------------------ Process each subject ------------------
subjects = [f for f in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, f))]
if not subjects:
    raise FileNotFoundError(f"No subject folders found in {input_dir}")

print(f"Found {len(subjects)} subjects. Starting preprocessing...")

for subj in subjects:
    subj_input_path = os.path.join(input_dir, subj)
    subj_output_path = os.path.join(output_dir, subj)
    os.makedirs(subj_output_path, exist_ok=True)
    
    print(f"Processing subject: {subj}")
    
    # ------------------ MRIPreprocessor call ------------------
    preprocess_dataset(subj_input_path, subj_output_path, sequences=sequences)

print("All subjects processed successfully!")
print(f"Preprocessed data saved in: {output_dir}")
