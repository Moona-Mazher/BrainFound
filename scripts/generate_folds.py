from brainfound.preprocessing.kfold_split import create_kfold_splits

# Replace these paths with your dataset paths
csv_path = 'path/to/your/dataset.csv'  # CSV file containing labels or metadata
save_dir = 'path/to/save/folds/'      # Folder to store train/validation fold CSVs

# Create 5-fold splits
create_kfold_splits(csv_path, save_dir, n_splits=5, prefix='AD_CN')
