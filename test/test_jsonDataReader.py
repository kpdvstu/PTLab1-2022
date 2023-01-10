# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.TextDataReader import TextDataReader
from src.JsonReader import JsonReader
import json


class TestJsonDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = """
{
    "Иванов Иван Иванович": {
    "математика": 67,
    "литература": 100,
    "программирование": 91
  },
  "Петров Петр Петрович": {
  "математика": 78,
  "химия": 87,
  "социология": 61
  }
  }
"""
        data = {
            'Иванов Иван Иванович': [('математика', 67), ('литература', 100), ('программирование', 91)],
            'Петров Петр Петрович': [('математика', 78), ('химия', 87), ('социология', 61)]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]