from codeserver import _print
from Crypto.Util.number import bytes_to_long, long_to_bytes
string = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
string = int(string)
# string = string.to_bytes(0, 'big')
string = long_to_bytes(string)
print(string)
for i in range(min(list(string))):
    s = "".join([chr(o - i) if  chr(o^i) != "\n" or chr(o^i) != "\r" else "" for o in list(string)])
    if not s.startswith("crypto"): continue
    print(f"{i = :3f}")
    _print(s)
print("END")