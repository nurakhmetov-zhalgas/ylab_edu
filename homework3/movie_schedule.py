from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        """
        Возвращает обьект генератор, который формирует даты показа текущего
        экземпляра(фильма).
        """
        return (
            start_date + timedelta(days=day)
            for start_date, end_date in self.dates
            for day in range((end_date - start_date).days + 1)
        )


if __name__ == "__main__":
    m = Movie(
        "sw",
        [
            (datetime(2020, 1, 1), datetime(2020, 1, 7)),
            (datetime(2020, 1, 15), datetime(2020, 2, 7)),
        ],
    )

    for d in m.schedule():
        print(d)
