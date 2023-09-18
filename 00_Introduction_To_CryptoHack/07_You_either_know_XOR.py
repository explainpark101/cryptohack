from codeserver import _print, xor, intJoin
from base64 import b64decode, b64encode

def main():
    print("\n")
    string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    string = bytes.fromhex(string)
    _string = b64encode(string)
    for i in range(100000000):
        tmp = intJoin((xor(_string, i)))
        _tmp = intJoin((xor(string, i)))
        if tmp.startswith('c'):
            print(tmp)
        if _tmp.startswith("c"):
            print(_tmp)
        if not _tmp.startswith("c") and not tmp.startswith('c'):
            print(f"{i=}", end="\r")
    print("\nEND")


if __name__ == "__main__":
    main()