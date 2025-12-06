from functools import reduce
from pprint import pprint
import re

original_sheet = """5973
6499
4319
8513
+"""

def compute(exercises, operators):
    result = 0
    for pos, exercise in enumerate(exercises):
        match operators[pos]:
            case "*":
                result += reduce(lambda a, b: a * b, exercise)
            case "/":
                result += reduce(lambda a, b: a / b, exercise)
            case "+" :
                result += reduce(lambda a, b: a + b, exercise)
            case "-" :
                result += reduce(lambda a, b: a - b, exercise)

    return result

def parse_part1(sheet, columns):
    exercises = []
    for p in range(0, columns):
        exercises = exercises + [[row[p] for row in sheet]]

    return exercises

def parse_part2(sheet, operators_row):
    # pass the unparsed sheet
    positions = [i for i, op in enumerate(operators_row) if op != "" or i == len(operators_row)-1]
    sheet_lines = sheet.split("\n")[:-1]

    end = 0
    distance = 0
    exercises = []
    numbers = []

    for i, p in enumerate(positions):
        cols = []
        if i < len(positions)-1:
            next = positions[i+1]
            distance = next - p
            cols = [line[end:end+distance] for line in sheet_lines]
        else:
            cols = [line[end:] for line in sheet_lines]

        end = end+distance+1
        exercises = [cols] + exercises

    for e, exercise in enumerate(exercises):
        exercise = [ex for ex in exercise if ex != ""]

        l = max(list(map(len, exercise)))
        ex = []
        for i in range(l-1, -1, -1):
            n = "".join([num[i] for num in exercise])
            ex.append(int(n))
        numbers.append(ex)

    return numbers


sheet = original_sheet.split("\n")
operators_row = original_sheet.split("\n")[-1].split(" ")
operators = [op for op in operators_row if op != ""]
sheet = [[int(n) for n in row if n != ""] for row in [r.split(" ") for r in sheet[0:-1]]]
cols = len(operators)

exercises = parse_part1(sheet, cols)
result_1 = compute(exercises, operators)
print("part_1 {}".format(result_1))

exercises = parse_part2(original_sheet, operators_row)
result_2 = compute(exercises, operators[::-1])
print("part_2 {}".format(result_2))
