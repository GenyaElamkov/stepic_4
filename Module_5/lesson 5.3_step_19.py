from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month

    @property
    def get_calend(self):
        return self.year, self.month

    def __str__(self) -> str:
        return f"{self.year}-{self.month}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self.year, self.month}"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, __class__) or isinstance(__value, tuple):
            return self.get_calend == __value
        return NotImplemented

    def __ge__(self, __value: object) -> bool:
        if isinstance(__value, __class__) or isinstance(__value, tuple):
            return self.get_calend >= __value
        return NotImplemented

months = [Month(2014, 4), Month(2016, 8), Month(2006, 5), Month(2022, 8), Month(2014, 9), Month(2014, 9),
          Month(2002, 12), Month(2003, 8), Month(2016, 5), Month(2022, 5), Month(2019, 12), Month(2011, 2),
          Month(2005, 12), Month(2009, 8), Month(2023, 2), Month(2020, 5), Month(2020, 6), Month(2022, 4),
          Month(2000, 12), Month(2002, 5), Month(2012, 4), Month(2007, 1), Month(2008, 4), Month(2008, 1),
          Month(2000, 11), Month(2006, 8), Month(2011, 9), Month(2012, 12), Month(2015, 9), Month(2017, 12),
          Month(2016, 5), Month(2002, 1), Month(2015, 8), Month(2003, 4), Month(2005, 9), Month(2016, 9),
          Month(2009, 12), Month(2017, 4), Month(2020, 3), Month(2018, 12), Month(2008, 1), Month(2011, 11),
          Month(2004, 9), Month(2004, 9), Month(2002, 5), Month(2014, 6), Month(2023, 5), Month(2016, 11),
          Month(2002, 8), Month(2005, 12), Month(2002, 7), Month(2008, 3), Month(2015, 4), Month(2010, 10),
          Month(2014, 7), Month(2022, 9), Month(2001, 11), Month(2003, 1), Month(2000, 4), Month(2012, 7),
          Month(2004, 1), Month(2011, 6), Month(2012, 8), Month(2008, 9), Month(2005, 2), Month(2007, 8),
          Month(2012, 1), Month(2018, 7), Month(2022, 12), Month(2018, 11), Month(2001, 5), Month(2009, 10),
          Month(2000, 8), Month(2008, 4), Month(2018, 10), Month(2003, 5), Month(2020, 12), Month(2011, 3),
          Month(2003, 12), Month(2023, 3), Month(2003, 1), Month(2020, 7), Month(2019, 4), Month(2020, 2),
          Month(2005, 11), Month(2008, 7), Month(2013, 9), Month(2015, 4), Month(2004, 12), Month(2001, 2),
          Month(2003, 9), Month(2021, 6), Month(2020, 9), Month(2000, 10), Month(2021, 4), Month(2014, 11),
          Month(2016, 9), Month(2004, 12), Month(2015, 10), Month(2009, 1)]

print(sorted(months))
print(min(months))
print(max(months))