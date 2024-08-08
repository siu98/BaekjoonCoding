def solution(arr):
    
    num = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            num.append(arr[i])
    return num
        