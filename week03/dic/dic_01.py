#딕셔너리

#3. - 학생들의 과목별 점수를 저장한 딕셔너리:
students = {
    "철수": {"국어": 90, "영어": 85},
    "영희": {"국어": 95, "영어": 100},
    "민수": {"국어": 70, "영어": 80}
}
print(students["영희"]["영어"]) #   - "영희"의 영어 점수를 출력하세요.
#   - 모든 학생의 국어 평균 점수를 구하세요.
total = 0
for gu in students.values():
    total += gu["국어"]

avg = total / len(students)
print(avg)

#2. 가격이 1000원 이상인 물품만 출력하세요 / 가장 비싼 물품의 이름과 가격을 출력하세요.
prices = {"펜": 1200, "노트": 2500, "지우개": 800}
# 1000원 이상인 물품 출력
for item, price in prices.items():
    if price >= 1000:
        print(item, price)
# 가장 비싼 물품 찾기
max_item = max(prices, key=prices.get)
print("가장 비싼 물품:", max_item, prices[max_item])

#1. 학생들 점수를 딕셔너리에 저장
# 새로운 학생 "지훈"을 추가하고 점수를 95로 설정하세요.
scores = {"철수": 85, "영희": 92, "민수": 78}

print(scores["영희"])# "영희"의 점수를 출력하세요.
scores["민수"] = 80 # "민수"의 점수를 80으로 수정하세요.
print(scores["민수"])
scores["지훈"] = 95 # 새로운 학생 "지훈"을 추가하고 점수를 95로 설정하세요.
print(scores)

