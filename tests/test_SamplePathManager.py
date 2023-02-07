from models.sample_manager import SamplePathManager
from unittest.mock import MagicMock
import os


def test_SampleManager_ChecksIfSampleFolderHasCsvFile():
    """
    The path under test doesn't exist.
    We will mock os module to get fake return values
    GasName
        |_images
        |   |_1.jpg
        |   |_2.jpg
        |   |_etc.
        |_serialdata.csv

    """
    os.listdir = MagicMock(return_value=["images",
                                         "serialdata.csv"])
    path_under_test = "GasName"
    path_manager = SamplePathManager()
    assert path_manager.check_csv(path_under_test)
    os.listdir.assert_called_with(path_under_test)
