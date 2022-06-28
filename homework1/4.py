"""
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.

(Используйте - для обозначения зачеркнутой буквы)
"""


class Solution:
    def __init__(self, s: str) -> None:
        self.data = s
        self.ans = set()

    def helper(self, current: str, remainder: str, search: str) -> None:
        if search == "":
            self.ans.add(current + '-' * len(remainder))
            return
        elif remainder == "":
            return
        if remainder[0] == search[0]:
            self.helper(current + search[0], remainder[1:], search[1:])
        self.helper(current + '-', remainder[1:], search)

    def solve(self) -> None:
        current = ""
        remainder = self.data
        search = "banana"
        self.helper(current, remainder, search)


def bananas(s: str) -> set:
    sol = Solution(s)
    sol.solve()
    return sol.ans
