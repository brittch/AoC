def contains_all(str, set):
    return 0 not in [c in str for c in set]


def get_all_neighbors(row_index, col_index, map):
    max_y = len(map) - 1
    max_x = len(map[0]) - 1
    neighbors = [None, None, None, None, None, None, None, None]
    if row_index > 0:
        neighbors[1] = map[row_index - 1][col_index]
    if row_index < max_y:
        neighbors[5] = map[row_index + 1][col_index]
    if col_index > 0:
        neighbors[7] = map[row_index][col_index - 1]
    if col_index < max_x:
        neighbors[3] = map[row_index][col_index + 1]
    if row_index > 0 and col_index > 0:
        neighbors[0] = map[row_index - 1][col_index - 1]
    if row_index < max_y and col_index < max_x:
        neighbors[4] = map[row_index + 1][col_index + 1]
    if col_index > 0 and row_index < max_y:
        neighbors[6] = map[row_index + 1][col_index - 1]
    if col_index < max_x and row_index > 0:
        neighbors[2] = map[row_index - 1][col_index + 1]
    return [neighbors[5], row_index + 1, col_index], [neighbors[1], row_index - 1, col_index], \
           [neighbors[7], row_index, col_index - 1], [neighbors[3], row_index, col_index + 1], \
           [neighbors[0], row_index - 1, col_index - 1], [neighbors[2], row_index - 1, col_index + 1], \
           [neighbors[4], row_index + 1, col_index + 1], [neighbors[6], row_index + 1, col_index - 1]


def get_neighbors_dpad(row_index, col_index, map):
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
    return [below, row_index + 1, col_index], [above, row_index - 1, col_index], \
           [left, row_index, col_index - 1], [right, row_index, col_index + 1]


def parse_map(h_map):
    parsed_map = []
    for row in h_map:
        row = [int(x) for x in row.strip()]
        parsed_map.append(row)
    return parsed_map
