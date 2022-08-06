# 연습문제 - 핸드폰 번호 가리기

# 내 풀이
def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]


# Test Case 1.
# phone_number = "01033334444"
# return : "*******4444"

# Test Case 2.
# phone_number = "027778888"
# return : "*****8888"
