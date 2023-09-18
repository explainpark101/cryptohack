from codeserver import _print, xor, intJoin, xor_s
from base64 import b64decode, b64encode


b64keys = []
nb64keys = []
MAGIC_STRING = "crypto{"
ITER_COUNT = 1000
def main():
    print("\n")
    string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    string = bytes.fromhex(string)
    _string = b64encode(string)
    with open("07_You_either_know_XOR.txt", "w") as f:
        f.write("\n")
    for k in range(32, 127):
        b64keys = []
        nb64keys = []   
        _MAGIC_STRING = MAGIC_STRING
        if k>32:
            _MAGIC_STRING += chr(k)
        
        for j, MAGIC in enumerate(_MAGIC_STRING):
            for i in range(10000):
                tmp = intJoin((xor_s(_string, i)))[j:]
                if tmp.startswith(MAGIC):
                    b64keys.append(i)
                    print(f"{i=:5} {tmp=}")
                    break
                if not tmp.startswith(MAGIC):
                    print(f"{i=:5}", end="\r")
        print(b64keys)
        print("\n")
        for j, MAGIC in enumerate(_MAGIC_STRING):
            for i in range(10000):
                _tmp = intJoin((xor_s(string, i)))[j:]
                if _tmp.startswith(MAGIC):
                    nb64keys.append(i)
                    print(f"{i=:5} {_tmp=}")
                    break
                if not _tmp.startswith(MAGIC):
                    print(f"{i=:5}", end="\r")
        print("\n\n")
        ans_nb64 = ""
        for x in range(42):
            idx = x % len(nb64keys)
            _ = chr((string[x] ^ nb64keys[idx]))
            ans_nb64 += _
        print(ans_nb64)
        ans_b64 = ""
        if not len(b64keys):
            for x in range(42):
                print(len(b64keys), b64keys)
                idx = x % len(b64keys)
                _ = chr((_string[x] ^ b64keys[idx]))
                ans_b64 += _
            print(ans_b64)
        lines: list
        with open("07_You_either_know_XOR.txt", "r") as f:
            lines = f.readlines()
        with open("07_You_either_know_XOR.txt", "w+") as f:
            for line in lines:
                f.write(line)
            if ans_nb64.endswith("}"):
                f.write(f"{chr(k)=} : {nb64keys = } || ans >>> \n{ans_nb64}\n\n")
            if ans_b64.endswith("}"):
                f.write(f"{chr(k)=} : {b64keys = } || ans >>> \n{ans_b64}\n\n\n")
        if ans_nb64.endswith("}"): print(f"{chr(k)=} : {nb64keys = } || ans= {ans_nb64}")
        if ans_b64.endswith("}"): print(f"{chr(k)=} : {b64keys = } || ans= {ans_b64}")
    
    print("\nEND")


if __name__ == "__main__":
    main()