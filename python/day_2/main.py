id_ranges = """11-22""".split(",")

def part_1(id_ranges):
    count = 0
    for r in id_ranges:
        min_r, max_r = map(int, r.split("-"))

        for v in range(min_r, max_r+1):
            val = str(v)
            count += v if val == val[:len(val)//2]*2 else 0

    print(count)

def part_2(id_ranges):
    count = 0
    for r in id_ranges:
        min_r, max_r = map(int, r.split("-"))

        for v in range(min_r, max_r+1):
            val = str(v)
            for i in range(0, len(val)//2 + 1):
                t = val[:i]
                if val.replace(t, '') == '':
                    count += v
                    break

    print(count)

def part_2_improved(id_ranges):
    count = 0
    for r in id_ranges:
        min_r, max_r = map(int, r.split("-"))

        for v in range(min_r, max_r+1):
            val = str(v)
            if val in (val+val)[1:-1]:
                count += v
