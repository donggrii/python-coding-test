# 순차 탐색(Sequential Search) : 리스트 안의 특정 데이터를 찾기 위해 앞에서부터 데이터를 "하나씩 차례대로 확인"하는 방법
#                              보통 '정렬되지 않은' 리스트에서 데이터를 찾아야 할 때 사용
#                              특정 값을 가지는 원소의 개수를 세는 count() 메서드를 이용할 때도 내부에서 순차 탐색이 수행됨
# 최악의 경우 시간 복잡도(= O(N)) : 데이터의 개수가 N개일 때, 최대 N번의 비교 연산이 필요하기 때문

def sequential_search(n, target, array):
    for i in range(n):             # 각 원소를 하나씩 확인하며
        if array[i] == target:     # 현재의 원소가 찾고자 하는 원소와 동일한 경우
            return i + 1           # 현재의 위치 반환 (index는 0부터 시작하므로 1 더해줌)
        
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])    # 원소의 개수
target = input_data[1]    # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))   # 순차 탐색 수행 결과 출력

# < 예시 >
# 생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.
# >>> 5 Dongbin
# 앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.
# >>> Haneul Jonggu Dongbin Taeil Sangwook
# >>> 3