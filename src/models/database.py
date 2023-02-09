import os
from typing import Protocol
import pandas
import json
import numpy
import cv2


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

    def __init__(self, path: str, config_json: str):
        """Default constructor for sample reading

        Args:
            path (str): path to sample folder/directory
            config_json (str): path to json file containing sensors configurations
        """
        self.path = path

        with open(config_json) as file:
            self.sensors = json.load(file)

    def get_raw_mos(self) -> pandas.DataFrame:
        """Get raw metal oxide sensor (MOS) array responses

        Returns:
            pandas.DataFrame: sensor responses
        """
        return pandas.read_csv(self.path + "/serialdata.csv",
                               header=0,
                               index_col=0,
                               names=self.sensors["mos_names"])

    def __remove_file_extension(self, file: str, ext: str) -> str:
        """Remove file extension from the given string (if any)

        Args:
            file (str): file name
            ext (str): extension

        Returns:
            str: file name with extension removed
        """
        return file.replace(ext, "")

    def get_raw_csa(self) -> list[numpy.array]:
        """Get raw colorimetric sensor array responses

        Returns:
            list[numpy.array]: _description_
        """
        image_names = os.listdir(self.path + "/images")
        image_names = [self.__remove_file_extension(
            name, ".jpg"
        ) for name in image_names]
        image_names = sorted(image_names, key=int)
        image_paths = [self.path + "/images/" + name + ".jpg" for name in image_names]
        return [cv2.imread(path) for path in image_paths]
