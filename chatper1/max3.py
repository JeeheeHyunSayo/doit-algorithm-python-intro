# 세 정수 입력 받아 최대값 구하기
a = int(input('정수 a의 값을 입력하시오.'))
b = int(input('정수 b의 값을 입력하시오.'))
c = int(input('정수 c의 값을 입력하시오.'))

maxNum = a
if b > maxNum: maxNum = b
if c > maxNum: maxNum = c

print(f'최댓값은 {maxNum} 입니다.')