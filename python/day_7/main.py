diagram = """...S...
......
..^...
......"""

def timelines(lines=[]):
    width = len(lines[0])

    for r, line in enumerate(lines):
        if "S" in line:
            start_row = r
            start_col = line.index("S")
            break
    beam_counts = {start_col: 1}

    for r in range(start_row + 1, len(lines)):
        new_counts = {}
        for c, count in beam_counts.items():
            if lines[r][c] == "^":
                if c > 0:
                    new_counts[c - 1] = new_counts.get(c - 1, 0) + count
                    print("r={}, c={}, count={} new_counts[c-1]={}+count".format(r, c, count, new_counts.get(c-1, 0)));
                if c < width - 1:
                    new_counts[c + 1] = new_counts.get(c + 1, 0) + count
                    print("r={}, c={}, count={} new_counts[c+1]={}+count".format(r, c, count, new_counts.get(c+1, 0)));
            else:
                new_counts[c] = new_counts.get(c, 0) + count
                print("r={}, c={}, count={} new_counts[c]={}+count".format(r, c, count, new_counts.get(c, 0)));
        beam_counts = new_counts
    return sum(beam_counts.values())

def traverse(lines=[]):
    split_count = 0
    last_positions=[]

    for row_index, line in enumerate(lines):

        new_positions = []

        if "S" in line:
            last_positions = [(0, line.index("S"))]
            continue

        if "^" not in line:
            new_positions = [(row_index, col) for (_, col) in last_positions]

        else:
            splitter_positions = [j for j, c in enumerate(line) if c == "^"]
            splits = []

            for pos in splitter_positions:
                if (row_index - 1, pos) in last_positions:
                    splits.append((0, pos - 1))
                    splits.append((0, pos + 1))
                    split_count += 1

            straight = [(row_index, col)
                        for (_, col) in last_positions
                        if col not in splitter_positions]
            new_positions = straight + splits

        last_positions = new_positions

    return split_count



lines = diagram.splitlines()
part1 = traverse(lines)
part2 = timelines(lines)

print("Part 1 (splits):", part1)
print("Part 2 (timelines):", part2)

