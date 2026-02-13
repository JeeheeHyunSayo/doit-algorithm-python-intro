# 1부터 n 까지의 정수 합 구하기
import sys
input = sys.stdin.readline
print('1부터 n까지의 정수 합을 구합니다.')
print('n값을 입력하세요: ', end='')
n = int(input())

sum = 0
i = 1

# while 문 버전
while i <= n:
    sum += i
    i += 1 # 합계를 더하고 다음 루프를 위해 i 를 1씩 증가해야함. (순서 착각)

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

# for 문 버전
sum1 = 0
for i in range(1, n+1): # in range(1, n+1) ####
    sum1+= i
print(f'1부터 {n}까지 정수의 합은 {sum1}입니다.')

# 가우스 덧셈 : n * (n+1) / 2
sum2 = 0
sum2 = n * (n+1) / 2
print(sum2)