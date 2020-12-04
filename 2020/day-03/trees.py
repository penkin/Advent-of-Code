def get_map_data_character(map_data: list, x: int, y: int) -> str:
    """
    Gets the character found in the map data at the given x and y positions. Since the
    map tiles, if we get an index error on the x value, we can simply tile the line and
    try again.
    :param map_data:
    :param x:
    :param y:
    :return:
    """
    line = map_data[y]

    try:
        character = line[x]
        return character
    except IndexError:
        map_data[y] = map_data[y] * 2
        return get_map_data_character(map_data, x, y)


def run_path(map_data: list, move_x: int, move_y: int, tree: str = "#") -> int:
    """
    Runs the map path for the give movement x and y steps. If the character found at the
    spot and it matches the passed in tree character it is counted with the total trees
    being returned.
    :param map_data:
    :param move_x:
    :param move_y:
    :param tree:
    :return:
    """
    position_x = 0
    position_y = 0
    number_of_trees = 0

    while position_y < len(map_data) - 1:
        position_x += move_x
        position_y += move_y
        character = get_map_data_character(map_data, position_x, position_y)

        if character == tree:
            number_of_trees += 1

    return number_of_trees


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [line.strip() for line in f]

        trees = run_path(data, 3, 1)
        print('Trees: ', trees)

        trees_1_1 = run_path(data, 1, 1)
        trees_5_1 = run_path(data, 5, 1)
        trees_7_1 = run_path(data, 7, 1)
        trees_1_2 = run_path(data, 1, 2)

        print('Trees multiplied: ', trees * trees_1_1 * trees_5_1 * trees_7_1 * trees_1_2)
