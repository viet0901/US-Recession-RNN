import os
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

def load_raw(filename):
    """
    Load a raw dataset
    """
    path = os.path.join(PROJECT_ROOT, "data", "raw", filename)
    return pd.read_csv(path)

def load_processed(filename):
    """
    Load a processed dataset
    """
    path = os.path.join(PROJECT_ROOT, "data", "processed", filename)
    return pd.read_csv(path)
