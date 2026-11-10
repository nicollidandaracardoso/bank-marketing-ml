"""Shared data loading and preprocessing for the Bank Marketing project."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATASET_FILENAME = "bank-additional-full.csv"
TARGET_COLUMN = "y"
DURATION_COLUMN = "duration"
PDAYS_COLUMN = "pdays"
NO_PREVIOUS_CONTACT_SENTINEL = 999
PREVIOUS_CONTACT_FLAG = "was_previously_contacted"


def load_dataset(data_path: str | Path | None = None) -> pd.DataFrame:
    """Load the official semicolon-delimited Bank Marketing CSV.

    If ``data_path`` is omitted, read ``data/bank-additional-full.csv`` from
    the project root (the parent directory of this ``src`` folder).
    """
    if data_path is None:
        data_path = Path(__file__).resolve().parents[1] / "data" / DATASET_FILENAME

    path = Path(data_path)
    if not path.is_file():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Place {DATASET_FILENAME} in the data/ folder."
        )

    return pd.read_csv(path, sep=";")


def prepare_features_target(
    dataframe: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series]:
    """Separate ``X`` and ``y``, remove leakage, and represent ``pdays`` safely.

    ``duration`` is removed because it is only known after the phone call.
    The sentinel 999 in ``pdays`` becomes missing for numeric imputation, while
    a binary feature records whether the client had been contacted previously.
    Text values such as ``unknown`` remain unchanged as categorical values.
    """
    if TARGET_COLUMN not in dataframe.columns:
        raise ValueError(f"Required target column {TARGET_COLUMN!r} is missing.")
    if PDAYS_COLUMN not in dataframe.columns:
        raise ValueError(f"Required column {PDAYS_COLUMN!r} is missing.")

    y = dataframe[TARGET_COLUMN].copy()
    X = dataframe.drop(columns=[TARGET_COLUMN, DURATION_COLUMN], errors="ignore").copy()

    pdays = pd.to_numeric(X[PDAYS_COLUMN], errors="raise")
    X[PREVIOUS_CONTACT_FLAG] = (pdays.notna() & pdays.ne(NO_PREVIOUS_CONTACT_SENTINEL)).astype(
        "int8"
    )
    X[PDAYS_COLUMN] = pdays.mask(pdays.eq(NO_PREVIOUS_CONTACT_SENTINEL), np.nan)

    return X, y


def make_preprocessor(features: pd.DataFrame) -> ColumnTransformer:
    """Build numeric and categorical transformations without fitting them.

    Numeric medians, scales, categorical modes, and one-hot categories are
    learned only when this transformer is fitted on training data.
    """
    numeric_columns = features.select_dtypes(include=np.number).columns.tolist()
    categorical_columns = features.select_dtypes(exclude=np.number).columns.tolist()

    if not numeric_columns and not categorical_columns:
        raise ValueError("No predictor columns were provided to the preprocessor.")

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    transformers = []
    if numeric_columns:
        transformers.append(("numeric", numeric_pipeline, numeric_columns))
    if categorical_columns:
        transformers.append(("categorical", categorical_pipeline, categorical_columns))

    return ColumnTransformer(transformers=transformers, remainder="drop")


def split_data(
    features: pd.DataFrame,
    target: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into stratified train and test sets reproducibly."""
    return train_test_split(
        features,
        target,
        test_size=test_size,
        random_state=random_state,
        stratify=target,
    )
