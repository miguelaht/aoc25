ingredients = """1-7

3"""

range_block, ingredient_block = ingredients.split("\n\n")
range_strings = range_block.split("\n")
ingredient_ids = list(map(int, ingredient_block.split("\n")))

fresh_count = 0
fresh_ingredient_ids = []
ranges = [tuple(map(int, r.split("-"))) for r in range_strings]

for ingredient in ingredient_ids:
    for start, end in ranges :
        if end >= ingredient >= start:
            fresh_count += 1
            break

print("part_1", fresh_count)

ranges.sort()
(current_s, current_e) = ranges[0]
count = 0
for (s,e) in ranges[1:]:
    if s <= current_e:
        current_e = max(e, current_e)
        continue
    else:
        count += (current_e - current_s) + 1
        current_s, current_e = s, e

count += (current_e - current_s) + 1

print("part_2", count)
