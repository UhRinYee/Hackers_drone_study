money = "ㅁ" 
if money:               #money 변수값이 True면 if구문실행, False면 else 구문 
    print("돈이 있다")   #파이썬은 들여쓰기 중요함   
else:
    print("돈이 없다")  
print(3>2)      # True로 인식함

# and(&) : 둘다 True 일때만 True
# or : 둘다 False 이여야 False
# not은 뒤의 bool값을 반대로

if True:
    pass # 암것도하지마

if True:        # ==a = 3 if True else 5   
    a = 3       # ==a = 3 if True else 5
else:           # ==a = 3 if True else 5
    a= 5        # ==a = 3 if True else 5

tree_hit = 0
while tree_hit < 10:       #tree_hit이 10보다 작을 때까지 반복해라
    tree_hit +=1            
    print("나무를 {0}번 찍었습니다.".format(tree_hit))
    if tree_hit ==10:       
        print("나무 넘어갑니당")
                        #continue 는 밑에 꺼 다무시

test_list = ["one","two","thr"]
for test in test_list:      #test_list 안의 값들 하나 하나가 test가 되고 실행
    print(test)    
(a,b) = (1,2)


grades = [90,80,70,60]
names = ["정석","성훈","호떡","카메라"]



for i in range(4):  # 4번 반복
    name = names[i] # 순차적으로 name과 grade가 names와 grades의 값을 받음
    grade = grades[i]
    if grade >=80:
        print("{0}학생 {1}점으로 합격".format(name,grade))
    else:
        print("{0}학생 {1}점으로 불합격".format(name,grade))

for i in range(2,10):   #이중for문
    for j in range(1,10):   #2~9 *1~9 (구구단)
        print(i*j,end="  ") 
    print('')   