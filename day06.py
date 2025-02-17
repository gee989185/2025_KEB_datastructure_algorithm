# O(n) 선형시간
def total(n):
    result = 0
    for i in range(n+1):
        result += i
    return result
n = int(input())
print(total(n))


