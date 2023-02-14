import numpy
import pandas
import json


class MetalOxideSensor:

    def __init__(self, raw_df: pandas.DataFrame) -> None:
        self.raw_df = raw_df
        with open("sensors.json") as file:
            self.sensors = json.load(file)

    def get_voltage(self) -> pandas.DataFrame:
        return 5-self.raw_df

    def get_current(self) -> pandas.DataFrame:
        return self.get_voltage()/self.sensors["load_resistors"]

    def get_conductance(self) -> pandas.DataFrame:
        return self.get_current()/self.get_voltage()
