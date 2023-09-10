grid = {}


def transform_rectangle(pointA, pointB, transform):
    tmp = pointA.split(',')
    ax = int(tmp[0])
    ay = int(tmp[1])
    tmp = pointB.split(',')
    bx = int(tmp[0])
    by = int(tmp[1])
    for x in range(ax, bx+1, 1 if ax < bx else -1):
        for y in range(ay, by+1, 1 if ay < by else -1):
            grid[f"{x},{y}"] = transform(grid[f"{x},{y}"])


def toogle(input):
    return not input


def toggle_2(input):
    return input + 2


def turn_on(input):
    return input + 1


def turn_off(input):
    if input == 0:
        return 0
    return input - 1


def set_light(value):
    def helper_function(point):
        return value
    return helper_function


def init_grid():
    for x in range(1000):
        for y in range(1000):
            grid[f"{x},{y}"] = False


def count_brightness(hash_map):
    brightness = 0
    for x in range(1000):
        for y in range(1000):
            brightness += hash_map[f"{x},{y}"]
    return brightness


def count_lights(hash_map):
    counter = 0
    for x in range(1000):
        for y in range(1000):
            if hash_map[f"{x},{y}"]:
                counter = counter + 1
    return counter


def main():
    init_grid()
    with open("../input.txt", "r") as f:
        for line in f:
            print(line)
            fields = line.split(' ')
            if fields[0] == "toggle":
                transform_rectangle(fields[1], fields[3], toggle_2)
            else:
                if fields[1] == "on":
                    transform_rectangle(fields[2], fields[4], turn_on)
                else:
                    transform_rectangle(fields[2], fields[4], turn_off)
    lights = count_brightness(grid)
    print(f"{lights} lights are on!\n")


if __name__ == "__main__":
    main()
