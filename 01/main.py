def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(part_one(data))
    print(part_two(data))


def calc_fuel(mass):
    return int((int(mass) / 3) - 2)


def part_one(numbers):
    total = 0
    for n in numbers:
        total += calc_fuel(n)

    return total


def part_two(numbers):
    total = 0
    for n in numbers:
        fuel = calc_fuel(n)
        while fuel > 0:
            total += fuel
            fuel = calc_fuel(fuel)

    return total


main()
