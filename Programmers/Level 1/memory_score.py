# 연습문제 - 추억 점수


# 내 풀이 : dictionary와 get(key[, default])를 이용
def solution(name, yearning, photo):
    name_score = {n: yearning[i] for i, n in enumerate(name)}
    result = []

    for lst in photo:
        score = sum([name_score.get(x, 0) for x in lst])
        result.append(score)

    return result


# Test Case 1.
# name : ["may", "kein", "kain", "radi"]
# yearning : [5, 10, 1, 3]
# photo : [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

# result : [19, 15, 6]

# Test Case 2.
# name : ["kali", "mari", "don"]
# yearning : [11, 1, 55]
# photo : [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]

# result : [67, 0, 55]

# Test Case 3.
# name : ["may", "kein", "kain", "radi"]
# yearning : [5, 10, 1, 3]
# photo : [["may"],["kein", "deny", "may"], ["kon", "coni"]]

# result : [5, 15, 0]
