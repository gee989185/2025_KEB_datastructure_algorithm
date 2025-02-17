# # 8진수 만들기
# def oct(number) -> int:
#     if number // 8 > 8:
#         result +=1
#
#
#         7 > 7
#         10 > 8
#         11 > 9
#         64 > 101
#
#
# # 2진수 만들기
# def bin(number):
#     2 > 10 (2 // 2 = 1)
#     3 > 11
#     4 > 100 ( 4 // 2 = 2)
#     6 > 110
#     8 > 1000 (8 // 2 = 3)
#     10 > 1010 (10 // 2 = )
#
def dec_bin(n):
    if n == 0:
        return ""
    else:
        return dec_bin(n // 2) + str(n % 2)

def dec_oct(n) -> int:
    if n == 0:
        return ""
    else:
        return dec_oct(n // 8) + str(n % 8)  # 8로 나누면 몫

n = int(input())
print(dec_oct(n))

n1 = int(input())
print(dec_bin(n1))