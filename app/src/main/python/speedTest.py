import time
import random

def fib(n):
    """計算斐波那契數列的第n項"""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def sort_random_numbers():
    """生成一個包含10000個隨機數的列表並排序"""
    numbers = [random.randint(1, 100000) for _ in range(10000)]
    numbers.sort()
    return True

def measure_performance():
    """測量和輸出各項操作的執行時間"""
    start_time = time.time()
    fib_result = fib(30)  # 計算斐波那契數列的第30項，可根據需要調整此值
    fib_time = time.time() - start_time

    start_time = time.time()
    sort_result = sort_random_numbers()
    sort_time = time.time() - start_time
    print(f"fib_time: {fib_time}, sort_time: {sort_time}")
    return f"fib_time: {fib_time},\n sort_time: {sort_time},\n fib_result: {fib_result},\n sort_result: {sort_result}"