# 연습문제 - 시저 암호

# 내 풀이
# ord('A') = 65, ord('Z') = 90
# ord('a') = 97, ord('z') = 122
# ord(' ') = 32
def solution(s, n):
    lst = []
    for char in list(s):
        if char.isupper():
            lst.append(ord(char) + n - 26 if ord(char) + n > 90 else ord(char) + n)
        elif char.islower():
            lst.append(ord(char) + n - 26 if ord(char) + n > 122 else ord(char) + n)
        else:
            lst.append(ord(char))
    return "".join([chr(r) for r in lst])


# 다른 풀이
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))
    return "".join(s)


# Test Case 1.
# s = "AB"
# n = 1
# result : "BC"

# Test Case 2.
# s = "z"
# n = 1
# result : "a"

# Test Case 3.
# s = "a B z"
# n = 4
# result : "e F d"
