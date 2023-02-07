import os


class SamplePathManager:

    def __init__(self) -> None:
        pass

    def check_csv(self, path: str) -> bool:
        items_under_path = os.listdir(path)
        return "serialdata.csv" in items_under_path
