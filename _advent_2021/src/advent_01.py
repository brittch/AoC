import csv
import numpy as np

from enums import Directions


def day_01_a():
    with open('data/01.csv', newline='') as csv_file:
        readings = csv.reader(csv_file, delimiter='\n')
        readings_list = list(readings)
        print(f"Number of readings: {len(readings_list)}")
        increase_counter = 0
        prev_reading = None
        for reading in readings_list:
            r = int(reading[0])
            print(f"prev: {prev_reading} vs. {r}")
            if prev_reading is not None and r > prev_reading:
                print(f"INCREASE!")
                increase_counter += 1
            prev_reading = r
        print(f"Increases: {increase_counter}")


def day_01_b():
    with open('data/01.csv', newline='') as csv_file:
        readings = csv.reader(csv_file, delimiter='\n')
        readings_list = list(readings)
        num_readings = len(readings_list)
        print(f"Number of readings: {num_readings}")
        increase_counter = 0
        prev_sum = None
        for i in range(num_readings):
            if i + 3 <= num_readings:
                r_sum = int(readings_list[i][0]) + int(readings_list[i+1][0]) + int(readings_list[i+2][0])
                print(f"{i}: {r_sum}")
                if prev_sum is not None and r_sum > prev_sum:
                    print(f"prev_sum: {prev_sum} vs. r_sum: {r_sum}")
                    increase_counter += 1
                prev_sum = r_sum
        print(f"Increases: {increase_counter}")


def day_02_a():
    with open('data/02.txt') as f:
        lines = f.readlines()
        x_coord = 0
        y_coord = 0
        for line in lines:
            command = line.strip().split()
            if command[0] == 'forward':
                x_coord += int(command[1])
                print(f"command: {command} : x_coord: {x_coord}")
            elif command[0] == 'up':
                y_coord -= int(command[1])
                print(f"command: {command} : y_coord: {y_coord}")
            elif command[0] == 'down':
                y_coord += int(command[1])
                print(f"command: {command} : y_coord: {y_coord}")
        print(f"x_coord: {x_coord} x y_coord: {y_coord}")
        print(x_coord * y_coord)


def day_02_b():
    with open('data/02.txt') as f:
        lines = f.readlines()
        horizontal = 0
        depth = 0
        aim = 0
        for line in lines:
            command = line.strip().split()
            value = int(command[1])
            if command[0] == 'forward':
                horizontal += value
                depth += (aim * value)
                print(f"command: {command} : horizontal: {horizontal} - depth: {depth}")
            elif command[0] == 'up':
                aim -= value
                print(f"command: {command} : aim: {aim}")
            elif command[0] == 'down':
                aim += value
                print(f"command: {command} : aim: {aim}")
        print(f"horizontal: {horizontal} x depth: {depth} aim: {aim}")
        print(horizontal * depth)


def day_03_a():
    gamma_rate = []
    epsilon_rate = []
    with open('data/03.txt') as f:
        lines = f.readlines()
        positions = len(lines[0].strip())
        for i in range(positions):
            one = 0
            zero = 0
            for line in lines:
                bit = line.strip()
                if bit[i] == "1":
                    one += 1
                elif bit[i] == "0":
                    zero += 1
            if one > zero:
                gamma_rate.append(1)
                epsilon_rate.append(0)
            else:
                gamma_rate.append(0)
                epsilon_rate.append(1)

    print(f"gamma_rate:{gamma_rate} - epsilon_rate:{epsilon_rate}")
    gamma_rate = int("".join(str(i) for i in gamma_rate), 2)
    epsilon_rate = int("".join(str(i) for i in epsilon_rate), 2)
    print(f"gamma_rate:{gamma_rate} - epsilon_rate:{epsilon_rate}")
    print(gamma_rate * epsilon_rate)


def day_03_b():
    with open('data/03.txt') as f:
        lines = f.readlines()
        positions = len(lines[0].strip())
        oxy_bit_val = day_03_b_sub(positions, lines, 'oxy')
        c02_bit_val = day_03_b_sub(positions, lines, 'c02')

    print(f"oxygen_bit:{oxy_bit_val} - c02_bit:{c02_bit_val}")
    oxygen = int(oxy_bit_val, 2)
    c02 = int(c02_bit_val, 2)
    print(f"oxygen:{oxygen} - c02:{c02}")
    print(oxygen * c02)


def day_03_b_sub(pos_num, readings, val_type):
    filtered_readings = readings
    print(f"INIT length of values: {len(readings)} of reading type {val_type}")
    for i in range(pos_num):
        if len(filtered_readings) > 1:
            print(f"position {i}")
            one = 0
            zero = 0
            for line in filtered_readings:
                bit = line.strip()
                if bit[i] == "1":
                    one += 1
                elif bit[i] == "0":
                    zero += 1
            print(f"ones: {one} vs zeros: {zero}")
            if (val_type == 'oxy' and (one > zero or one == zero)) or (val_type == 'c02' and (one < zero)):
                print(f"Filtering out Non-1s at position {i}")
                filtered_readings = list(filter(lambda bit_val: bit_val.strip()[i] == '1', filtered_readings))
                print(f"{len(filtered_readings)} values left")
            elif (val_type == 'oxy' and one < zero) or (val_type == 'c02' and (one > zero or one == zero)):
                print(f"Filtering out Non-0s at position {i}")
                filtered_readings = list(filter(lambda bit_val: bit_val.strip()[i] == '0', filtered_readings))
                print(f"{len(filtered_readings)} values left")
    return filtered_readings[0]


def day_04_a():
    called_nums = [17, 2, 33, 86, 38, 41, 4, 34, 91, 61, 11, 81, 3, 59, 29, 71, 26, 44, 54, 89, 46, 9, 85, 62, 23, 76,
                   45, 24, 78, 14, 58, 48, 57, 40, 21, 49, 7, 99, 8, 56, 50, 19, 53, 55, 10, 94, 75, 68, 6, 83, 84, 88,
                   52, 80, 73, 74, 79, 36, 70, 28, 37, 0, 42, 98, 96, 92, 27, 90, 47, 20, 5, 77, 69, 93, 31, 30, 95, 25,
                   63, 65, 51, 72, 60, 16, 12, 64, 18, 13, 1, 35, 15, 66, 67, 43, 22, 87, 97, 32, 39, 82]
    with open('data/04.txt') as f:
        board_results = {}

        lines = f.readlines()
        all_boards = build_bingo_boards(lines)
        winning_board, called_balls = announce_balls(called_nums, all_boards, board_results)
        for row in winning_board:
            print(row)
        print(called_balls)
        flattened = list(np.array(winning_board).flatten())
        print(flattened)
        remains = sum(list(filter(lambda val: val not in called_balls, flattened)))
        print(f"{remains} x {called_balls[len(called_balls)-1]}")
        print(remains * called_balls[len(called_balls)-1])


def announce_balls(called_nums, all_boards, board_results):
    spent_balls = []
    for ball in called_nums:
        print(f"* {ball} *")
        spent_balls.append(ball)
        for i, board in enumerate(all_boards):
            board_results[i] = stamp_board(board, ball, board_results.get(i))
            if evalute_board(board_results[i]):
                return board, spent_balls
    return None


def stamp_board(board, ball, board_status):
    if board_status is None:
        board_status = []
    np_board = np.array(board)
    result = np.where(np_board == ball)
    coordinates = list(zip(result[0], result[1]))
    if len(coordinates) == 1:
        board_status.append(coordinates[0])
    return board_status


def evalute_board(board_status):
    bingo = False
    if len(board_status) > 4:
        x = []
        y = []
        for tup in board_status:
            x.append(tup[0])
            y.append(tup[1])
        x_bins = np.bincount(np.array(x))
        y_bins = np.bincount(np.array(y))
        if 5 in x_bins or 5 in y_bins:
            bingo = True
    return bingo


def build_bingo_boards(lines):
    all_boards = list()
    for i in range(0, len(lines)-1, 6):
        board = list()
        for j in range(5):
            row = lines[i+j].strip().replace('  ', ' ')
            row_arr = row.split(' ')
            row_arr = [int(i) for i in row_arr]
            board.append(row_arr)
        all_boards.append(board)
    return all_boards


def day_04_b():
    called_nums = [17, 2, 33, 86, 38, 41, 4, 34, 91, 61, 11, 81, 3, 59, 29, 71, 26, 44, 54, 89, 46, 9, 85, 62, 23, 76,
                   45, 24, 78, 14, 58, 48, 57, 40, 21, 49, 7, 99, 8, 56, 50, 19, 53, 55, 10, 94, 75, 68, 6, 83, 84, 88,
                   52, 80, 73, 74, 79, 36, 70, 28, 37, 0, 42, 98, 96, 92, 27, 90, 47, 20, 5, 77, 69, 93, 31, 30, 95, 25,
                   63, 65, 51, 72, 60, 16, 12, 64, 18, 13, 1, 35, 15, 66, 67, 43, 22, 87, 97, 32, 39, 82]
    with open('data/04.txt') as f:
        board_results = {}

        lines = f.readlines()
        all_boards = build_bingo_boards(lines)

        spent_balls = []
        un_bingoed_boards = build_bingo_boards(lines)
        exhausted_boards = []
        for ball in called_nums:
            if len(exhausted_boards) < 100:
                print(f"* {ball} *")
                spent_balls.append(ball)
                for i, board in enumerate(all_boards):
                    board_results[i] = stamp_board(board, ball, board_results.get(i))
                    if evalute_board(board_results[i]) and len(un_bingoed_boards) > 1:
                        if board not in exhausted_boards:
                            exhausted_boards.append(board)
                            print("REMOVING *************")
                            print(board)
                            print("****")
                            un_bingoed_boards.remove(board)
                            if len(un_bingoed_boards) <= 3:
                                for un_board in un_bingoed_boards:
                                    for row in un_board:
                                        print(row)
                                    print("****")
                    elif evalute_board(board_results[i]) and len(un_bingoed_boards) == 1 and board == un_bingoed_boards[0]:
                        print("*** LAST BOARD ***")
                        print(board_results[i])
                        exhausted_boards.append(board)
                        if len(un_bingoed_boards) <= 5:
                            for un_board in un_bingoed_boards:
                                for row in un_board:
                                    print(row)
                                print("****")
                        for row in board:
                            print(row)
                        winning_board = un_bingoed_boards[0]
                        break
                print(f"un_bingoed_boards:{len(un_bingoed_boards)} vs. exhausted_boards:{len(exhausted_boards)} vs. all_boards:{len(all_boards)}")
        flattened = list(np.array(winning_board).flatten())
        print(flattened)
        print(list(filter(lambda val: val not in spent_balls, flattened)))
        remains = sum(list(filter(lambda val: val not in spent_balls, flattened)))
        print(f"{remains} x {spent_balls[len(spent_balls) - 1]}")
        print(remains * spent_balls[len(spent_balls) - 1])


def day_05_a():
    with open('data/05.txt') as f:
        lines = f.readlines()
        vent_coords = parse_vents(lines)
        # filter only horz and vert lines
        filtered_vent_coords = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], vent_coords))
        # filtered_vent_coords = [[(9, 0), (5, 0)], [(2, 9), (6, 9)],
        #                        [(1, 3), (6, 3)], [(5, 0), (1, 0)],
        #                        [(7, 4), (7, 9)], [(0, 3), (0, 1)],
        #                        [(9, 3), (9, 1)], [(8, 2), (9, 2)]]

        max_x = get_max_value(filtered_vent_coords, "x")
        max_y = get_max_value(filtered_vent_coords, "y")
        grid = [[0] * (max_x + 1) for _ in range(max_y + 1)]

        for line in filtered_vent_coords:
            pt1 = line[0]
            pt2 = line[1]
            if pt1[0] != pt2[0]:
                x = pt1[1]
                y_0 = pt1[0]
                y_1 = pt2[0]
                if pt1[0] > pt2[0]:
                    y_0 = pt2[0]
                    y_1 = pt1[0]
                for y in range(y_0, y_1 + 1):
                    grid[y][x] = grid[y][x] + 1
            else:
                y = pt1[0]
                x_0 = pt1[1]
                x_1 = pt2[1]
                if pt1[1] > pt2[1]:
                    x_0 = pt2[1]
                    x_1 = pt1[1]
                for x in range(x_0, x_1 + 1):
                    grid[y][x] = grid[y][x] + 1
        for row in grid:
            print(row)
        flat_grid = np.array(grid).flatten().tolist()
        filtered_grid = list(filter(lambda pt: pt > 1, flat_grid))
        print(len(filtered_grid))


def parse_vents(lines):
    parsed_lines = []
    for line in lines:
        line = line.strip().split(' -> ')
        parsed_points = []
        for pt in line:
            pts = pt.split(',')
            parsed_points.append((int(pts[0]), int(pts[1])))
        parsed_lines.append(parsed_points)
    return parsed_lines


def get_max_value(lines, type):
    i = 0
    if type == 'x':
        i = 1
    max = 0
    for line in lines:
        for pt in line:
            if pt[i] > max:
                max = pt[i]
    return max


def gen_range(start, stop):
    pts = list()
    x_sign = np.sign(start[1] - stop[1]) * -1
    y_sign = np.sign(start[0] - stop[0]) * -1
    print(f"Y: {start[0]} -> {stop[0]} step:{y_sign}")
    print(f"X: {start[1]} -> {stop[1]} step:{x_sign}")
    y_range = list(range(start[0], stop[0] + y_sign, y_sign))
    x_range = list(range(start[1], stop[1] + x_sign, x_sign))
    print(y_range)
    print(x_range)
    for r in range(len(y_range)):
        pts.append((y_range[r], x_range[r]))
    print(pts)
    return pts


def day_05_b():
    with open('data/05.txt') as f:
        lines = f.readlines()
        vent_coords = parse_vents(lines)
        # vent_coords = [[(9, 0), (5, 0)], [(2, 9), (6, 9)],
        #               [(1, 3), (4, 0)], [(5, 0), (1, 0)],
        #               [(7, 4), (7, 9)], [(6, 5), (9, 8)],
        #               [(9, 3), (9, 1)], [(8, 2), (9, 2)]]

        max_x = get_max_value(vent_coords, "x")
        max_y = get_max_value(vent_coords, "y")
        grid = [[0] * (max_x + 1) for _ in range(max_y + 1)]

        for line in vent_coords:
            pt1 = line[0]
            pt2 = line[1]
            if pt1[0] != pt2[0] and pt1[1] == pt2[1]:  # Hoizantal
                x = pt1[1]
                y_0 = pt1[0]
                y_1 = pt2[0]
                if pt1[0] > pt2[0]:
                    y_0 = pt2[0]
                    y_1 = pt1[0]
                for y in range(y_0, y_1 + 1):
                    grid[y][x] = grid[y][x] + 1
            elif pt1[1] != pt2[1] and pt1[0] == pt2[0]:  # Vertical
                y = pt1[0]
                x_0 = pt1[1]
                x_1 = pt2[1]
                if pt1[1] > pt2[1]:
                    x_0 = pt2[1]
                    x_1 = pt1[1]
                for x in range(x_0, x_1 + 1):
                    grid[y][x] = grid[y][x] + 1
            else:  # Diagonal
                diag_range = gen_range(pt1, pt2)
                for y, x in diag_range:
                    grid[y][x] = grid[y][x] + 1

        for row in grid:
            print(row)
        flat_grid = np.array(grid).flatten().tolist()
        filtered_grid = list(filter(lambda pt: pt > 1, flat_grid))
        print(len(filtered_grid))


if __name__ == "__main__":
    day_05_b()
