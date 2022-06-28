"""
Написать метод count_find_num, который принимает на вход
список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые
множители простых чисел primesL.
"""

from functools import reduce


class Solution:
    def __init__(self, primes: list, limit: int) -> None:
        self.primes = primes
        self.limit = limit
        self.count = 0
        self.max_value = 0
        self.visited = set()

    def dfs(self, number) -> None:
        if number > self.limit:
            return
        if number > self.max_value:
            self.max_value = number
        self.count += 1
        for x in self.primes:
            if number * x not in self.visited:
                self.visited.add(number * x)
                self.dfs(number * x)

    def solve(self) -> None:
        start = reduce((lambda a, b: a * b), self.primes)
        self.dfs(start)


def count_find_num(primesL: list, limit: int) -> list:
    s = Solution(primesL, limit)
    s.solve()
    if s.count:
        return [s.count, s.max_value]
    return []
