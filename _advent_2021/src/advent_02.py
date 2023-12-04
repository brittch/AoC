import numpy as np
import util
from functools import reduce
import math


def day_06_a():
    fish_colony = []
    with open('data/06.txt') as f:
        fish_colony = [int(i) for i in f.readlines()[0].split(',')]
        # fish_colony = np.array([3, 4, 3, 1, 2])

    spawn_check = [None for _ in range(300)]
    total = 0
    for age in fish_colony:
        total += 1 + calc_fish_age(age, 256, spawn_check)
    print(f"FISH: {total}")


def calc_fish_age(age, days_rem, spawn_check):
    spawn = days_rem - age
    family = 0
    while spawn >= 1:
        if spawn_check[spawn]:
            family += spawn_check[spawn]
        else:
            spawn_check[spawn] = 1 + calc_fish_age(8, spawn - 1, spawn_check)
            family += spawn_check[spawn]
        spawn -= 7
    return family


def day_07():
    with open('data/07.txt') as f:
        crab_pos = [int(i) for i in f.readlines()[0].split(',')]
    # crab_pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    # figure out cheapest position for eberyone to meet at
    min_pos = min(crab_pos)
    max_pos = max(crab_pos)

    calc_fuel_cost = calc_fuel_cost_b  # calc_fuel_cost_a

    print(f"min {min_pos} and max {max_pos}")
    fuel_cost = [None] * (max_pos - min_pos)
    for pos in range(len(fuel_cost)):
        print(f"POSITION {pos} *************")
        total_gas = 0
        for crab in crab_pos:
            total_gas += calc_fuel_cost(pos, crab)
        fuel_cost[pos] = total_gas
    print(fuel_cost)
    min_fuel = min(fuel_cost)
    print(f"MIN FUEL: {min_fuel} at meeting coord {fuel_cost.index(min_fuel)}")


def calc_fuel_cost_a(pos, crab):
    return abs(pos-crab)


def calc_fuel_cost_b(pos, crab):
    # print(f"crab {crab} at position: {pos} ****************************")
    base_cost = abs(pos-crab)
    summed_cost = 0
    for x in range(base_cost):
        summed_cost += x + 1  # offseet 0 index
        # print(f"x: {x} - summed_cost: {summed_cost}")
    return summed_cost


def day_08():
    with open('data/08.txt') as f:
        readings = f.readlines()
    # readings = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    #              "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    #              "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    #              "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    #              "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    #              "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    #              "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    #              "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    #              "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    #              "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
    parsed_readings = parse_readings(readings)
    simple_numbers = 0
    for key in parsed_readings:
        display_numbers = key.split(" ")
        for num in display_numbers:
            num = num.strip()
            if len(num) == 3 or len(num) == 7 or len(num) == 2 or len(num) == 4:
                simple_numbers += 1
    print(simple_numbers)


def day_08_b():
    with open('data/08.txt') as f:
        readings = f.readlines()
    # readings = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    #             "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    #             "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    #             "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    #             "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    #             "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    #             "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    #             "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    #             "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    #             "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
    parsed_readings = parse_readings(readings)
    number_digits = [0] * 4
    sum = 0
    for key in parsed_readings:
        wire_map = [num.strip() for num in parsed_readings[key]]
        wire_key = untangle_wires(wire_map)
        numbers = [num.strip() for num in key.split(" ")]
        # print(f"KEY: {wire_key}")
        # print(f"NUMBERS: {numbers}")
        for i, num in enumerate(numbers):
            # print(f"i: {i} - num: {num}")
            wire_val = list(filter(lambda x: util.contains_all(num, x) and len(x) == len(num), wire_key))[0]
            number_digits[i] = wire_key.index(wire_val)
            # print(f"YES: {number_digits[i]}")
            # print("***********")
        print(f"{number_digits}: {''.join([str(digit) for digit in number_digits])}")
        sum += int("".join([str(digit) for digit in number_digits]))
        # print("***********")

    print(f"OUTPUT: {sum}")


def parse_readings(readings):
    parsed_readings = {}
    for row in readings:
        values = row.split(' | ')
        wiring_key = values[0].split(' ')
        parsed_readings[values[1]] = wiring_key
    return parsed_readings


def untangle_wires(wire_map):
    key = [None, list(filter(lambda num: len(num) == 2, wire_map))[0], None, None,
           list(filter(lambda num: len(num) == 4, wire_map))[0], None, None,
           list(filter(lambda num: len(num) == 3, wire_map))[0],
           list(filter(lambda num: len(num) == 7, wire_map))[0], None]
    right = key[1]
    top = key[7].replace(right[0], '').replace(right[1], '')
    left_middle = key[4].replace(right[0], '').replace(right[1], '')
    left_bottom = key[8].replace(right[0], '').replace(right[1], '')\
        .replace(top, '').replace(left_middle[0], '').replace(left_middle[1], '')
    for num in wire_map:
        if len(num) == 5:
            if util.contains_all(num, right):
                key[3] = num
            elif util.contains_all(num, left_middle):
                key[5] = num
            elif util.contains_all(num, left_bottom):
                key[2] = num
        elif len(num) == 6:
            if util.contains_all(num, right) and util.contains_all(num, left_middle):
                key[9] = num
            elif util.contains_all(num, left_bottom) and util.contains_all(num, left_middle):
                key[6] = num
            else:
                key[0] = num
    return key


def day_09():
    with open('data/09.txt') as f:
        height_map = f.readlines()
    # height_map = ["2199943210\n",
    #               "3987894921\n",
    #               "9856789892\n",
    #               "8767896789\n",
    #               "9899965678\n"]
    parsed_map = parse_height_map(height_map)
    basin_counter = []
    for i, row in enumerate(parsed_map):
        for j, height in enumerate(row):
            if is_low_check(i, j, parsed_map):
                print(f"LOW POINT! {i, j} HEIGHT - {parsed_map[i][j]} *************************************")
                basin = count_basin(i, j, parsed_map, [])
                basin_counter.append(len(basin))
                print(f"{basin} - COUNT: {len(basin)}")
    print(basin_counter)
    results = []
    while len(results) < 3:
        results.append(basin_counter.pop(basin_counter.index(max(basin_counter))))
    print(f"{results}: {reduce((lambda x, y: x * y), results)}")


def parse_height_map(h_map):
    parsed_map = []
    for row in h_map:
        row = [int(x) for x in row.strip()]
        parsed_map.append(row)
    return parsed_map


def is_low_check(row_index, col_index, map):
    is_lowest = False
    height = map[row_index][col_index]
    below, above, left, right = get_neighbors(row_index, col_index, map)
    if (above[0] is None or (above[0] is not None and height < above[0])) and \
            (below[0] is None or (below[0] is not None and height < below[0])) and \
            (left[0] is None or (left[0] is not None and height < left[0])) and \
            (right[0] is None or (right[0] is not None and height < right[0])):
        is_lowest = True
    #print(f"height: {height}")
    #print(is_lowest)
    return is_lowest


def get_neighbors(row_index, col_index, map):
    max_y = len(map) - 1
    max_x = len(map[0]) - 1
    below, above, left, right = None, None, None, None
    if row_index > 0:
        above = map[row_index - 1][col_index]
    if row_index < max_y:
        below = map[row_index + 1][col_index]
    if col_index > 0:
        left = map[row_index][col_index - 1]
    if col_index < max_x:
        right = map[row_index][col_index + 1]
    # print(f"max_y: {max_y} - max_x: {max_x} - row_index: {row_index} - col_index: {col_index}")
    # print(f"above: {above}\n below: {below}\n left: {left}\n right: {right}")
    return [below, row_index + 1, col_index], [above, row_index - 1, col_index], \
           [left, row_index, col_index - 1], [right, row_index, col_index + 1]


def count_basin(row_index, col_index, map,basin_pt):
    # print(f"INITIAL: {row_index, col_index}")
    basin_pt.append((row_index, col_index))
    below, above, left, right = get_neighbors(row_index, col_index, map)
    height = map[row_index][col_index]
    if height < 9:
        for neighbor in [below, above, left, right]:
            # print(f"NEIGHBOR: {neighbor}")
            # print(f"IS {(neighbor[1], neighbor[2])} in not basin_pt? {(neighbor[1], neighbor[2]) not in basin_pt}")
            if neighbor[0] is not None and neighbor[0] < 9 and (neighbor[1], neighbor[2]) not in basin_pt:
                count_basin(neighbor[1], neighbor[2], map, basin_pt)
    # print("DONE!")
    return basin_pt


def day_10():
    syntax_key = {")": "(", "]": "[", "}":"{", ">": "<"}
    with open('data/10.txt') as f:
        chunks = f.readlines()
    # chunks = ["[({(<(())[]>[[{[]{<()<>>\n",
    #           "[(()[<>])]({[<{<<[]>>(\n",
    #           "{([(<{}[<>[]}>{[]{[(<()>\n",
    #           "(((({<>}<{<{<>}{[]{[]{}\n",
    #           "[[<[([]))<([[{}[[()]]]\n",
    #           "[{[{({}]{}}([{[{{{}}([]\n",
    #           "{<[[]]>}<{[{[{[]{()[[[]\n",
    #           "[<(<(<(<{}))><([]([]()\n",
    #           "<{([([[(<>()){}]>(<<{{\n",
    #           "<{([{{}}[<[[[<>{}]]]>[]]"]
    result_list = []
    points = 0
    for row in chunks:
        r = syntax_checker(row.strip(), syntax_key)
        if r:
            result_list.append(r)
    points += ''.join(result_list).count(")") * 3
    points += ''.join(result_list).count("]") * 57
    points += ''.join(result_list).count("}") * 1197
    points += ''.join(result_list).count(">") * 25137
    print(f"POINTS: {points}")


def day_10_b():
    syntax_key = {")": "(", "]": "[", "}": "{", ">": "<"}
    with open('data/10.txt') as f:
        chunks = f.readlines()
    # chunks = ["[({(<(())[]>[[{[]{<()<>>\n",
    #           "[(()[<>])]({[<{<<[]>>(\n",
    #           "{([(<{}[<>[]}>{[]{[(<()>\n",
    #           "(((({<>}<{<{<>}{[]{[]{}\n",
    #           "[[<[([]))<([[{}[[()]]]\n",
    #           "[{[{({}]{}}([{[{{{}}([]\n",
    #           "{<[[]]>}<{[{[{[]{()[[[]\n",
    #           "[<(<(<(<{}))><([]([]()\n",
    #           "<{([([[(<>()){}]>(<<{{\n",
    #           "<{([{{}}[<[[[<>{}]]]>[]]"]
    result_list = []
    points = []
    for row in chunks:
        if syntax_checker(row.strip(), syntax_key) is None:
            result_list.append(syntax_completer(row, syntax_key))
    for r in result_list:
        r_points = 0
        for c in r:
            r_points = r_points * 5
            if c == ")":
                r_points += 1
            elif c == "]":
                r_points += 2
            elif c == "}":
                r_points += 3
            elif c == ">":
                r_points += 4
        points.append(r_points)
    points.sort()
    middle_index = math.floor(len(points) / 2)
    print(points)
    print(middle_index)
    print(points[middle_index])


def syntax_checker(row, syntax_key):
    openers = list(syntax_key.values())
    closers = list(syntax_key.keys())
    open_record = []
    for c in row:
        if c in openers:
            open_record.append(c)
        elif c in closers and len(open_record) > 0:
            if syntax_key.get(c) != open_record.pop():
                return c
        else:
            print("fuckey")
            return c
    return None


def syntax_completer(row, syntax_key):
    openers = list(syntax_key.values())
    closers = list(syntax_key.keys())
    open_record = []
    finish_it = []
    # print(f"ROW: {row}")
    for c in row:
        # print(c)
        if c in openers:
            open_record.append(c)
        elif c in closers and len(open_record) > 0:
            open_record.pop()
            # print(f"CLOSER! '{c}' closes? '{open_record.pop()}'")
    # print(f"OPENS: {''.join(open_record)}")
    for i in range(len(open_record)-1, -1, -1):
        finish_it.append(list(syntax_key.keys())[list(syntax_key.values()).index(open_record[i])])
    return finish_it


if __name__ == "__main__":
    day_10_b()
