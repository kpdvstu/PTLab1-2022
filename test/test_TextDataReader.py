# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.TextDataReader import TextDataReader
from src.TextDataReader import JsonDataReader

class TestTextDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "Иванов Константин Дмитриевич\n" + \
               "    математика:91\n" + "    химия:100\n" + \
               "Петров Петр Семенович\n" + \
               "    русский язык:87\n" + "    литература:78\n"

        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = TextDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

class TestJsonDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:

        text = "{\n" + \
         "     \"Иванов Иван Иванович\": {\n" + \
         "         \"математика\": 67,\n" + \
         "         \"литература\": 100,\n" + \
         "         \"программирование\": 91\n" + \
         "     },\n" + \
         "     \"Петров Петр Петрович\": {\n" + \
         "         \"математика\": 78,\n" + \
         "         \"химия\": 87,\n" + \
         "         \"социология\": 61\n" + \
         "     },\n" + "}\n"
        data = {
             "Иванов Иван Иванович": [
                 ("математика", 67), ("литература", 100), ("программирование", 91)
             ],
             "Петров Петр Петрович": [
                 ("математика", 78), ("химия", 87), ("социология", 61)
             ]
         }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]


@pytest.fixture()
def noncoorrect_path_to_file() -> tuple[str, DataType]:
    return "../dat/data.json",{"Error": [("no such file of directory", 1)]}


def test_noncorrect_path_to_file(
        noncoorrect_path_to_file: tuple[str, DataType]) -> None:
    path = JsonDataReader().read(noncoorrect_path_to_file[0])
    assert path == noncoorrect_path_to_file[1]







