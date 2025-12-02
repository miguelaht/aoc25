import timeit
import io
import sys
from main import part_1, part_2, part_2_simulated

instructions = """
R21
L50
"""

class DummyOut:
    def write(self, x): pass
    def flush(self): pass

def benchmark(func, instructions, number=1000):
    def wrapped():
        # redirect stdout so prints don't affect timings
        old_stdout = sys.stdout
        sys.stdout = DummyOut()
        try:
            func(instructions)
        finally:
            sys.stdout = old_stdout

    return timeit.timeit(wrapped, number=number)

# Run benchmark
runs = 500  # reduce/increase depending on desired precision/speed

t1 = benchmark(part_1, instructions, number=runs)
t2 = benchmark(part_2_simulated, instructions, number=runs)
t3 = benchmark(part_2, instructions, number=runs)

print(f"part_1:            {t1:.6f} seconds total   ({t1/runs:.6f} per run)")
print(f"part_2_simulated:  {t2:.6f} seconds total   ({t2/runs:.6f} per run)")
print(f"part_2:            {t3:.6f} seconds total   ({t3/runs:.6f} per run)")
