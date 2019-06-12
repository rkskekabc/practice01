# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
import sys

number_list = []
my_sum = 0

for i in range(0, 5):
    number = input('> ')
    if not number.isdecimal():
        print('숫자가 아닙니다.')
        sys.exit(0)
    else:
        number = int(number)
        number_list.append(number)
        my_sum += number

print('평균 : ', my_sum / len(number_list))