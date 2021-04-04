# 숫자 자료형

# a = 1           # int
# b = 1.23        # float
# c = 4.24e10     # float


# a = 3
# b = 4

# print(a + b)
# print(a - b)
# print(a * b)        # 곱하기
# print(a ** b)       # 제곱
# print(a / b)        # 나누기
# print(a // b)       # 몫
# print(a % b)        # 나머지

# 문자 자료형

# a = "Hello World"     # ", ', """, ''' - 다 같은뜻
#                       # -> 왜 이렇게 쓰냐면 문장안에 작은따옴표, 큰따옴표 모두 들어갈 수 있기때문

# b = "\"Python\""      # 요렇게 따옴표도 가능

#                       # \n : 개행


# print(type(a))

# a = "Python"
# b = " is fun"

# print(a + b)    # 이렇게 문자열을 합칠 수 있다.
# print(a * 100)  # 곱하기를 이용하여 문자열을 여러번 출력이 가능



# a = "Life is too short, You need Python"

# # 문자열 인덱싱
# print(a[0])       # 인덱싱은 0부터 시작하며 -n을 한다면 거꾸로 인덱싱을 한다.

# # 문자열 슬라이싱
# print(a[1:8])     # 두번째 글자부터 8번 인덱스 전까지 출력
# print(a[:8])      # 첫글자부터 8번 인덱스 전까지 출력

# # 위 처럼 시작숫자를 지정하지 않는다면 무조건 1번부터 시작

# print(a[::2])     # 0부터 끝까지 2칸 간격으로 출력

# [이상:미만:간격]

# 포매팅

# number = 10
# day = "three"
# a = "I ate %d apples. so I was sick for %s days." %(number, day)

# %d는 정수, %s는 문자열
# 위와 같은 포매팅을 쓰는이유는 출력할 문장에 변수를 넣고싶을때 사용

# print(a)

# name = "int"
# a = "asdf {} asd".format("안녕") # 이런식으로 포맷도 가능
# b = "asdf {name} asd {age}".format(name="이시영", age="10") # 이런식으로 포맷도 가능
# c = f"나의 이름은 {name}입니다."  # 이것도 가능

# print(c)

# 소숫점 조절

# a = "%.4f" % 3.141592     #%.nf   : 소숫점 n번째 자리까지 선택
# print(a)

# 함수

# count : 문자열 안에 인자의 갯수를 셈
# find : 문자열 안에 인자의 인덱스를 셈   없다면 -1 리턴
# index : 위와 같지만 없다면 에러
# join : 문자열 삽입
# 등등...

# 리스트
# A = [“1”,”2”,”3”,”4”]
# 리스트 안에 리스트도 넣을 수 있음
# Append – 맨 뒤의 추가
# Insert – 사용자 지정 숫자에 추가
# Remove – 사용자 지정값을 삭제
# Count – 사용자 지정값이 리스트 안에 몇 개이었는지 세어줌
# Extend – 값을 한 개씩 넣어줌
# -&gt;pink
# =p,I,n,k

# 튜플

# t1 = (1,2,'a','b')

# 튜플은 변수의 값을 바꿀 수 없다. 이외에는 리스트와 모두 같다.

# 딕셔너리
# {key : value}
# a = {1 : "a"}
# a["name"] = "익명"

# print(a)

# values : 딕셔너리의 value를 모두 가져옴
# keys : 딕셔너리의 key를 모두 가져옴
# item : 모든 쌍을 가져옴

# 집합 자료형
# s1 = set([1,2,3])
# s1 = {1,2,3}

# print(s1)

# l = [1,2,2,3,3]
# new_list = list(set(l))

# print(new_list)

# s1 = set("Hello")
# print(s1)

# 교집합
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# print(s1 & s2)
# print(s1.intersection(s2))

# 합집합
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])

# print(s1 | s2)
# print(s1.union(s2))

# 차집합
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])

# print(s1 - s2)
# print(s1.difference(s2))

# bool 자료형

# a = True
# b = False

#변수

# a = [1,2,3]
# b = a
# a[1] = 4
# print(id(a))
# print(id(b))

# print(a is b)       # a와 b는 같은것을 가리키게 된다.

# a = [1,2,3]
# b = a[:]            # 이렇게하면 슬라이싱을 하여 새로운것이 들어감
# a[1] = 4
# print(a)
# print(b)

# from copy import copy   # copy하는 라이브러리 선언
# a = [1,2,3]
# b = copy(a)             # a를 copy하여 b에 넣음
# a[1] = 4
# print(a)
# print(b)

# 파이썬에서만 가능한것
# a = 3
# b = 5
# a,b = b,a

#원래라면 변수 3개를 이용하여 바꿔야하지만 2개만 바꿔서 사용이 가능하다

