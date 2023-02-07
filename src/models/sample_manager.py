import os


class SamplePathManager:

    def __init__(self) -> None:
        pass

    def __check_path(self, target_item: str, path: str) -> bool:
        items_under_path = os.listdir(path)
        return target_item in items_under_path

    def check_csv(self, path: str) -> bool:
        """Checks if serialdata.csv file exist in the path

        Args:
            path (str): sample folder/path

        Returns:
            bool: true if it exists, false otherwise
        """
        return self.__check_path("serialdata.csv", path)

    def check_jpg(self, path: str) -> bool:
        return (self.__check_path("images", path) and
                self.__check_path("1.jpg", path + "/images"))
