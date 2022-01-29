# 문제 : N과 K가 주어질 때, N에서 1을 빼거나 N을 K로 나눠 N이 1이 될 때까지의 최소 횟수 구하기
# 아이디어 : 주어진 N에 대해 최대한 많이 나누기 (문제에서 주어진 K가 2 이상의 자연수이고, 2 이상의 수로 나누는 것이 1을 빼는 것보다 숫자를 훨씬 많이 줄일 수 있기 때문)

##### 내 풀이
n, k = map(int, input().split())
cnt = 0

while True:
    if n == 1:
        break    
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)

##### 단순하게 푸는 답안 예시 (위의 내 풀이와 동일한 접근)
# N의 범위가 10만 이하이므로 이처럼 일일이 1씩 빼도 문제를 해결할 수 있음
# 하지만, N이 100억 이상의 큰 수가 되는 경우를 가정했을 때도 빠르게 동작하려면 N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 풀어야 함 (아래의 답안)
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    n //= k      # K로 나누기
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

##### N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식의 답안 (한번에 1씩 빼는 게 아니라 나누어 떨어지는 수까지 한 번에 빼주기)
n, k = map(int, input().split())      # N, K를 공백으로 구분하여 입력받기
result = 0

while True:
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    
    # K로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)


# Test Case 1.
# 입력 : 17 4
# 출력 : 3

# Test Case 2.
# 입력 : 25 5
# 출력 : 2

# Test Case 3.
# 입력 : 25 3
# 출력 : 6

# Test Case 4.
# 입력 : 127 4
# 출력 : 12