import time

def time_dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rs = func(*args)
        end = time.time()
        print(f"The time taken by Program  :  {start - end} Seconds")
        return rs
    return wrapper



