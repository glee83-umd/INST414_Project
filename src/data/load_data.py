import pandas as pd
import os

def load_raw_data(filename: str) -> pd.DataFrame:
    """
    Load raw data from the 'data/raw/' directory.

    Args:
        filename (str): Name of the CSV file to load (example: 'my_data.csv').

    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist in the expected path.
    """

    raw_data_path = os.path.join('data', 'raw', filename)
    
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"File '{raw_data_path}' does not exist. Please check the filename and path.")

    df = pd.read_csv(raw_data_path)
    print(f"Successfully loaded data from {raw_data_path}")
    return df
