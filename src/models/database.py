import os
from typing import Protocol
import pandas

SENSOR_NAMES = ["MQ-2",
                "MQ-3",
                "MQ-5",
                "MQ-6",
                "MQ-8",
                "MQ-9",
                "MQ-135",
                "MQ-138"
                ]


class PathChecker(Protocol):

    def check(self, path: str) -> bool:
        pass


class SamplePathChecker:

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
        """Checks if an image folder
        with at least one image file named 1.jpg exists in the path

        Args:
            path (str): sample folder/path

        Returns:
            bool: true if it exists, false otherwise.
        """
        return (self.__check_path("images", path) and
                self.__check_path("1.jpg", path + "/images"))

    def check(self, path: str) -> bool:
        """Check if the given path is a valid sample folder.

        Args:
            path (str): the sample folder/path 

        Returns:
            bool: true if the path is valid, false otherwise.
        """
        return (self.check_csv(path) and self.check_jpg(path))


class SampleReader:

    def __init__(self, path: str):
        self.path = path

    def get_raw_mos(self) -> pandas.DataFrame:
        """Get raw metal oxide sensor (MOS) array responses

        Returns:
            pandas.DataFrame: sensor responses
        """
        return pandas.read_csv(self.path + "/serialdata.csv",
                               header=0,
                               index_col=0,
                               names=SENSOR_NAMES)
