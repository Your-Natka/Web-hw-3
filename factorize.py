from multiprocessing import Pool, cpu_count
from time import time

def factorize_single(n: int):
    return [i for i in range(1, n + 1) if n % i == 0]

def factorize(*numbers):
    return [factorize_single(n) for n in numbers]

def factorize_parallel(*numbers):
    with Pool(processes=cpu_count()) as pool:
        return pool.map(factorize_single, numbers)

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    start = time()
    res_seq = factorize(*numbers)
    print(f"Sync time: {time() - start:.2f}s")

    start = time()
    res_par = factorize_parallel(*numbers)
    print(f"Parallel time: {time() - start:.2f}s")

    a, b, c, d = res_par
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
