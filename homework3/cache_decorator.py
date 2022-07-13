def cache(func):
    """
    Кэширует значения результата функции для последующих вызовов.
    """

    def memo(number):
        if number not in memo.data:
            memo.data[number] = func(number)
        return memo.data[number]

    memo.data = dict()
    return memo


@cache
def multiplier(number: int):
    return number * 2
