from CalcRating import CalcRating


class LastQuartileCalc(CalcRating):

    def quartile_calc(self) -> list:
        data = self.calc()
        sorted_rating = dict(sorted(data.items(),
                                    key=lambda item: item[1]))
        quan = len(sorted_rating) // 4
        return list(sorted_rating.items())[:quan]