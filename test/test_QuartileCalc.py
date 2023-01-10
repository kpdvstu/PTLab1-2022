# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcRating import CalcRating
from src.LastQuartCalc import LastQuartileCalc
import pytest


RatingsType = dict[str, float]

class TestQuartileRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000
        }
        return data, rating_scores

    @pytest.fixture()
    def input_data_two(self) -> tuple[DataType, list]:
        data: DataType = {
            'Иванов Иван Иванович':
                [
                    ('математика', 67),
                    ('литература', 100),
                    ('программирование', 91)
                ],
            'Петров Петр Петрович':
                [
                    ('математика', 78),
                    ('химия', 87),
                    ('социология', 61)
                ],
            'Александров Сергей Иванович':
                [
                    ('математика', 61),
                    ('литература', 67),
                    ('программирование', 77)
                ],
            'Дмитриев Дмитрий Петрович':
                [
                    ('математика', 75),
                    ('химия', 89),
                    ('социология', 99)
                ],
            'Станисович Стас Стасов':
                [
                    ('математика', 69),
                    ('литература', 87),
                    ('программирование', 90)
                ],
            'Грезнов Стас Стасов':
                [
                    ('математика', 75),
                    ('литература', 77),
                    ('программирование', 91)
                ],
            'Уткин Василий Иванов':
                [
                    ('математика', 64),
                    ('литература', 78),
                    ('программирование', 68)
                ],
            'Петров Иван Петрович':
                [
                    ('математика', 79),
                    ('литература', 56),
                    ('программирование', 90)
                ]
        }

        quartile = [('Александров Сергей Иванович', 68.33333333333333), ('Уткин Василий Иванов', 70.0)]
        return data, quartile

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingsType]) -> None:
        calc_rating = LastQuartileCalc(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:
        rating = LastQuartileCalc(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]

    def test_calc_quartile(self,
                           input_data_two: tuple[DataType, list]) -> None:
        res = LastQuartileCalc(input_data_two[0]).quartile_calc()
        assert res == input_data_two[1]
