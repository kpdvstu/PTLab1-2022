# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from JsonReader import JsonReader
from LastQuartCalc import LastQuartileCalc

def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = JsonReader()
    students = reader.read(path)
    #вывод студента
    print("Список студентов: ", students)
    #вывод рейтинга
    rating = CalcRating(students).calc()
    print("Рейтинг:", rating)
    '''sorted_rating = dict(sorted(rating.items(), key=lambda item: item[1]))
    print("Отсортированный рейтинг:",sorted_rating)
    quan = len(sorted_rating)//4
    result = list(sorted_rating.items())[:quan]'''
    result = LastQuartileCalc(students).quartile_calc()
    print("Последняя квартиль:",result)

if __name__ == "__main__":
    main()
