# 정렬 - K번째수

# 내 풀이
def solution(array, commands):
    answer = []
    for x in commands:
        i, j, k = x
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# 다른 풀이
# 반복문 사용 없이 lambda 익명함수와 map 활용
def solution(array, commands):
    return list(map(lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# Test Case.
# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# return = [5, 6, 3]