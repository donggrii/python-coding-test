# 연습문제 - 달리기 경주


# 내 풀이
def solution(players, callings):
    dict_ = {p: i for i, p in enumerate(players)}
    dict_inv = dict(enumerate(players))  # {i: p for i, p in enumerate(players)}

    for call in callings:
        idx = dict_[call]  # 앞으로 이동할 선수, 위치값 : call, idx
        call_inv = dict_inv[idx - 1]  # 뒤로 이동할 선수, 위치값 : call_inv, idx - 1

        # update dictionary using swap
        dict_[call_inv], dict_[call] = idx, idx - 1
        dict_inv[idx - 1], dict_inv[idx] = call, call_inv

    result = list(dict_inv.values())

    return result
