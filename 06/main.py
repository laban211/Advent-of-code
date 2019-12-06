import re


def main():
    data = get_data()
    # part1
    # print(calc_num_of_orbits(data))
    # part2
    find_santa(data)


def get_data():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def calc_num_of_orbits(data):
    counter = 0
    for line in data:
        child = line[:3]
        counter += count_children(child, data)

    return counter


def count_children(head_child, data):
    counter = 1
    data_str = str(data)

    while True:
        regex = r"\w{3}\)("+head_child+")"
        match = re.search(regex, data_str)

        if match == None:
            break
        head_child = match.group(0)[:3]
        counter += 1
    return counter


def find_santa(data):
    my_path_to_COM = get_path_to_COM(data, "YOU")
    santas_path_to_COM = get_path_to_COM(data, "SAN")

    diff = (list(set(my_path_to_COM) ^ set(santas_path_to_COM)))
    print(len(diff)+2)


def get_path_to_COM(data, who):
    path_to_COM = []
    data_str = str(data)
    regex = r"\w{3}\)("+who+")"
    start_pos = re.search(regex, data_str).group(0)[:3]
    nex = start_pos
    while nex != "COM":
        regex = r"\w{3}\)("+nex+")"
        nex = re.search(regex, data_str).group(0)[:3]
        path_to_COM.append(nex)
    return path_to_COM


main()
