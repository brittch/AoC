import string
import pandas as pd


def day_1():
    with open('_data/01.txt') as f:
        lines = f.readlines()
        elves = list()
        cal_sum = 0
        for cal in lines:
            if cal == '\n':
                elves.append(cal_sum)
                cal_sum = 0
            else:
                cal_sum += int(cal)
        if cal_sum != 0:
            elves.append(cal_sum)

        elves.sort(reverse=True)
        print(f"Sum of calories from top three elves: {elves[0] + elves[1] + elves[2]}")


def day_2a():
    points = {
        "X": {"points": 1, "A": 3, "B": 0, "C": 6},
        "Y": {"points": 2, "A": 6, "B": 3, "C": 0},
        "Z": {"points": 3, "A": 0, "B": 6, "C": 3}
    }
    with open('_data/02.txt') as f:
        # match = f.readlines()
        match = ["A Y\n",
                 "B X\n",
                 "C Z\n"]
        total_points = 0
        for m in match:
            moves = m.split(" ")
            my_move = moves[1].strip()
            total_points += points.get(my_move).get("points")
            total_points += points.get(my_move).get(moves[0])

        print(f"Points! {total_points}")


def day_2b():
    points = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    shapes = {
        "A": {"X": 3, "Y": 1, "Z": 2},
        "B": {"X": 1, "Y": 2, "Z": 3},
        "C": {"X": 2, "Y": 3, "Z": 1},
    }
    with open('_data/02.txt') as f:
        match = f.readlines()
        # match = ["A Y\n",
        #         "B X\n",
        #         "C Z\n"]
        total_points = 0
        for m in match:
            moves = m.split(" ")
            my_outcome = moves[1].strip()
            total_points += points.get(my_outcome)
            total_points += shapes.get(moves[0]).get(my_outcome)

        print(f"Points! {total_points}")


def day_3():
    with open('_data/03.txt') as f:
        sacks = f.readlines()
        # sacks = ["vJrwpWtwJgWrhcsFMMfFFhFp\n",
        #         "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
        #         "PmmdzqPrVvPwwTWBwg\n",
        #         "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
        #         "ttgJtRGJQctTZtZT\n",
        #         "CrZsJsPPZsGzwwsLwLmpwMDw\n"]

        total_priority = 0
        group = []
        for s in sacks:
            group.append(s.strip())
            if len(group) == 3:
                intersection = (set(group[0]) & set(group[1]) & set(group[2])).pop()

                priority = string.ascii_lowercase.index(intersection.lower()) + 1
                if intersection.isupper():
                    priority += 26
                total_priority += priority

                group = []

        print(f"total_priority: {total_priority}")


def day_4():
    with open('_data/04.txt') as f:
        assignments = f.readlines()
        # assignments = ["2-4,6-8",
        #                "2-3,4-5",
        #                "5-7,7-9",
        #                "2-8,3-7",
        #                "6-6,4-6",
        #                "2-6,4-8"]
        count = 0
        for asmnt in assignments:
            pair = asmnt.strip().split(",")
            one = pair[0].split("-")
            two = pair[1].split("-")
            one_series = []
            two_series = []
            one_series.extend(range(int(one[0]), int(one[1]) + 1))
            two_series.extend(range(int(two[0]), int(two[1]) + 1))

            #if set(one_series) <= set(two_series) or set(two_series) <= set(one_series):
            if not set(one_series).isdisjoint(two_series):
                count += 1
        print(count)


def day_5():
    with open('_data/05.txt') as f:
        instructions = f.readlines()
        # instructions = ["    [D]    \n",
        #                 "[N] [C]    \n",
        #                 "[Z] [M] [P]\n",
        #                 " 1   2   3 \n",
        #                 "\n",
        #                 "move 1 from 2 to 1\n",
        #                 "move 3 from 1 to 3\n",
        #                 "move 2 from 2 to 1\n",
        #                 "move 1 from 1 to 2\n"]
        diagram, steps = day_5_parse(instructions)
        print(f"{diagram}\n{steps}")
        for s in steps:
            num_boxes = s.get("count")
            move = diagram[s.get("origin") - 1][0:num_boxes]
            del diagram[s.get("origin") - 1][0:num_boxes]
            diagram[s.get("dest") - 1] = move + diagram[s.get("dest") - 1]
            # for i in range(s.get("count")):
            #    box = diagram[s.get("origin") - 1].pop(0)
            #    diagram[s.get("dest") - 1].insert(0, box)
        print(f"{''.join([diagram[i].pop(0) for i in range(len(diagram))])}")


def day_5_parse(instructions):
    fold = instructions.index("\n")
    diagram = instructions[:fold]
    steps = instructions[fold + 1:]

    stps = []
    for s in steps:
        pass_1 = s.split("move")[1].split("from")
        pass_2 = pass_1[1].split("to")
        stps.append({
            "count": int(pass_1[0]),
            "origin": int(pass_2[0]),
            "dest": int(pass_2[1].strip()),
        })

    col_labels = diagram[len(diagram)-1].strip()
    col_count = int(col_labels[len(col_labels) - 1])
    diagram_aray = [[] for i in range(col_count)]

    for row in diagram:
        if row != diagram[len(diagram)-1]:  # col label
            for spot in range(0, int(len(row.replace(' ', '*'))/4)):
                column = "".join(row[0 + (4*spot): 4 + (4*spot)])
                if column != "    " and column != "   \n":
                    box = column.replace("[", "").replace("]", "").strip()
                    diagram_aray[spot].append(box)

    return diagram_aray, stps


def day_6():
    with open('_data/06.txt') as f:
        signal = f.readlines()
        # signal = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        #           "bvwbjplbgvbhsrlpgdmjqwftvncz",
        #           "nppdvjthqldpwncqszvftbrmjlhg",
        #           "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        #           "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]

        for a in signal:
            marker = ""
            for i in range(len(a)):
                if marker == "":
                    sample = a[0 + i: 14 + i]
                    for j in range(len(sample)):
                        if sample[j] in sample[j + 1:]:
                            break
                        elif j == len(sample) - 1:
                            marker = i + 14
                            break
                else:
                    break
            print(f"Packet index: {marker}")


def day_7():
    with open('_data/07.txt') as f:
        terminal_cmd = f.readlines()
        system = {"name": "/", "children": [], "parent": None, "size": 0}
        current_node = system
        for cmd in terminal_cmd:
            cmd = cmd.split(" ")
            if "$" in cmd:
                if "cd" in cmd:
                    dir_name = cmd[2].strip()
                    if dir_name != current_node.get("name") and dir_name != "..":
                        current_node = [item for item in current_node.get("children") if item.get("name") == dir_name][0]
                    elif dir_name != current_node.get("name") and dir_name == "..":
                        current_node = day_07_parent_walk(system, current_node.get("parent"))
                elif "ls" in cmd:
                    break  # nothing to do, just go to next ine to consume
            else:
                if cmd[0] == 'dir':
                    if len(list(filter(lambda obj: obj.get("name") == cmd[1].strip(), current_node.get("children")))) == 0:
                        current_node.get("children").append({"name": cmd[1].strip(),
                                                             "children": [],
                                                             "parent": current_node.get("name"),
                                                             "size": 0})
                else:
                    current_node.get("children").append({"name": cmd[1].strip(),
                                                         "children": [],
                                                         "size": int(cmd[0]),
                                                         "parent": current_node.get("name")})
        size_sum = day_07_folder_sum(system, 0)
        print(f"total sum: {size_sum}")


def day_07_parent_walk(node, parent_name):
    if node.get("name") != parent_name:
        for child in node.get("children"):
            return day_07_parent_walk(child, parent_name)
    else:
        return node


def day_07_folder_sum(node, size_sum):
    children = node.get("children")
    if not children:
        return node.get("size")
    else:
        for child in children:
            return size_sum + day_07_folder_sum(child, size_sum)
    print(f"Name: {node.get('name')} -- SIZE: {size_sum}")
    return size_sum


if __name__ == '__main__':
    day_7()
