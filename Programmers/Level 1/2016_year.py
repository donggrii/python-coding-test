# 연습문제 - 2016년

# 내 풀이
def solution(a, b):
    weeks = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return weeks[(sum(days[: a - 1]) + b + 4) % 7]


# 다른 풀이
# datetime 함수 활용 (월요일부터 시작)
import datetime


def solution(a, b):
    t = "MON TUE WED THU FRI SAT SUN".split()
    return t[datetime.datetime(2016, a, b).weekday()]


# Test Case.
# a = 5
# b = 24
# result = "TUE"
