# 해시 - 전화번호 목록

# 내 풀이
# phone_book을 정렬하는 게 핵심!
# 정렬하면 바로 오른쪽 문자열이랑만 비교하면 됨. 접두어이면 False로 바로 반환될테고, 아니면 건너 뛴 다음 것도 접두어가 아닐 것이므로
# 즉, 하나의 문자열이 나머지 문자열 "모두"와 비교해서 접두어인지 확인할 필요 X
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True

# 다른 풀이 1
# heap을 이용한 풀이(시간복잡도 NlogN) : sort()를 이용한 정렬과 heapify를 이용한 오름차순 정렬이 동일함(문자열이든 숫자든)
# sort()(시간복잡도 NlogN)로 푼 내 풀이보다 효율성과 속도가 훨씬 빠름..!!
import heapq

def solution(phone_book):
    heapq.heapify(phone_book)
    p = heapq.heappop(phone_book)
    while phone_book:
        if p == phone_book[0][:len(p)]:
            return False
        p = heapq.heappop(phone_book)
    return True

# 다른 풀이 2
# 정렬과 startswith를 이용한 풀이
# zip(phoneBook, phoneBook[1:])하면 하나씩 밀려서 1:1로 매칭됨!
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# Test Case 1.
# phone_book : ["119", "97674223", "1195524421"]
# return : false

# Test Case 2.
# phone_book : ["123","456","789"]
# return : true

# Test Case 3.
# phone_book : ["12","123","1235","567","88"]
# return : false