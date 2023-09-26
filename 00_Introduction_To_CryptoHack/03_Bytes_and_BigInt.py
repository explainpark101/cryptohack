from codeserver import _print
string = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

if True:
    from Crypto.Util.number import bytes_to_long, long_to_bytes
    string = long_to_bytes(int(string))
else:
    string = bytes.fromhex(hex(int(string))[2:])

print(string)
for i in range(min(list(string))):
    s = "".join([chr(o - i) if  chr(o^i) != "\n" or chr(o^i) != "\r" else "" for o in list(string)])
    if not s.startswith("crypto"): continue
    print(f"{i = :3f}")
    _print(s)
print("END")