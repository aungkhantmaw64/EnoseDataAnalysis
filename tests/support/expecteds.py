import os
import pandas

EXPECTED_SAMPLE_PATH = "..\\data\\raw_samples\\Acetone"
EXPECTED_SAMPLE_NAME = "Acetone"
EXPECTED_SAMPLE_LIST = ["Acetone",
                        "Ammonia",
                        "Benzene",
                        "Ethanol",
                        "Methanol",
                        "Toluene"]

EXPECTED_IMAGES_PATH = os.path.join(EXPECTED_SAMPLE_PATH, "images")
EXPECTED_CSV_PATH = "..\\data\\raw_samples\\Acetone\\serialdata.csv"
CORRECT_SAMPLE_STRUCTURE = ["images",
                            "serialdata.csv"]

VALID_IMAGE_NAMES = ["1.jpg",
                     "2.jpg",
                     "3.jpg"]

EXPECTECTED_LOAD_RESISTANCES = pandas.Series(data=[2.5,
                                                   0.52,
                                                   56,
                                                   96.2,
                                                   29,
                                                   95,
                                                   16.9,
                                                   95.6],
                                             index=["MQ-2",
                                                    "MQ-3",
                                                    "MQ-5",
                                                    "MQ-6",
                                                    "MQ-8",
                                                    "MQ-9",
                                                    "MQ-135",
                                                    "MQ-138"]).T

EXPECTED_RAW_DATA = pandas.DataFrame(data={'MQ-2': [3.5, 3.5],
                                           'MQ-3': [3.5, 3.5],
                                           'MQ-5': [3.5, 3.5],
                                           'MQ-6': [3.5, 3.5],
                                           'MQ-8': [3.5, 3.5],
                                           'MQ-9': [3.5, 3.5],
                                           'MQ-135': [3.5, 3.5],
                                           'MQ-138': [3.5, 3.5]},
                                     index=[0, 1])

EXPECTED_VOLTAGE_TRANSIENT = pandas.DataFrame(data={"MQ-2": [1.5, 1.5],
                                                    "MQ-3": [1.5, 1.5],
                                                    "MQ-5": [1.5, 1.5],
                                                    "MQ-6": [1.5, 1.5],
                                                    "MQ-8": [1.5, 1.5],
                                                    "MQ-9": [1.5, 1.5],
                                                    "MQ-135": [1.5, 1.5],
                                                    "MQ-138": [1.5, 1.5]},
                                              index=[0, 1])

EXPECTED_CURRENT_TRANSIENT = EXPECTED_RAW_DATA/EXPECTECTED_LOAD_RESISTANCES

EXPECTED_CONDUCTANCE_TRANSIENT = EXPECTED_CURRENT_TRANSIENT/EXPECTED_VOLTAGE_TRANSIENT
