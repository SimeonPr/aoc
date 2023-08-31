if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        instructions = f.read()
        floor = 0
        entered_basement = False
        for i, c in enumerate(instructions):
            if c == '(':
                floor = floor + 1
            elif c == ')':
                floor = floor - 1
            if (floor == -1) and not entered_basement:
                entered_basement = True
                print(f"Basement entered at index {i}")
        print(f"Final floor: {floor}")
