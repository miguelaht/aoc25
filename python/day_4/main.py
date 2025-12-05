paper_rolls_map = """
...
.@.
...
"""
paper_rolls_map = list(map(list, paper_rolls_map.split("\n")))
# add padding columns to each end of each row
paper_rolls_map = [["0"] + row + ["0"] for row in paper_rolls_map ]
# add padding rows
padding_row = [0] * len(paper_rolls_map[0])
paper_rolls_map = [padding_row] + paper_rolls_map + [padding_row]
removed = []

def replace_removed_rolls():
    for pos in removed:
        paper_rolls_map[pos[0]][pos[1]] = "X"

def remove_rolls(repeat=False):
    count = 0
    # skip padding at both ends
    for i, line in enumerate(paper_rolls_map[1:-1], start=1):
        # skip padding at both ends
        for j, column in enumerate(line[1:-1], start=1):
            # skip empty columns and paddings
            if column == "." or column == "0" or column == "X":
                continue

            # start at -1 to exclude current roll
            rolls_count = -1
            # adjacent previows row
            rolls_count += paper_rolls_map[i-1][j-1:j+2].count("@")
            # adjacent current row
            rolls_count += paper_rolls_map[i][j-1:j+2].count("@")
            # adjacent next row
            rolls_count += paper_rolls_map[i+1][j-1:j+2].count("@")

            if rolls_count < 4:
                removed.append((i,j))
                count += 1

    print("removed {} rolls. Total = {}".format(count, len(removed)))
    if count > 0 and repeat:
        replace_removed_rolls()
        remove_rolls(repeat)

remove_rolls(repeat=True)
