# concepts/data_processor.py

import pandas as pd

class DataProcessor:
    """
    A class to process and clean data from a given pandas DataFrame.

    Attributes:
    -----------
    data : pd.DataFrame
        The DataFrame containing raw data to be processed.
    
    Methods:
    --------
    remove_duplicates() -> pd.DataFrame:
        Removes duplicate rows from the DataFrame.
        
    fill_missing_values(strategy: str = 'mean') -> pd.DataFrame:
        Fills missing values in the DataFrame using the specified strategy.
    
    normalize_data() -> pd.DataFrame:
        Normalizes numeric columns in the DataFrame to a [0, 1] range.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the DataProcessor with the input DataFrame.
        
        Parameters:
        -----------
        data : pd.DataFrame
            The DataFrame to process.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        self.data = data

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Removes duplicate rows from the DataFrame.

        Returns:
        --------
        pd.DataFrame
            A DataFrame with duplicate rows removed.
        """
        self.data = self.data.drop_duplicates().reset_index(drop=True)
        return self.data

    def fill_missing_values(self, strategy: str = 'mean') -> pd.DataFrame:
        """
        Fills missing values in the DataFrame using the specified strategy.

        Parameters:
        -----------
        strategy : str
            The strategy to use for filling missing values. Options are 'mean', 'median', or 'mode'.

        Returns:
        --------
        pd.DataFrame
            A DataFrame with missing values filled.
        
        Raises:
        -------
        ValueError: If an invalid strategy is provided.
        """
        strategies = ['mean', 'median', 'mode']
        if strategy not in strategies:
            raise ValueError(f"Invalid strategy. Choose from {strategies}.")
        
        for column in self.data.select_dtypes(include=['float64', 'int64']).columns:
            if strategy == 'mean':
                self.data[column].fillna(self.data[column].mean(), inplace=True)
            elif strategy == 'median':
                self.data[column].fillna(self.data[column].median(), inplace=True)
            elif strategy == 'mode':
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
        return self.data

    def normalize_data(self) -> pd.DataFrame:
        """
        Normalizes numeric columns in the DataFrame to a [0, 1] range.

        Returns:
        --------
        pd.DataFrame
            A DataFrame with normalized numeric columns.
        """
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        for column in numeric_cols:
            min_val = self.data[column].min()
            max_val = self.data[column].max()
            if max_val - min_val != 0:  # Prevent division by zero
                self.data[column] = (self.data[column] - min_val) / (max_val - min_val)
        return self.data


# Sample usage
if __name__ == "__main__":
    sample_data = {
        'A': [1, 2, 2, 3, None],
        'B': [4, None, 6, 7, 8],
        'C': [10, 10, 10, 10, 10]
    }
    df = pd.DataFrame(sample_data)
    
    processor = DataProcessor(df)
    print("Original Data:")
    print(processor.data)

    processor.remove_duplicates()
    print("\nAfter Removing Duplicates:")
    print(processor.data)

    processor.fill_missing_values(strategy='mean')
    print("\nAfter Filling Missing Values:")
    print(processor.data)

    processor.normalize_data()
    print("\nAfter Normalizing Data:")
    print(processor.data)