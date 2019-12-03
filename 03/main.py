def main():
    with open("input.txt", "r") as f:
        wire1 = f.readline().strip().split(",")
        wire2 = f.readline().strip().split(",")

    path1 = get_path(wire1)
    path2 = get_path(wire2)

    interactions = find_intersections(path1, path2)

    print(get_min_path(interactions))
    print(get_min_length(path1, path2, interactions))


def get_path(wire):
    visited_positions = list()

    for val in wire:
        direction = val[0]
        length = int(val[1:])
        last_visited = get_last_visited(visited_positions)
        last_x = last_visited[0]
        last_y = last_visited[1]

        if direction == "L":
            goal_x = last_x - length
            iter_x = last_x
            while iter_x != goal_x:
                iter_x -= 1
                visited_positions.append((iter_x, last_y))
        elif direction == "U":
            goal_y = last_y + length
            iter_y = last_y
            while iter_y != goal_y:
                iter_y += 1
                visited_positions.append((last_x, iter_y))
        elif direction == "R":
            goal_x = last_x + length
            iter_x = last_x
            while iter_x != goal_x:
                iter_x += 1
                visited_positions.append((iter_x, last_y))
        elif direction == "D":
            goal_y = last_y - length
            iter_y = last_y
            while iter_y != goal_y:
                iter_y -= 1
                visited_positions.append((last_x, iter_y))

    return visited_positions


def find_intersections(path1, path2):
    return set(path1) & set(path2)


def get_last_visited(my_list):
    if len(my_list) == 0:
        return (0, 0)

    return my_list.copy().pop()


def get_min_path(duplicates):
    min_path = 9999999
    for i in duplicates:
        x = i[0] if i[0] > 0 else -1*i[0]
        y = i[1] if i[1] > 0 else -1*i[1]
        path_length = x+y
        if path_length < min_path:
            min_path = path_length

    return min_path


def get_min_length(path1, path2, duplicates):
    min_steps = 9999999
    for val in duplicates:
        total_steps = count_steps(path1, val) + count_steps(path2, val)
        if total_steps < min_steps:
            min_steps = total_steps

    return min_steps


def count_steps(path, goal):
    i = 0
    while path[i] != goal:
        i += 1

    return i + 1


main()
