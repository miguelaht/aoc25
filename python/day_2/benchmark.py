import timeit
import io
import sys
from main import part_1, part_2, part_2_improved

id_ranges = """11-22""".split(",")

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
runs = 10  # reduce/increase depending on desired precision/speed

t1 = benchmark(part_1, id_ranges, number=runs)
t2 = benchmark(part_2, id_ranges, number=runs)
t3 = benchmark(part_2_improved, id_ranges, number=runs)

print(f"part_1:            {t1:.6f} seconds total   ({t1/runs:.6f} per run)")
print(f"part_2:            {t2:.6f} seconds total   ({t2/runs:.6f} per run)")
print(f"part_2_improved:   {t3:.6f} seconds total   ({t3/runs:.6f} per run)")
