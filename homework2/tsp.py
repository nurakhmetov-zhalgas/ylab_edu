"""
Почтальон выходит из почтового отделения,
объезжает всех адресатов один раз для вручения посылки и
возвращается в почтовое отделение.

Необходимо найти кратчайший маршрут для почтальона.

Входные данные:
В первой строчке N - количество точек(включая почтовое отделение).
Далее в следующих N строках координаты точек, разделеленных пробелом.

Пример входных данных:
5
0 2
2 5
5 2
6 6
8 3
"""
from math import inf


class Solution():
    def __init__(self) -> None:
        self.count_points = int(input())
        self.points = [(0, 0) for _ in range(self.count_points)]
        self.graph = [
            [0 for _ in range(self.count_points)]
            for _ in range(self.count_points)
        ]
        self.visited = [False for _ in range(self.count_points)]
        self.min_cost = inf
        self.ans = []
        for i in range(self.count_points):
            self.points[i] = tuple(map(int, input().split()))
        for i in range(self.count_points):
            for j in range(i + 1, self.count_points):
                distance = self.calc_distance(self.points[i], self.points[j])
                self.graph[i][j] = self.graph[j][i] = distance

    def calc_distance(self, point1: tuple[int], point2: tuple[int]) -> float:
        x_cord = (point2[0] - point1[0]) ** 2
        y_cord = (point2[1] - point1[1]) ** 2
        return (x_cord + y_cord) ** 0.5

    def solve(self) -> None:
        def tsp(curr_pos: int, cntr: int, cost: int, way: list[int]) -> None:
            if cntr == self.count_points:
                if cost + self.graph[curr_pos][0] < self.min_cost:
                    self.min_cost = cost + self.graph[curr_pos][0]
                    self.ans = way
                return
            for i in range(self.count_points):
                if self.visited[i] is False:
                    self.visited[i] = True
                    current_cost = cost + self.graph[curr_pos][i]
                    tsp(i, cntr + 1, current_cost, way + [i])
                    self.visited[i] = False

        self.visited[0] = True
        tsp(0, 1, 0, [0])

    def print_ans(self) -> None:
        prev = 0
        passed = 0
        print(self.points[0], end=' ')
        self.ans.append(0)
        for current in self.ans[1:]:
            passed += self.graph[current][prev]
            print('-> ', self.points[current], f'[{passed}]', sep='', end=' ')
            prev = current
        print('=', self.min_cost)


if __name__ == '__main__':
    sol = Solution()
    sol.solve()
    sol.print_ans()
