from models.database import SamplePathChecker, SampleReader
import unittest
from unittest.mock import MagicMock, Mock, call
import pandas
import numpy
import numpy.typing
import json
import cv2
import os


class SampleReaderTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sample_reader = SampleReader(path="path/to/sample", config_json="sensors.json")
        with open("sensors.json") as file:
            self.sensors = json.load(file)
        self.mock_images = {
            "path/to/sample/images/1.jpg":
            self.create_mock_csa_sample(),
            "path/to/sample/images/2.jpg":
            self.create_mock_csa_sample(),
            "path/to/sample/images/3.jpg":
            self.create_mock_csa_sample()}

    def test_get_raw_mos(self):
        pandas.read_csv = MagicMock(
            return_value=self.create_mock_mos_sample())

        df = self.sample_reader.get_raw_mos()
        df.columns = self.sensors["mos_names"]

        pandas.read_csv.assert_called_with(
            self.path + "/serialdata.csv",
            header=0,
            index_col=0,
            names=self.sensors["mos_names"])

    def test_get_raw_mos(self):

        def imread_side_effect(image_file_path: str):
            return self.mock_images[image_file_path]

        mock_image_names = ["1.jpg", "2.jpg", "3.jpg"]
        os.listdir = MagicMock(
            return_value=mock_image_names
        )
        cv2.imread = MagicMock()
        cv2.imread.side_effect = imread_side_effect

        csa_images: list[numpy.typing.NDArray[numpy.uint8]] = self.sample_reader.get_raw_csa()

        for expected, actual in zip(self.mock_images.values(), csa_images):
            numpy.testing.assert_equal(actual, expected)

        os.listdir.assert_called_with("path/to/sample/images")
        cv2.imread.assert_has_calls(
            calls=[
                call("path/to/sample/images/1.jpg"),
                call("path/to/sample/images/2.jpg"),
                call("path/to/sample/images/3.jpg")
            ]

        )

    def create_mock_mos_sample(self) -> pandas.DataFrame:
        columns = ["Channel " + str(i) for i in range(1, 9)]
        df = pandas.DataFrame(data=numpy.random.randint(0, 100, size=(200, 8)),
                              columns=columns)
        return df

    def create_mock_csa_sample(self) -> numpy.typing.NDArray[numpy.uint8]:
        img = numpy.random.randint(low=0,
                                   high=200,
                                   size=(
                                       self.sensors["img_prop"]["width"],
                                       self.sensors["img_prop"]["height"]
                                   ))
        return img
