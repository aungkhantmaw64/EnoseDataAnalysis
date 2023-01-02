
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List
import pandas
# Sensors deployed during experimentation
DEFAULT_MOS_SENSORS = ["MQ-2",
                       "MQ-3",
                       "MQ-5",
                       "MQ-6",
                       "MQ-8",
                       "MQ-9",
                       "MQ-135",
                       "MQ-138"]

# Sensors are configured as simple voltage divider networks
# Resitor values are ordered according to their corresponding sensors
DEFAULT_LOAD_RESISTORS_KOHM = [2.5,
                               0.52,
                               56,
                               96.2,
                               29,
                               95,
                               16.9,
                               95.6]

REFERENCE_VOLTAGE = 5


@dataclass
class Sensor:

    name: str
    loadResistance: float


class Transient(ABC):

    @abstractmethod
    def acquire(self, csvPath: str, sensors: List[Sensor]) -> pandas.DataFrame:
        raise NotImplementedError


class VoltageTransient(Transient):

    def acquire(self, csvPath: str, sensors: List[Sensor]) -> pandas.DataFrame:
        raw_df = pandas.read_csv(csvPath,
                                 header=0,
                                 index_col=0,
                                 names=DEFAULT_MOS_SENSORS)
        return REFERENCE_VOLTAGE - raw_df


class MetalOxideSensorResponse:

    def __init__(self) -> None:
        pass
