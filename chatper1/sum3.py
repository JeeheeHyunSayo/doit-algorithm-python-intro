# a 부터 b까지 정수의 합을 구하는 과정과 최종값을 출력하는 프로그램
import sys
input = sys.stdin.readline

print('정수 a를 입력하세요: ', end='')
a = int(input())

print('정수 b를 입력하세요: ', end='')
b = int(input())

if a > b:
    a, b = b, a

sum = 0
# a, b 가 너무 커지면 추천하는 방법은 아님
for i in range(a, b+1):
    if i < b:  # i가 b보다 작으면 합을 구하는 과정을 출력
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)