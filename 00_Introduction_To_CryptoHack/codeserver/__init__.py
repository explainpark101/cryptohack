def _print(*args):
    print(*args)
    with open(__file__+".txt", "w") as f:
        for arg in args:
            f.write(arg)
            f.write("\n")



def optionalIndex(_list, _index, default=None):
    try:
        return _list[_index]
    except IndexError:
        return default
# From 04_XOR_Starter.py
def xor(a1, a2):
    def typeConvert(o):
        return ord(o) if type(o) is str else o
    new = []
    if getattr(a1, "__iter__", None) and getattr(a2, "__iter__", None):
        if len(a1) != len(a2):
            if len(a1) > len(a2):
                for i, _ in enumerate(a1):
                    if not optionalIndex(a2, i, False):
                        a2[i] = 0
            else:
                for i, _ in enumerate(a2):
                    if not optionalIndex(a1, i, False):
                        a1[i] = 0
        new = [int(typeConvert(_a1)^typeConvert(_a2)) for (_a1, _a2) in zip(a1, a2)]
        return new
    if getattr(a1, "__iter__", None):
        return [int(typeConvert(_a1)^typeConvert(a2)) for _a1 in a1]
    if getattr(a2, "__iter__", None):
        return [int(typeConvert(_a2)^typeConvert(a1)) for _a2 in a2]

def xor_s(*args):
    _ = args[0]
    for a in args[1:]:
        _ = xor(_, a)
    return _

def intJoin(_list):
    return "".join([chr(_) for _ in _list])
def join(_list):
    return "".join(_list)

