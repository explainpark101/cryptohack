
def hexToArray(hexstring):
    # return [int(hexstring[i:i+2], 16) for i in range(0, len(hexstring), 2)]
    return bytes.fromhex(hexstring)

def bitwise_xor(str1, str2):
    if isinstance(str1, str):
        str1 = hexToArray(str1)
    if isinstance(str2, str):
        str2 = hexToArray(str2)
    return [a^b for a, b in zip(str1, str2)]

def bitwise_xors(*strs):
    if len(strs) < 2: return None
    tmp = strs[0]
    for _str in strs[1:]:
        tmp = bitwise_xor(_str, tmp)
    return tmp

def intList_to_str(intList):
    return "".join((chr(_) for _ in intList))

def slice_half(iter):
    return iter[:len(iter)//2], iter[len(iter)//2:]


CIPHER_TEXT = "78aba33c48cde9101c698a96ff66b3d4798594230780e4c248d811d0eda6de5e336bc5619f7e50efbda1fd25a399afbc"
PLAIN_TEXT = "1bd9da4c3ca292237f0bd5a38a05d8e126b1e21336e4bbf37f8730f1cc87ff23"


iv, cipher = hexToArray(CIPHER_TEXT[:32]), slice_half(hexToArray(CIPHER_TEXT[32:]))
plain = slice_half(hexToArray(PLAIN_TEXT))

print(f"""
{plain  = }
{cipher = }
{iv     = }
""".strip())

print()

flag = intList_to_str(bitwise_xors(iv, plain[0])) + intList_to_str(bitwise_xor(cipher[0], plain[1]))

print(flag)