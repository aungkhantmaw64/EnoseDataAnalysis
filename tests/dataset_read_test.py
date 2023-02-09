from models.database import SamplePathChecker, SampleReader
import unittest
from unittest.mock import MagicMock, Mock, call
import os
import pandas
import numpy


class SampleReaderTest(unittest.TestCase):

    def setUp(self) -> None:
        self.path = "path/to/fake/sample"
        self.sample_reader = SampleReader(path=self.path)
        self.mos_names = [
            "MQ-2",
            "MQ-3",
            "MQ-5",
            "MQ-6",
            "MQ-8",
            "MQ-9",
            "MQ-135",
            "MQ-138",
        ]

    def test_get_raw_mos(self):
        pandas.read_csv = MagicMock(
            return_value=self.create_mock_mos_sample())

        df = self.sample_reader.get_raw_mos()
        df.columns = self.mos_names

        pandas.read_csv.assert_called_with(
            self.path + "/serialdata.csv",
            header=0,
            index_col=0,
            names=self.mos_names)

    def create_mock_mos_sample(self) -> pandas.DataFrame:
        columns = ["Channel " + str(i) for i in range(1, 9)]
        df = pandas.DataFrame(data=numpy.random.randint(0, 100, size=(200, 8)),
                              columns=columns)
        return df
