#파일 읽고 쓰기 
import os 
f = open("week03/file/새파일.txt", 'w', encoding='utf-8') # 경로 지정 할때는 큰 따옴표 사용!!
for i in range(1,11):
    data =f"{i}줄입니다\n"
    f.write(data)
f.close()

f = open("week03/file/새파일.txt", 'r', encoding='utf-8') 
line = f.readline()
print(line)
f.close()

f = open("week03/file/새파일.txt","a",encoding='utf-8' )
