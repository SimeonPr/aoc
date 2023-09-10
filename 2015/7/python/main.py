# signal to "how to calculate"


def and_function(a, b):
    return a & b


def or_function(a, b):
    return a | b


def lshift_function(a, b):
    return a << b


def rshift_function(a, b):
    return a >> b


keyword_to_function = {
        "AND": and_function,
        "OR": or_function,
        "LSHIFT": lshift_function,
        "RSHIFT": rshift_function
        }


signal_to_calc = {}
cache = {"hits": 0}


def eval_signal(signal):
    if signal in cache:
        cache["hits"] = cache["hits"] + 1
        return cache[signal]
    if signal.isdigit():
        return int(signal)
    else:
        calc = signal_to_calc[signal]
        if len(calc) == 1:
            res = eval_signal(calc[0])
        elif len(calc) == 2:
            if calc[0] == "NOT":
                res = ~eval_signal(calc[1])
        elif len(calc) == 3:
            res = keyword_to_function[calc[1]](
                    eval_signal(calc[0]),
                    eval_signal(calc[2]))
        cache[signal] = res
        return res


def main():
    global cache
    with open("../input.txt", "r") as f:
        for line in f:
            tmp = line.rstrip().split(' ')
            signal_to_calc[tmp[-1]] = tmp[0:-2]
    res = eval_signal('a')
    print(f"{cache['hits']} cache hits")
    print(f"The signal 'a' evaluates to {res}")
    print("Overriding b with a")
    signal_to_calc['b'] = [str(res)]
    cache = {"hits": 0}
    res = eval_signal('a')
    print(f"{cache['hits']} cache hits")
    print(f"The signal 'a' evaluates to {res}")
if __name__ == "__main__":
    main()
