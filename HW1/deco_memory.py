import psutil
import time

def measure_memory(f):
    def deco(*args, **kwargs):
        start_memory = psutil.virtual_memory().used
        result = f(*args, **kwargs)
        end_memory = psutil.virtual_memory().used
        used_memory = end_memory - start_memory
        print(f"Memory used: {used_memory} bytes")
        return result

    return deco

@measure_memory
def test_f():
    time.sleep(2)
    return "Done"

result = test_f()
print(result)