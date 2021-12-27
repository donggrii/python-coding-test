# 월간 코드 챌린지 시즌2 - 음양 더하기

# 내 풀이
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# 다른 풀이
def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))

# Test Case 1.
# absolutes : [4,7,12]
# signs : [true,false,true]
# result : 9

# Test Case 2.
# absolutes : [1,2,3]
# signs : [false,false,true]
# result : 0