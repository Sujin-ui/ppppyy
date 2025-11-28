#함수 

#1. 두수를 입력받아 합을 구하시오
number_1 = int(input("첫번째 숫자를 입력하세요: "))
number_2 = int(input("두번째 숫자를 입력하세요: "))
def add_number (number_1=0, number_2=0):
    return number_1 + number_2
print(add_number(number_1, number_2))

#2. 짝수 판별 정수를 입력 받아서 짝수 Tr 홀수면 Fla 
number_3 = int(input("숫자를 입력하세요: "))
def bol_number (number_3):
    if number_3 % 2 == 0 :
        return "짝수입니다"
    else:
        return "홀수입니다"
    
print(bol_number(number_3))

#3. 구구단 만들기
number_4 = int(input("구구단 단수를 입력하세요: "))

def gugu (number_4):
    for i in range(1,10):
        print(f"{number_4} * {i} = {number_4 * i}")
gugu(number_4)

#4. 리스트 평균 구하기
numbers = [10, 20, 30, 40, 50]
def number_aver (numbers):
    return sum(numbers)/len(numbers)
print(number_aver(numbers))

#5. 최대값 찾기 함수
scores_1 = [88, 92, 79, 93, 85]
def number_ma (scores_1):
    return max(scores_1)
print(number_ma(scores_1))