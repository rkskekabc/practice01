# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
import sys

number = input('숫자를 입력하세요: ')

if not number.isdecimal():
    print('숫자가 아닙니다.')
    sys.exit(0)
else:
    number = int(number)
    my_sum = 0
    for i in range(0, number + 1):
        if number % 2 == i % 2:
            my_sum += i

print('결과값 :', my_sum)