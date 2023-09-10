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


def set_light(value):
    def helper_function(point):
        return value
    return helper_function


def init_grid():
    for x in range(1000):
        for y in range(1000):
            grid[f"{x},{y}"] = False


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
                transform_rectangle(fields[1], fields[3], toogle)
            else:
                if fields[1] == "on":
                    transform_rectangle(fields[2], fields[4], set_light(True))
                else:
                    transform_rectangle(fields[2], fields[4], set_light(False))
    lights = count_lights(grid)
    print(f"{lights} lights are on!\n")


if __name__ == "__main__":
    main()
