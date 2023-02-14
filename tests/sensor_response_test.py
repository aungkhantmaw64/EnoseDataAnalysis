from models.sensor_response import MetalOxideSensor
import unittest
import json
import numpy
import pandas


class MetalOxideSensorTest(unittest.TestCase):

    def setUp(self):
        with open("sensors.json") as file:
            self.sensors = json.load(file)
        self.raw = self.create_raw_mos_df_mock()
        self.response = MetalOxideSensor(raw_df=self.raw)

    def test_MetalOxideSensor_ShouldTransformRawToVoltage(self):
        pandas.testing.assert_frame_equal(self.create_voltage_mos_df_mock(), self.response.get_voltage())

    def test_MetalOxideSensor_ShouldTransformRawToConductance(self):
        pandas.testing.assert_frame_equal(self.create_conductance_mos_df_mock(), self.response.get_conductance())

    def test_MetalOxideSensor_ShouldTransformRawToCurrent(self):
        pandas.testing.assert_frame_equal(self.create_current_mos_df_mock(), self.response.get_current())

    def create_raw_mos_df_mock(self):
        df = pandas.DataFrame(numpy.array(
            [[1, 2, 3, 4, 5, 4, 3, 2]], dtype="float64"
        ), columns=self.sensors["mos_names"])
        return df

    def create_voltage_mos_df_mock(self):
        df = pandas.DataFrame(numpy.array(
            [[4, 3, 2, 1, 0, 1, 2, 3]], dtype="float64"
        ), columns=self.sensors["mos_names"])
        return df

    def create_current_mos_df_mock(self):
        df = self.create_voltage_mos_df_mock()/self.sensors["load_resistors"]
        return df

    def create_conductance_mos_df_mock(self):
        df = self.create_current_mos_df_mock()/self.create_voltage_mos_df_mock()
        return df
