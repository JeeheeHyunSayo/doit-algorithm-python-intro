# 코드 개선 해보기
print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for _ in range(n//w):
    print('*' *  w)

if (n % w):
    print('*' * (n % w), end='')