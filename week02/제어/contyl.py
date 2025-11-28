#if문
money = True 
if money:               #if 조건문 :
    print("택시 ㄱ")    #   수행 문장
elif money == false:    #elif 조건문 
    print("버스")       #   수행문장 
else:                   #else :
    print("걸어가")     #    수행문장

#while문 
i = 0 
while i < 10 :
    i = i+1
    print(f"나무를 {i}번 찍습니다" )
    if i == 10 :
        print("나무가 넘어갑니다")
        break

c=0
while True: 
    print("커피 구매가 가능합니다")
    c = c+1
    if c == 3:
        break

#for문 
a = ['a', 'b', 'c' ]
for i in a:
    print(i)

for i in range(1, 10, +2): #reange는 시작값 끝값 증가값 을 지정 할수 있다
    print(i)