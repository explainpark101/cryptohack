from codeserver import _print, xor, intJoin

string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
string = bytes.fromhex(string)

_print(*(intJoin(xor(i, string)) for i in range(1000) if intJoin(xor(i, string)).startswith("crypto")))