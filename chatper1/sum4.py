print('a부터 b까지의 정수의 합을 구합니다. ')
a = int(input('정수 a의 값을 구하시오.'))
b = int(input('정수 b의 값을 구하시오.'))

# 오름차 순 정렬
if a > b:
    a, b = b, a

sum = 0

# 마지막 수 직전까지 +
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

# 마지막 수 더하기
print(f'{b} = ', end='')
sum+= b

print(sum)

# sum3.py 보다 판단 횟수 N -> 0 번으로 바뀌고, 반복횟수도 1번 감소 !
