from support.expecteds import (EXPECTED_CSV_PATH,
                               EXPECTED_VOLTAGE_TRANSIENT,
                               EXPECTED_CURRENT_TRANSIENT,
                               EXPECTED_CONDUCTANCE_TRANSIENT,
                               EXPECTED_RAW_DATA)
from models.sensor_responses import (MetalOxideSensorResponse,
                                     VoltageTransient,
                                     CurrentTransient,
                                     ConductanceTransient,
                                     Sensor,
                                     DEFAULT_MOS_SENSORS,
                                     DEFAULT_LOAD_RESISTORS_KOHM)
import pytest
from unittest import mock
from pandas.testing import assert_frame_equal

SAMPLE_DURATION = 120


@pytest.fixture
def sensors():
    return [Sensor(name=name,
                   loadResistance=res) for name, res
            in zip(DEFAULT_MOS_SENSORS,
                   DEFAULT_LOAD_RESISTORS_KOHM)]


@pytest.fixture
def metalOxideSensorResponse(sensors):
    return MetalOxideSensorResponse(
        csvPath="..\\data\\raw_samples\\Acetone\\serialdata.csv",
        duration_s=SAMPLE_DURATION,
        sensors=sensors)


def test_SensorClass(sensors):
    for sensor, sensor_name, resistor in zip(sensors,
                                             DEFAULT_MOS_SENSORS,
                                             DEFAULT_LOAD_RESISTORS_KOHM):
        assert sensor.name == sensor_name
        assert sensor.loadResistance == resistor


@mock.patch("pandas.read_csv",
            side_effect=[EXPECTED_RAW_DATA])
def test_VoltageTransient(mock_read_csv, sensors):
    voltage = VoltageTransient()
    csvPath = "..\\data\\raw_samples\\Acetone\\serialdata.csv"
    assert_frame_equal(EXPECTED_VOLTAGE_TRANSIENT,
                       voltage.acquire(csvPath=csvPath,
                                       sensors=sensors))

    mock_read_csv.assert_has_calls(
        [mock.call.read_csv(EXPECTED_CSV_PATH,
                            header=0,
                            index_col=0,
                            names=DEFAULT_MOS_SENSORS)]
    )


@mock.patch("pandas.read_csv",
            side_effect=[EXPECTED_RAW_DATA])
def test_CurrentTransient(mock_read_csv, sensors):
    current = CurrentTransient()
    csvPath = "..\\data\\raw_samples\\Acetone\\serialdata.csv"
    assert_frame_equal(EXPECTED_CURRENT_TRANSIENT,
                       current.acquire(csvPath=csvPath,
                                       sensors=sensors))
    mock_read_csv.assert_has_calls(
        [mock.call.read_csv(EXPECTED_CSV_PATH,
                            header=0,
                            index_col=0,
                            names=DEFAULT_MOS_SENSORS)]
    )


@mock.patch("pandas.read_csv",
            side_effect=[EXPECTED_RAW_DATA,
                         EXPECTED_RAW_DATA])
def test_ConductanceTransient(mock_read_csv, sensors):
    conductance = ConductanceTransient()
    csvPath = "..\\data\\raw_samples\\Acetone\\serialdata.csv"
    assert_frame_equal(EXPECTED_CONDUCTANCE_TRANSIENT,
                       conductance.acquire(csvPath=csvPath,
                                           sensors=sensors))
    mock_read_csv.assert_has_calls(
        [mock.call.read_csv(EXPECTED_CSV_PATH,
                            header=0,
                            index_col=0,
                            names=DEFAULT_MOS_SENSORS) for i in range(2)]
    )


@mock.patch("pandas.read_csv",
            return_value=EXPECTED_RAW_DATA)
def test_GetResponse_VaryingTransients(mock_read_csv,
                                       metalOxideSensorResponse):
    actual = metalOxideSensorResponse.getResponse(transient=VoltageTransient())
    assert_frame_equal(EXPECTED_VOLTAGE_TRANSIENT[:SAMPLE_DURATION], actual)
    actual = metalOxideSensorResponse.getResponse(transient=ConductanceTransient())
    assert_frame_equal(EXPECTED_CONDUCTANCE_TRANSIENT[:SAMPLE_DURATION], actual)
    actual = metalOxideSensorResponse.getResponse(transient=CurrentTransient())
    assert_frame_equal(EXPECTED_CURRENT_TRANSIENT[:SAMPLE_DURATION], actual)
    mock_read_csv.assert_has_calls(
        [mock.call.read_csv(EXPECTED_CSV_PATH,
                            header=0,
                            index_col=0,
                            names=DEFAULT_MOS_SENSORS) for i in range(3)]
    )
