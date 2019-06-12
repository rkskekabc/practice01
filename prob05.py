# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_num = 0
my_sum = 0

for i in my_list:
    if i % 3 == 0:
        my_num += 1
        my_sum += i

print('주어진 리스트에서 3의 배수의 개수=>', my_num)
print('주어진 리스트에서 3의 배수의 합=>', my_sum)
