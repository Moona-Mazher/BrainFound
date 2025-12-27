# brainfound/preprocessing/kfold_split.py

import pandas as pd
import os
from sklearn.model_selection import KFold
from typing import Optional

def create_kfold_splits(csv_path: str,
                        save_dir: str,
                        n_splits: int = 5,
                        shuffle: bool = True,
                        random_state: Optional[int] = 42,
                        prefix: str = 'fold') -> None:
    """
    Split a dataset CSV into K-Folds and save train/validation CSVs.

    Args:
        csv_path (str): Path to input dataset CSV.
        save_dir (str): Directory to save train/val fold CSVs.
        n_splits (int): Number of folds (default 5).
        shuffle (bool): Whether to shuffle the data before splitting.
        random_state (int, optional): Random seed for reproducibility.
        prefix (str): Prefix for saved files (default 'fold').
    """
    os.makedirs(save_dir, exist_ok=True)
    df = pd.read_csv(csv_path)
    kf = KFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)

    for i, (train_idx, val_idx) in enumerate(kf.split(df)):
        train_df = df.iloc[train_idx]
        val_df = df.iloc[val_idx]

        train_file = os.path.join(save_dir, f'{prefix}_train_fold{i}.csv')
        val_file = os.path.join(save_dir, f'{prefix}_val_fold{i}.csv')

        train_df.to_csv(train_file, index=False)
        val_df.to_csv(val_file, index=False)

        print(f"Fold {i}: Train {len(train_df)} samples, Validation {len(val_df)} samples")
