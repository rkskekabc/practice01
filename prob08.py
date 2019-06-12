# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.


def reverse(s):
    s = str(s)
    reverse_string = []
    for i in range(1, len(s) + 1):
        reverse_string.append(s[-i])
    return ''.join(reverse_string)


string = input('입력 > ')
print('결과 >', reverse(string))