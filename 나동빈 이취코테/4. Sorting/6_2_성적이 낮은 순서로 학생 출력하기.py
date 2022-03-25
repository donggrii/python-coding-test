# 문제 : N명의 학생 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하기 (1 <= N <= 100,000)
#      => 시간 제한이 1초이고 학생의 정보가 최대 100,000개까지 입력될 수 있으므로 최악의 경우 O(NlogN)을 보장하는 알고리즘을 이용하거나 O(N)을 보장하는 계수 정렬을 이용해야 함!
# (cf) '풀이 1(기본 정렬 이용)'과 '풀이 2(계수 정렬 이용)'의 수행 시간 차이를 계산해봤을 때, 
#      Test Case 예시와 같이 5개 이하의 데이터가 입력되는 경우 '풀이 1'이 미세하게 더 빠르지만,
#      10개 이상의 데이터만 입력돼도 '풀이 2'의 수행 속도가 월등히 빠른 것을 확인

##### 내 풀이 1
# 아이디어 : 파이썬 기본 정렬 라이브러리와 key parameter를 이용해 성적을 기준으로 정렬
#          (주의) input을 받은 후, 성적 정보는 문자열이 아닌 정수형으로 변환해야 함
n = int(input())
array = []
for i in range(n):
    arr = input().split()
    arr[1] = int(arr[1])
    array.append(arr)

array = sorted(array, key = lambda x:x[1])

for i in range(len(array)):
    print(array[i][0], end = ' ')

##### 내 풀이 2
# 아이디어 : 계수 정렬을 이용한 풀이
# (ex) dictionary = {'이순신' : 5, '홍길동' : 3, '철수' : 5} 일 때,
#      -> count 변수의 형태 : [0, 0, 0, ['홍길동'], 0, ['이순신', '철수'], 0]
n = int(input())
dictionary = {}
for i in range(n):
    input_data = input().split()
    dictionary[input_data[0]] = int(input_data[1])

count = [0] * (max(dictionary.values()) + 1)

for key, value in dictionary.items():
    if type(count[value]) == int:   # 초기화된 값 0일 때
        count[value] = []
        count[value].append(key)
    else:
        count[value].append(key)

for i in range(len(count)):
    if count[i] != 0:
        for student in count[i]:
            print(student, end = ' ')

##### 답안 예시
# 좀 더 복잡한 문제라고 가정했을 때, 입력받은 데이터가 이후에 변환되지 않도록 tuple로 받는 게 좋은 방법
n = int(input())   # N을 입력받기

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장

array = sorted(array, key = lambda student: student[1])  # 키(Key)를 이용하여, 점수를 기준으로 정렬

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end = ' ')


# Test Case.
# < input >
# 2
# 홍길동 95
# 이순신 77

# output : 이순신 홍길동