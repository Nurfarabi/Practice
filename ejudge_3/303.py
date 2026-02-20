digit_map = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

reverse_map = {v: k for k, v in digit_map.items()}

s = input().strip()


for op in "+-*":
    if op in s:
        left, right = s.split(op)
        operator = op
        break

def decode(num_str):
    digits = ""
    for i in range(0, len(num_str), 3):
        digits += digit_map[num_str[i:i+3]]
    return int(digits)

def encode(number):
    return "".join(reverse_map[d] for d in str(number))

a = decode(left)
b = decode(right)

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
else:
    result = a * b

print(encode(result))
