import logging
from multiprocessing import cpu_count, Pool
from time import time

def divisor_without_remainder(num: int) -> list:
        list_dividers = []
        for i in range(1, num + 1):
            if (num % i) == 0:
                list_dividers.append(i)
        return list_dividers


def factorize_synchronous_version(*numbers):
    return [divisor_without_remainder(i) for i in numbers]


def factorize_asynchronous_version(*numbers):
    num_cpus = cpu_count()
    logging.debug(f"Кількість логічних ядер: {num_cpus}")

    with Pool(num_cpus) as pool:
        result = pool.map(divisor_without_remainder, numbers)
    return (res for res in result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')


    '''aсинхронна версія'''
    timer_on = time()
    a, b, c, d  = factorize_asynchronous_version(128, 255, 99999, 10651060)
    timer_off = time()
    print('Асинхронна версія:', timer_off - timer_on, 's')


    '''синхронна версія'''
    timer_on = time()
    a, b, c, d  = factorize_synchronous_version(128, 255, 99999, 10651060)
    timer_off = time()
    print('Синхронна версія:', timer_off - timer_on, 's')


    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]