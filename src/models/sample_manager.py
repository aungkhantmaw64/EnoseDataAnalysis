import os


class SamplePathManager:

    def __init__(self) -> None:
        pass

    def check_csv(self, path: str) -> bool:
        """Checks if serialdata.csv file exist in the path

        Args:
            path (str): sample folder/path

        Returns:
            bool: true if it exists, false otherwise
        """
        items_under_path = os.listdir(path)
        return "serialdata.csv" in items_under_path
