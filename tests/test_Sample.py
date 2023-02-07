from models.database import Sample, SamplePathChecker
import pandas
from unittest.mock import MagicMock, Mock, call

sensorNames = ["MQ-2",
               "MQ-3",
               "MQ-5",
               "MQ-6",
               "MQ-8",
               "MQ-9",
               "MQ-135",
               "MQ-138"
               ]


def test_SampleReader_ReadsCsvFileFromPathIfValid():
    fake_sample_path = "data/raw_samples/GasName"
    fake_raw_data = pandas.DataFrame(
        data={"Channel 1": [0, 1, 2, 3],
              "Channel 2": [1, 2, 3, 4],
              "Channel 3": [0, 1, 2, 3],
              "Channel 4": [1, 2, 3, 4],
              "Channel 5": [0, 1, 2, 3],
              "Channel 6": [1, 2, 3, 4],
              "Channel 7": [0, 1, 2, 3],
              "Channel 8": [1, 2, 3, 4]
              }
    )
    expected_dataframe = pandas.DataFrame(
        data={"MQ-2": [0, 1, 2, 3],
              "MQ-3": [1, 2, 3, 4],
              "MQ-5": [0, 1, 2, 3],
              "MQ-6": [1, 2, 3, 4],
              "MQ-8": [0, 1, 2, 3],
              "MQ-9": [1, 2, 3, 4],
              "MQ-135": [0, 1, 2, 3],
              "MQ-138": [1, 2, 3, 4]
              }
    )
    pandas.read_csv = MagicMock(return_value=expected_dataframe)
    path_checker = SamplePathChecker()
    path_checker.check = MagicMock(return_value=True)

    gas = Sample(path=fake_sample_path,
                 path_checker=path_checker)

    pandas.testing.assert_frame_equal(expected_dataframe, gas.raw_mos_data())

    path_checker.check.assert_called_with(fake_sample_path)
    pandas.read_csv.assert_called_with(fake_sample_path + "/serialdata.csv",
                                       header=0,
                                       index_col=0,
                                       names=sensorNames)
