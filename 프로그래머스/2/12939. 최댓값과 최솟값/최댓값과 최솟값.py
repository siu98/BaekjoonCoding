def solution(s):
    # s = "1 2 3 4"
    num_list = list(map(int, s.split()))
    # num_list = [1, 2, 3, 4]
    answer = []
    answer.append(min(num_list))
    answer.append(max(num_list))
    s = " ".join(map(str, answer))
    return s