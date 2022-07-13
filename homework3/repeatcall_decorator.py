import time


def repeat_call(call_count, start_sleep_time, factor, border_sleep_time):
    """
    Декоратор для последующего вызова декорируемой функции.

    Время повторного вызова растет экспоненциально
    до граничного времени ожидания.
    """

    def outer(func):
        def wrapper(*args, **kwargs):
            if call_count:
                print(f"Количество запусков = {call_count}\nНачало работы")
                for number_call in range(call_count):
                    sleep_time = min(
                        start_sleep_time * factor**number_call, border_sleep_time
                    )
                    print(
                        f"Запуск номер {number_call + 1}. "
                        f"Ожидание: {sleep_time} секунд.",
                        end=" ",
                    )
                    time.sleep(sleep_time)
                    result = func(*args, **kwargs)
                    print(f"Результат декорируемой функции = {result}")
                print("Конец работы")

        return wrapper

    return outer
