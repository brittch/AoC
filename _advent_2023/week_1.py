import re


def day_1():
    with open('data/01.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            print(line)
            letters = list(line.strip())
            filtered = list(filter(lambda num: num.isnumeric(), letters))
            number = int(str(filtered[0]) + str(filtered[len(filtered) - 1]))
            print(number)
            total += number
        print(f"TOTAL: {total}")


def day_1_b():
    help_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    with open('data/01.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            print(line)
            letters = list(line.strip())
            filtered_nums = list(filter(lambda num: num.isnumeric(), letters))
            print(filtered_nums)
            filtered_names = [x for x in list(help_dict.keys()) if x in line]
            print(filtered_names)
            if filtered_names:
                one = None
                two = None
                names_dict = {}
                for name in filtered_names:
                    names_dict[line.index(name)] = help_dict[name]
                    names_dict[line.rfind(name)] = help_dict[name]
                names_dict = dict(sorted(names_dict.items()))
                print(names_dict)
                keys = list(names_dict.keys())
                if line.index(filtered_nums[0]) < keys[0]:
                    one = filtered_nums[0]
                else:
                    one = names_dict[keys[0]]
                if line.rfind(filtered_nums[len(filtered_nums) - 1]) > keys[len(keys) - 1]:
                    two = filtered_nums[len(filtered_nums) - 1]
                else:
                    two = names_dict[keys[len(keys) - 1]]
                number = int(str(one) + str(two))
            else:
                number = int(str(filtered_nums[0]) + str(filtered_nums[len(filtered_nums) - 1]))
            print(number)
            total += number
        print(f"TOTAL: {total}")


def day_2():
    with open('data/02.txt') as f:
        games = f.readlines()
        total = 0
        for game in games:
            red = 0
            blue = 0
            green = 0
            parts = game.split(":")
            id = (parts[0].split("Game "))[1]
            each_game = parts[1].split(";")
            for round in each_game:
                colors = list(map(lambda x: x.strip(), round.split(", ")))
                blue_pieces = list(filter(lambda x: "blue" in x, colors))
                if blue_pieces:
                    if blue < int(blue_pieces[0].split(" blue")[0]):
                        blue = int(blue_pieces[0].split(" blue")[0])
                green_pieces = list(filter(lambda x: "green" in x, colors))
                if green_pieces:
                    if green < int((green_pieces[0].split(" green"))[0]):
                        green = int((green_pieces[0].split(" green"))[0])
                red_pieces = list(filter(lambda x: "red" in x, colors))
                if red_pieces:
                    if red < int((red_pieces[0].split(" red"))[0]):
                        red = int((red_pieces[0].split(" red"))[0])
            game_power = red * blue * green
            total += game_power
        print(f"TOTAL: {total}")


def day_3_a():
    with open('data/03.txt') as f:
        lines = f.readlines()
        total = 0
        symbols_master = []
        parts_master = []
        row_num = 0
        for line in lines:
            clean_line = line.strip()
            symbols = [(row_num, idx) for idx, sym in enumerate(list(clean_line)) if not sym.isnumeric() and sym != "."]
            if symbols:
                symbols_master.extend(symbols)
            parts = [(row_num, m.start(), int(m.group())) for m in re.finditer(r'\d+', clean_line)]
            # parts = [(row_num, clean_line.index(num), int(num)) for num in part_numbers]
            # for p in parts:
            #     print(f"{p} -> {clean_line}")
            #     print(f"{re.findall(str(p[2]), clean_line)}")
            if parts:
                parts_master.extend(parts)
            row_num += 1
        # print(symbols_master)
        # print("**********")
        for part in parts_master:
            part_number_len = len(str(part[2]))
            # print(f"{part[2]}: ({part[0]},{part[1]})*************")
            possible = [(part[0] - 1, part[1] - 1), (part[0] - 1, part[1]), (part[0] - 1, part[1] + 1),
                        (part[0], part[1] - 1), (part[0], part[1]), (part[0], part[1] + 1),
                        (part[0] + 1, part[1] - 1), (part[0] + 1, part[1]), (part[0] + 1, part[1] + 1)]
            for x in range(part_number_len - 1):
                possible.extend([(part[0] - 1, (part[1] + x + 1) - 1), (part[0] - 1, (part[1] + x + 1)),
                                 (part[0] - 1, (part[1] + x + 1) + 1),
                                 (part[0], (part[1] + x + 1) - 1), (part[0], (part[1] + x + 1)),
                                 (part[0], (part[1] + x + 1) + 1),
                                 (part[0] + 1, (part[1] + x + 1) - 1), (part[0] + 1, (part[1] + x + 1)),
                                 (part[0] + 1, (part[1] + x + 1) + 1)])
            # print(possible)
            if any(item in possible for item in symbols_master):
                # print("!!YES!!")
                total += part[2]
        print(f"TOTAL: {total} ")


def day_3_b():
    with open('data/03.txt') as f:
        lines = f.readlines()
        total = 0
        symbols_master = []
        parts_master = []
        row_num = 0
        for line in lines:
            clean_line = line.strip()
            gears = [(row_num, idx) for idx, sym in enumerate(list(clean_line)) if sym == "*"]
            if gears:
                symbols_master.extend(gears)
            parts = [(row_num, m.start(), int(m.group())) for m in re.finditer(r'\d+', clean_line)]
            new_parts = []
            for p in parts:
                if len(str(p[2])) > 1:
                    for d in range(len(str(p[2])) - 1):
                        new_parts.append((row_num, p[1] + d + 1, p[2]))
            if parts:
                parts_master.extend(parts)
                parts_master.extend(new_parts)
            row_num += 1
        for gear in symbols_master:
            possible = [(gear[0] - 1, gear[1] - 1), (gear[0] - 1, gear[1]), (gear[0] - 1, gear[1] + 1),
                        (gear[0], gear[1] - 1), (gear[0], gear[1]), (gear[0], gear[1] + 1),
                        (gear[0] + 1, gear[1] - 1), (gear[0] + 1, gear[1]), (gear[0] + 1, gear[1] + 1)]
            gear_parts = day_3_common_elements(possible, parts_master)
            if gear_parts and len(gear_parts) > 1:
                valid_parts = []
                for gear_part in gear_parts:
                    valid = list(filter(lambda x: x[0] == gear_part[0] and x[1] == gear_part[1], parts_master))
                    if len(valid):
                        valid_parts.extend(valid)
                valid_parts = list(set([m[2] for m in valid_parts]))
                if len(valid_parts) == 2:
                    total += valid_parts[0] * valid_parts[1]
        print(f"TOTAL: {total} ")


def day_3_common_elements(list_1, parts_master):
    a_set = set(list_1)
    b_set = set([(part[0], part[1]) for part in parts_master])

    if a_set & b_set:
        return list(a_set & b_set)
    else:
        return False


def day_4_a():
    with open('data/04.txt') as f:
        cards = f.readlines()
        total = 0
        for i, card in enumerate(cards):
            numbers = card.strip().replace("Card", '').replace(f" {i + 1}: ", '').split("|")
            winning_nums = list(filter(lambda x: x != '', numbers[0].strip().split(" ")))
            card_nums = list(filter(lambda x: x != '', numbers[1].strip().split(" ")))
            matches = list(set(winning_nums) & set(card_nums))
            if matches:
                card_total = 1
                for t in range(len(matches) - 1):
                    card_total = card_total * 2
                print(card_total)
                total += card_total
        print(f"TOTAL: {total}")


def day_4_b():
    with open('data/04.txt') as f:
        cards = f.readlines()
        total = 0
        cards_parsed = []
        tally = {}
        for i, card in enumerate(cards):
            numbers = card.strip().replace("Card", '').replace(f" {i + 1}: ", '').split("|")
            winning_nums = list(filter(lambda x: x != '', numbers[0].strip().split(" ")))
            card_nums = list(filter(lambda x: x != '', numbers[1].strip().split(" ")))
            matches = len(list(set(winning_nums) & set(card_nums)))
            cards_parsed.append(matches)
        for i, card in enumerate(cards_parsed):
            tally[i+1] = 1
        for i, card in enumerate(cards_parsed):
            card_num = i+1
            # print(f"CARD NUMBER: {card_num} *************")
            for m in range(card):
                copy = card_num + (m + 1)
                # print(f"COPYING: {copy}")
                tally[copy] = tally[copy] + (1 * tally[card_num])
        # print(cards_parsed)
        # print(tally)
        print(f"TOTAL: {sum(tally.values())}")


if __name__ == '__main__':
    day_4_b()
