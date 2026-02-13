# 연속하는 정수의 합 구하기

import sys
input =  sys.stdin.readline

print('a에서 b까지의 정수의 합을 구합니다. ')
print('정수 a의 값을 입력하세요: ', end='')
a = int(input())

print('정수 b의 값을 입력하세요: ', end='')
b = int(input())

## a,b 오름차순 정렬 ##
if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    sum += i

print(f'{a} 부터 {b} 까지의 정수의 합은 {sum} 입니다. ')
