from pwn import * # pip install pwntools
from base64 import b64decode
import json
import codecs

def json_recv(r):
    line = r.recvline()
    return json.loads(line.decode())

def json_send(r, hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

TYPES = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]
def base64_decode(val:str) -> str:
    return b64decode(val.encode()).decode()

def hex_decode(val:str) -> str:
    return "".join(map(chr, bytes.fromhex(val)))

def rot13_decode(val:str) -> str:
    return codecs.decode(val, 'rot_13')

def bigint_decode(val:str) -> str:
    val = val[2:] if val.startswith("0x") else val
    return bytes.fromhex(val).decode()
    
def utf8_decode(val:list) -> str:
    return "".join([chr(o) for o in val])
    
funcs = {
    "base64":base64_decode,
    "hex":hex_decode,
    "rot13":rot13_decode,
    "bigint":bigint_decode,
    "utf-8":utf8_decode,
}

def main():
    r = remote('socket.cryptohack.org', 13377)
    for _iter in range(100):
        received = json_recv(r)
        print("Received type: ", end="")
        print(received.get("type"))
        print("Received encoded value: ", end="")
        print(received.get("encoded"))
        type = received.get("type")
        val = received.get("encoded")
        decoded = funcs[type](val)
        
        to_send = {
            "decoded": decoded
        }
        print(to_send)
        json_send(r, to_send)
    print(json_recv(r))

if __name__ == "__main__":
    main()
