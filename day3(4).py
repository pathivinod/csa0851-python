def addBinary(a: str, b: str) -> str:
    carry = 0
    result = ""
    a = a[::-1]
    b = b[::-1]
    for i in range(max(len(a), len(b))):
        a_val = int(a[i]) if i < len(a) else 0
        b_val = int(b[i]) if i < len(b) else 0
        s = a_val + b_val + carry
        result += str(s % 2)
        carry = s // 2
    if carry:
        result += str(carry)
    return result[::-1]
print(addBinary("11", "1"))
