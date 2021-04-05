def plus(a,b):          #함수 정의(define)
    return a+b
a = plus(1349127598,1241510)
print(a)

def plus_many(*args):   # argument를 몇개가오든 노상관
    a= 0    
    for i in args:
        a += i
    return a
print(plus_many(1,2,321,41,25,145,134,416,4136,1265,16,1346,146,))
#함수의 리턴값은 하나이다. 여러개면 튜플로 묶임
def say_hello(name, old, man=True):     # 세번째 변수는 True가 디폴트값
    print("나의 이름은  %s입니다."%name)
    print("내 나이는 %d살입니다."%old)
    if man:
        print("나 남자")
    else:
        print("나 여자")
say_hello("a",3,False) 
say_hello("b",2)

def sum(a,b):
    return a+b
a = lambda a,b: a+b     #한줄 함수 정의 (리스트에듀ㅗ 넣을 수있음)
print(a(1,2))          
print(sum(1,2))
for i in range(1,10):
    print(i, end='  ') # 가로 줄에 다 쓸거임
print('') #띄어쓰기

nfile = open("새파일.txt",'w',encoding="utf-8")     #파일 만들기open(이름,용도,인코딩)
for i in range(1,10):   
    data = "%d번째 줄입니다.\n"%i
    nfile.write(data)

nfile = open("새파일.txt","r", encoding='utf-8')    #nfile
line = nfile.readline()
print(line)
nfile.close()       #꼭 닫기


nfile = open("새파일.txt",'r',encoding='utf-8')
while True:             # 반복readline
    line = nfile.readline()
    if not line:
        break
    print(line,end='')
nfile.close()

nfile = open("새파일.txt",'r',encoding='utf-8')
data = nfile.read()     #read는 통째로 다읽음
print(data)
nfile.close()

nfile = open("새파일.txt",'a',encoding='utf-8')
for i in range(11,20):
    data = "%d번째 줄입니다.\n"%i
    nfile.write(data)
nfile.close()

with open("새파일.txt","w",encoding='utf-8') as nfile:
    nfile.write("ㅁㄴ이러ㅐ헵")