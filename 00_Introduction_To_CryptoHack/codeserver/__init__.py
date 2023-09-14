def _print(*args):
    print(*args)
    with open(__file__+".txt", "w") as f:
        for arg in args:
            f.write(arg)
            f.write("\n")