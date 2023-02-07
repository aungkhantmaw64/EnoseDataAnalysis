from models.sample_checker import SamplePathChecker
from unittest.mock import MagicMock, Mock, call
import os


def test_SamplePathChecker_ChecksIfSampleFolderHasCsvFile():
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
    fake_sample_path = "GasName"
    path_checker = SamplePathChecker()
    assert path_checker.check_csv(fake_sample_path)
    os.listdir.assert_called_with(fake_sample_path)


def test_SamplePathChecker_ChecksIfSampleFolderHasImagesFolder():
    fake_sample_path = "GasName"
    expected_paths = {"GasName": ["images", "serialdata.csv"],
                      "GasName/images": ["1.jpg", "2.jpg"]}

    def side_effect(path: str) -> str:
        return expected_paths[path]
    os.listdir = Mock()
    os.listdir.side_effect = side_effect

    path_checker = SamplePathChecker()
    assert path_checker.check_jpg(fake_sample_path)
    os.listdir.assert_has_calls(
        calls=[call(fake_sample_path),
               call(fake_sample_path + "/images")]
    )


def test_SamplePathChecker_CheckIfSampleFolderIsValid():
    fake_sample_path = "GasName"
    path_checker = SamplePathChecker()
    path_checker.check_csv = MagicMock(return_value=True)
    path_checker.check_jpg = MagicMock(return_value=True)

    assert path_checker.check(fake_sample_path)

    path_checker.check_csv.assert_called_once_with(fake_sample_path)
    path_checker.check_jpg.assert_called_once_with(fake_sample_path)


def test_SamplePathChecker_ReturnsFalseWhenCheckingInvalidSampleFolder():
    fake_sample_path = "GasName"
    path_checker = SamplePathChecker()
    path_checker.check_csv = MagicMock(return_value=False)
    path_checker.check_jpg = MagicMock(return_value=False)

    assert not path_checker.check(fake_sample_path)
