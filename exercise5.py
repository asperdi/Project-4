import time
from decorator import decorator

@decorator
def repetition_counter(function, *args, **kwargs):
    start = time.time()
    function(*args, **kwargs)
    end = time.time()
    return end - start


@repetition_counter
def function(*args, delay=1):
    for arg in args:
        print(arg)
        time.sleep(delay)


if __name__ == "__main__":
    time = function("Hello", "World", "this", "is", "test", delay=0.5)
    print(f"time of executing the function '{function.__name__}': {time:.4f} seconds")
