# 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
import sys

number = input('수를 입력하세요: ')
if not number.isdecimal():
    print('정수가 아닙니다.')
    sys.exit(0)
else:
    number = int(number)
    if number % 3 != 0:
        print('3의 배수가 아닙니다.')
    else:
        print('3의 배수입니다.')


# if 1 + 2 == 3:
#     sys.exit(0)
