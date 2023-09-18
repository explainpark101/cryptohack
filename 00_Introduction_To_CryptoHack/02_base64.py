import base64 as b64
from codeserver import _print
string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
string = bytes.fromhex(string)
print(string)
t = b64.b64encode(string)
print(t)
_print(t.decode())