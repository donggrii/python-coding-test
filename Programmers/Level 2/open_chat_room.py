# 2019 KAKAO BLIND RECRUITMENT - 오픈채팅방

# 내 풀이
def solution(record):       
    answer = []
    users = {}
    for i in range(len(record)):
        com = record[i].split()  # (ex)"Enter uid1234 Muzi"
        # Enter
        if com[0] == "Enter":
            answer.append([com[1], "{}님이 들어왔습니다.".format(com[2])])
            users[com[1]] = com[2]
        # Leave
        elif com[0] == "Leave":
            answer.append([com[1], "{}님이 나갔습니다.".format(users[com[1]])])
        # Change
        else:
            users[com[1]] = com[2]
    
    for i in range(len(answer)):
        answer_split = answer[i][1].split('님')
        answer_split[0] = users[answer[i][0]]
        answer[i][1] = '님'.join(answer_split)

    return [result for id, result in answer]

# 다른 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

# Test Case.
# record : ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
# result : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]