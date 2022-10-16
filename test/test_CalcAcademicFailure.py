# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcAcademicFailure import CalcAcadFail
import pytest

RatingType = list[int, str, dict[str, int]]


class TestAcadFail:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, DataType, RatingType, RatingType]:
        data_fail: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 90),
                ("химия", 87),
                ("социология", 60)
            ]
        }
        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
             ],
            "Петров Петр Петрович": [
                 ("математика", 78),
                 ("химия", 87),
                 ("социология", 61)
             ]
        }
        failure: RatingType = [
            1,
            'Число задолжностей у студентов:',
            {'Петров Петр Петрович': 1}]
        nofailure: RatingType = [
            0,
            'Все студенты сдали сессию !',
            {}]

        return data_fail, data, failure, nofailure

    def test_init_calc_acadfail(self, input_data: tuple[DataType,
                                                        RatingType]) -> None:
        calc_acadfail = CalcAcadFail(input_data[0])
        assert input_data[0] == calc_acadfail.data

    def test_calc_acadfail(self, input_data: tuple[DataType,
                                                   RatingType]) -> None:
        failures = CalcAcadFail(input_data[0]).calc()
        assert failures[0] == input_data[2][0]
        for student in failures[2].keys():
            fail_lot = failures[2][student]
            assert fail_lot == input_data[2][2][student]

    def test_calc_notacadfail(self, input_data: tuple[DataType,
                                                      RatingType]) -> None:
        nofail = CalcAcadFail(input_data[1]).calc()
        assert nofail == input_data[3]
