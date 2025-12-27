from mripreprocessor.preprocessor import preprocess_dataset  # import main function

input_dir = "<path_to_raw_data>"
output_dir = "<path_to_preprocessed_data>"

# Call MRIPreprocessor with a single line
preprocess_dataset(input_dir, output_dir, sequences=["T1", "T2", "FLAIR"])

print(f"Preprocessing completed. Preprocessed data saved at {output_dir}")
