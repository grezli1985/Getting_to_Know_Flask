import time


def slow_function():
    print("Начло функции")
    time.sleep(5)
    print("Конец функции")


print("Начало программы")
slow_function()
print("Конец программы")
