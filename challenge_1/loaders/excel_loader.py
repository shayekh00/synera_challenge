# Document loader for Excel files

import pandas as pd
from typing import List

class ExcelLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> pd.DataFrame:
        return pd.read_excel(self.file_path)

    def load_sheets(self) -> List[str]:
        return pd.ExcelFile(self.file_path).sheet_names