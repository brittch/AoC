import numpy as np
import util
import math
from operator import itemgetter
from collections import defaultdict


def day_11():
    with open('data/11.txt') as f:
        dumbos = f.readlines()
    # dumbos = ["5483143223\n",
    #          "2745854711\n",
    #          "5264556173\n",
    #          "6141336146\n",
    #          "6357385478\n",
    #          "4167524645\n",
    #          "2176841721\n",
    #          "6882881134\n",
    #          "4846848554\n",
    #          "5283751526"]
    dumbo_map = (dumbos)
    total_flashes = 0
    print(f"STEP {0}")
    for row in dumbo_map:
        print(row)
    for step in range(100):
        print(f"STEP {step + 1}")
        post_flashed = []
        for row_index, row in enumerate(dumbo_map):
            for col_index, col in enumerate(row):
                flashes = tako_charging(row_index, col_index, dumbo_map, post_flashed)
        total_flashes += len(flashes)
        for row in dumbo_map:
            print(row)
    print(f"total_flashes: {total_flashes}")


def day_11_b():
    with open('data/11.txt') as f:
        dumbos = f.readlines()
    # dumbos = ["5483143223\n",
    #           "2745854711\n",
    #           "5264556173\n",
    #           "6141336146\n",
    #           "6357385478\n",
    #           "4167524645\n",
    #           "2176841721\n",
    #           "6882881134\n",
    #           "4846848554\n",
    #           "5283751526"]
    dumbo_map = util.parse_map(dumbos)
    all_flash = 0
    step = 0
    print(f"STEP {step}")
    for row in dumbo_map:
        print(row)
    while all_flash == 0:
        print(f"STEP {step + 1}")
        post_flashed = []
        for row_index, row in enumerate(dumbo_map):
            for col_index, col in enumerate(row):
                flashes = tako_charging(row_index, col_index, dumbo_map, post_flashed)
        for row in dumbo_map:
            print(row)
        if len(flashes) == 100:
            all_flash = step + 1
            print(f"****************** ALL FLASHED! ******************")
        step += 1
    print(all_flash)


def tako_charging(row_index, col_index, dumbo_map, post_flashed):
    if dumbo_map[row_index][col_index] == 9:
        dumbo_map[row_index][col_index] = 0
        post_flashed.append((row_index, col_index))
        neighbors = util.get_all_neighbors(row_index, col_index, dumbo_map)
        for n in neighbors:
            if n[0] is not None and (n[1], n[2]) not in post_flashed:
                tako_charging(n[1], n[2], dumbo_map, post_flashed)
    elif (row_index, col_index) not in post_flashed:
        dumbo_map[row_index][col_index] = dumbo_map[row_index][col_index] + 1
    return post_flashed


def day_12():
    with open('data/12.txt') as f:
        cave_system = f.readlines()
    # cave_system = ["start-A\n",
    #                "start-b\n",
    #                "A-c\n",
    #                "A-b\n",
    #                "b-d\n",
    #                "A-end\n",
    #                "b-end\n"]
    # cave_system = ["dc-end\n",
    #                "HN-start\n",
    #                "start-kj\n",
    #                "dc-start\n",
    #                "dc-HN\n",
    #                "LN-dc\n",
    #                "HN-end\n",
    #                "kj-sa\n",
    #                "kj-HN\n",
    #                "kj-dc\n"]
    # cave_system = ["fs-end\n",
    #                "he-DX\n",
    #                "fs-he\n",
    #                "start-DX\n",
    #                "pj-DX\n",
    #                "end-zg\n",
    #                "zg-sl\n",
    #                "zg-pj\n",
    #                "pj-he\n",
    #                "RW-he\n",
    #                "fs-DX\n",
    #                "pj-RW\n",
    #                "zg-RW\n",
    #                "start-pj\n",
    #                "he-WI\n",
    #                "zg-he\n",
    #                "pj-fs\n",
    #                "start-RW"]
    cave_dict = parse_cave_system(cave_system)
    print(cave_dict)
    paths = set()
    calc_caves('start', ['start'], cave_dict, paths)
    print("******************************************************************")
    print(len(paths))
    for x in sorted(paths):
        print(x)


def day_12_b():
    with open('data/12.txt') as f:
        cave_system = f.readlines()
    # cave_system = ["start-A\n",
    #                "start-b\n",
    #                "A-c\n",
    #                "A-b\n",
    #                "b-d\n",
    #                "A-end\n",
    #                "b-end\n"]
    # cave_system = ["dc-end\n",
    #                "HN-start\n",
    #                "start-kj\n",
    #                "dc-start\n",
    #                "dc-HN\n",
    #                "LN-dc\n",
    #                "HN-end\n",
    #                "kj-sa\n",
    #                "kj-HN\n",
    #                "kj-dc\n"]
    # cave_system = ["fs-end\n",
    #                "he-DX\n",
    #                "fs-he\n",
    #                "start-DX\n",
    #                "pj-DX\n",
    #                "end-zg\n",
    #                "zg-sl\n",
    #                "zg-pj\n",
    #                "pj-he\n",
    #                "RW-he\n",
    #                "fs-DX\n",
    #                "pj-RW\n",
    #                "zg-RW\n",
    #                "start-pj\n",
    #                "he-WI\n",
    #                "zg-he\n",
    #                "pj-fs\n",
    #                "start-RW"]
    cave_dict = parse_cave_system(cave_system)
    print(cave_dict)
    paths = set()

    lower_caves = list(filter(lambda l: l.islower() and l != 'start' and l != 'end', list(cave_dict.keys())))
    lower_caves_set = set(lower_caves)
    for c in list(cave_dict.values()):
        c_filtered = list(filter(lambda l: l.islower() and l != 'start' and l != 'end', c))
        lower_caves_set.update(c_filtered)
    caves_array = {list(lower_caves_set)[i]: 0 for i in range(0, len(list(lower_caves_set)))}
    print(caves_array)

    calc_caves_v2('start', ['start'], cave_dict, paths, caves_array)
    print("******************************************************************")
    print(len(paths))
    # for x in sorted(paths):
    #    print(x)


def calc_caves(node, history, cave_dict, paths):
    if node is not None and node != 'end':
        choices = cave_dict.get(node)
        if choices is None:
            choices = []
        origins = list(filter(lambda x: node in cave_dict[x], list(cave_dict.keys())))
        print(f"NODE: {node} ORIGIN: {origins}")
        for o in origins:
            if o != 'start' and \
               o not in choices and \
               (len(history) > 0 and history[len(history)-1] != o):
                choices.append(o)
        if len(history) > 2:
            last_cave = history[len(history) - 2]
            if last_cave.isupper() and node != last_cave and last_cave not in choices:
                choices.append(last_cave)
        if choices:
            print(f"\tNODE: {node} choices: {choices} history: {history}")
            for c in choices:
                if (c.islower() and c not in history) or c.isupper():
                    history.append(c)
                    calc_caves(c, history, cave_dict, paths)
        history.pop()
    else:
        paths.add(", ".join(history))
        history.pop()
        return


def calc_caves_v2(node, history, cave_dict, paths, visited):
    if node is not None and node != 'end':
        choices = cave_dict.get(node)
        if choices is None:
            choices = []
        origins = list(filter(lambda x: node in cave_dict[x], list(cave_dict.keys())))
        for o in origins:
            if o != 'start' and \
               o not in choices and \
               (len(history) > 0 and history[len(history)-1] != o):
                choices.append(o)
        if len(history) > 2:
            last_cave = history[len(history) - 2]
            if last_cave.isupper() and node != last_cave and last_cave not in choices:
                choices.append(last_cave)
        if choices:
            print(f"NODE: {node} choices: {choices} history: {','.join(history)} visited: {visited}")
            for c in choices:
                if (c.islower() and c != 'end' and c != 'start' and (max(visited.values()) < 2 or (max(visited.values()) == 2 and visited[c] < 1)))\
                        or c == 'end' or c.isupper():
                    history.append(c)
                    if c.islower() and c != 'start' and c != 'end':
                        visited[c] += 1
                    print(f"\t\tCHOICE: {c} HISTORY: {','.join(history)}")
                    calc_caves_v2(c, history, cave_dict, paths, visited)
        rewind = history.pop()
        if rewind.islower() and rewind != 'start' and rewind != 'end':
            visited[rewind] -= 1
    else:
        paths.add(",".join(history))
        # print(f"PATHS: {paths}")
        rewind = history.pop()
        if rewind.islower() and rewind != 'start' and rewind != 'end':
            visited[rewind] -= 1
        return


def parse_cave_system(cave_system):
    cave_dict = dict()
    for connection in cave_system:
        parts = connection.strip().split('-')
        if parts[0] not in cave_dict:
            cave_dict[parts[0]] = [parts[1]]
        else:
            cave_dict.get(parts[0]).append(parts[1])
    return cave_dict


def day_13():
    with open('data/13.txt') as f:
        instructions = f.readlines()
    # instructions = ["6,10\n",
    #                 "0,14\n",
    #                 "9,10\n",
    #                 "0,3\n",
    #                 "10,4\n",
    #                 "4,11\n",
    #                 "6,0\n",
    #                 "6,12\n",
    #                 "4,1\n",
    #                 "0,13\n",
    #                 "10,12\n",
    #                 "3,4\n",
    #                 "3,0\n",
    #                 "8,4\n",
    #                 "1,10\n",
    #                 "2,14\n",
    #                 "8,10\n",
    #                 "9,0\n",
    #                 "\n",
    #                 "fold along y=7\n",
    #                 "fold along x=5"]
    dots, folds = parse_instructions(instructions)
    # print_paper(dots)
    # print("****************")

    for fold in folds:
        # print(f"FOLD! {fold}")
        dots = fold_paper(fold[0], fold[1], dots)
    print_paper(dots)
    print(dots)
    print(f"DOT COUNT: {len(dots)}")


def parse_instructions(instructions):
    fold_label = "along "
    dots = []
    folds = []
    for row in instructions:
        row = row.strip()
        if len(row) > 1 and fold_label not in row:
            points = row.split(",")
            dots.append((int(points[0]), int(points[1])))
        elif fold_label in row:
            fold_raw = row.split(fold_label)
            fold = fold_raw[1].split("=")
            folds.append((fold[0], int(fold[1])))
    return dots, folds


def fold_paper(direction, line, dots):
    # print(f"direction: {direction} line: {line} num of dots: {len(dots)}")
    folded_dots = []
    if direction == "x":
        index = 0
    else:
        index = 1
    folded_dots = folded_dots + list(filter(lambda x: x[index] < line, dots))
    bottom_fold = list(set(dots) - set(folded_dots))
    folded = [increment_dots(x, line, index) for x in bottom_fold]
    return set(folded_dots + folded)


def increment_dots(dot, line, index):
    dot = list(dot)
    dot[index] = dot[index] - ((dot[index] - line) * 2)
    return tuple(dot)


def print_paper(dots):
    height = max(dots, key=itemgetter(1))[1]
    width = max(dots, key=itemgetter(0))[0]
    for y in range(height + 1):
        for x in range(width + 1):
            if (x, y) in dots:
                print("#", end='')
            else:
                print(".", end='')
        print("")


def day_14():
    with open('data/14.txt') as f:
        template = f.readlines()
    # template = ["NNCB\n",
    #             "\n",
    #             "CH -> B\n",
    #             "HH -> N\n",
    #             "CB -> H\n",
    #             "NH -> C\n",
    #             "HB -> C\n",
    #             "HC -> B\n",
    #             "HN -> C\n",
    #             "NN -> C\n",
    #             "BH -> H\n",
    #             "NC -> B\n",
    #             "NB -> B\n",
    #             "BN -> B\n",
    #             "BB -> N\n",
    #             "BC -> B\n",
    #             "CC -> N\n",
    #             "CN -> C"]
    polymer, template_dict = parse_template(template)
    master_polymer = ""
    for i in range(10):
        print(f"STEP {i + 1}")
        for pair in range(len(polymer)):
            if (pair + 1) < len(polymer):
                polymer_pair = polymer[pair] + polymer[pair+1]
                insertion = template_dict.get(polymer_pair)
                if insertion:
                    polymer_pair = polymer[pair] + insertion + polymer[pair+1]
                if pair + 1 == len(polymer) - 1:
                    master_polymer += polymer_pair
                else:
                    master_polymer += polymer_pair[0:len(polymer_pair)-1]
        print(f"\tLENGTH: {len(master_polymer)}")  # : {master_polymer}
        polymer = master_polymer
        master_polymer = ""

        final_polymer = np.array(list(polymer))
        unique = list(np.unique(final_polymer))
        most = 0
        least = 99999999
        for c in unique:
            count = polymer.count(c)
            print(f"\t\t{c}: {count}")
            if count > most:
                most = count
            if count < least:
                least = count
        print(f"TOTAL: {most} - {least} = {most - least}")


def day_14_b():
    with open('data/14.txt') as f:
        template = f.readlines()
    # template = ["NNCB\n",
    #             "\n",
    #             "CH -> B\n",
    #             "HH -> N\n",
    #             "CB -> H\n",
    #             "NH -> C\n",
    #             "HB -> C\n",
    #             "HC -> B\n",
    #             "HN -> C\n",
    #             "NN -> C\n",
    #             "BH -> H\n",
    #             "NC -> B\n",
    #             "NB -> B\n",
    #             "BN -> B\n",
    #             "BB -> N\n",
    #             "BC -> B\n",
    #             "CC -> N\n",
    #             "CN -> C"]
    # polymer, template_dict = parse_template(template)
    template, _, *rules = "".join(template).split('\n')
    rules = dict(r.split(" -> ") for r in rules)

    pairs = defaultdict(int)
    for a, b in zip(template, template[1:]):
        pairs[a + b] += 1

    chars = defaultdict(int)
    for a in template: chars[a] += 1

    for _ in range(40):
        for (a, b), c in pairs.copy().items():
            x = rules[a + b]
            pairs[a + b] -= c
            pairs[a + x] += c
            pairs[x + b] += c
            chars[x] += c

    print(max(chars.values()) - min(chars.values()))


def parse_template(template):
    polymer = template[0].strip()
    instructions = {}
    for i, row in enumerate(template):
        if i > 1:
            instruct = row.strip().split(" -> ")
            instructions[instruct[0]] = instruct[1]
    return polymer, instructions


def day_15():
    with open('data/15.txt') as f:
        readings = f.readlines()
    readings = ["1163751742\n",
                "1381373672\n",
                "2136511328\n",
                "3694931569\n",
                "7463417111\n",
                "1319128137\n",
                "1359912421\n",
                "3125421639\n",
                "1293138521\n",
                "2311944581"]
    readings = ["11637\n",
                "13813\n",
                "21365"]
    risk_map = util.parse_map(readings)
    for row in risk_map:
        print(row)
    end_pos = (len(risk_map) - 1, len(risk_map[0]) - 1)
    start_pos = util.get_neighbors_dpad(0, 0, risk_map)
    path = calc_route(risk_map, start_pos, [], [(0, 0)], end_pos)
    print(path)


def calc_route(risk_map, neighbors, path, path_hist, end):
    possible_route = []
    choices = {}
    for n in neighbors:
        neighbor_location = (n[1], n[2])
        if neighbor_location == end:
            path.append(n[0])
            return path
        elif n[0] is None:
            path.append(999)
            return path

        if neighbor_location not in path_hist:
            path_hist.append(neighbor_location)
        else:
            path.append(999)
            return
        new_neighbors = util.get_neighbors_dpad(n[1], n[2], risk_map)
        possible_route.append([n[0]] + calc_route(risk_map, new_neighbors, path, path_hist, end))
    for route in possible_route:
        index = sum(route)
        choices[index] = possible_route
    smallest_route = min(list(choices.keys()))
    path = path + smallest_route
    return


if __name__ == "__main__":
    day_15()
