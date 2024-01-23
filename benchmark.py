import timeit
from kmp import kmp_search
from rk import rabin_karp_search
from bm import boyer_moore_search


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped

def measure_time(search_function, text, pattern):
    wrapped_method = wrapper(search_function, text, pattern)
    execution_time = timeit.timeit(wrapped_method, number=1000)
    return execution_time


print('стаття 1')
with open("стаття 1.txt", "r") as file:
    text1 = file.read()
    print(f'kmp_search для існуючого підрядка {measure_time(kmp_search, text1, "Висновки"):.3f}')
    print(f'kmp_search для не існуючого підрядка {measure_time(kmp_search, text1, "Висновки не існують"):.3f}')

    print(f'rabin_karp_search для існуючого підрядка {measure_time(rabin_karp_search, text1, "Висновки"):.3f}')
    print(f'rabin_karp_search для не існуючого підрядка {measure_time(rabin_karp_search, text1, "Висновки не існують"):.3f}')

    print(f'boyer_moore_search для існуючого підрядка {measure_time(boyer_moore_search, text1, "Висновки"):.3f}')
    print(f'boyer_moore_search для не існуючого підрядка {measure_time(boyer_moore_search, text1, "Висновки не існують"):.3f}')

print('стаття 2')
with open("стаття 2.txt", "r") as file:
    text2 = file.read()
    print(f'kmp_search для існуючого підрядка {measure_time(kmp_search, text2, "Висновки"):.3f}')
    print(f'kmp_search для не існуючого підрядка {measure_time(kmp_search, text2, "Висновки не існують"):.3f}')

    print(f'rabin_karp_search для існуючого підрядка {measure_time(rabin_karp_search, text2, "Висновки"):.3f}')
    print(f'rabin_karp_search для не існуючого підрядка {measure_time(rabin_karp_search, text2, "Висновки не існують"):.3f}')

    print(f'boyer_moore_search для існуючого підрядка {measure_time(boyer_moore_search, text2, "Висновки"):.3f}')
    print(f'boyer_moore_search для не існуючого підрядка {measure_time(boyer_moore_search, text2, "Висновки не існують"):.3f}')