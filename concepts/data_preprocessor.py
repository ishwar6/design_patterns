# concepts/data_preprocessing.py

import pandas as pd
import numpy as np

class DataPreprocessor:
    """A class for preprocessing data in a pandas DataFrame."""

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initializes the DataPreprocessor with a pandas DataFrame.

        Args:
            dataframe (pd.DataFrame): The DataFrame to be preprocessed.
        """
        self.dataframe = dataframe

    def handle_missing_values(self, strategy: str = 'mean', columns: list = None) -> pd.DataFrame:
        """
        Handles missing values in the DataFrame based on the specified strategy.

        Args:
            strategy (str): The strategy for handling missing values ('mean', 'median', or 'drop').
            columns (list): The list of columns to apply the strategy. If None, applies to all numeric columns.

        Returns:
            pd.DataFrame: The DataFrame with missing values handled.
        
        Raises:
            ValueError: If an invalid strategy is provided.
        """
        if columns is None:
            columns = self.dataframe.select_dtypes(include=[np.number]).columns.tolist()

        if strategy == 'mean':
            for column in columns:
                self.dataframe[column].fillna(self.dataframe[column].mean(), inplace=True)
        elif strategy == 'median':
            for column in columns:
                self.dataframe[column].fillna(self.dataframe[column].median(), inplace=True)
        elif strategy == 'drop':
            self.dataframe.dropna(subset=columns, inplace=True)
        else:
            raise ValueError("Invalid strategy provided. Choose from 'mean', 'median', or 'drop'.")

        return self.dataframe

    def normalize_columns(self, columns: list) -> pd.DataFrame:
        """
        Normalizes specified columns using Min-Max scaling.

        Args:
            columns (list): The list of columns to normalize.

        Returns:
            pd.DataFrame: The DataFrame with normalized columns.
        """
        for column in columns:
            min_value = self.dataframe[column].min()
            max_value = self.dataframe[column].max()
            self.dataframe[column] = (self.dataframe[column] - min_value) / (max_value - min_value)

        return self.dataframe

# Sample usage
if __name__ == "__main__":
    sample_data = {
        'A': [1, 2, np.nan, 4],
        'B': [np.nan, 2, 3, 4],
        'C': [10, 20, 30, 40],
    }
    
    df = pd.DataFrame(sample_data)
    preprocessor = DataPreprocessor(df)

    print("Original DataFrame:")
    print(preprocessor.dataframe)

    df_handled = preprocessor.handle_missing_values(strategy='mean')
    print("\nDataFrame after handling missing values:")
    print(df_handled)

    df_normalized = preprocessor.normalize_columns(columns=['A', 'B', 'C'])
    print("\nDataFrame after normalization:")
    print(df_normalized)