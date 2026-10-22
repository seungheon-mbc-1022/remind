# 1. 변수 만들고 데이터 출력
# 변수 만들고 데이터 출력
print("변수 만들고 데이터 출력")
name = "홍길동"      # 문자형 데이터(str)
age = 25            # 수치형 데이터 - 정수형(int)
height = 175.5      # 수치형 데이터 - 실수형(float)
is_student = True   # 논리값(bool)
print(name, age, height, is_student) # 여러개 데이터 출력
print(f"{name}님의 나이는 {age}살 입니다,") # f-string 출력

# 자료형을 확인하는 파이썬의 표준기능(함수) - type()
print(type(name), type(age), type(height), type(is_student))

# 키보드로 사용자 입력 데이터 받기 input()
# user_name = input("이름을 입력하세요 : ").strip() or "학생" 
#     # .strip() : 양쪽 옆에 공백을 지워줌 
#     # or : A or B A 가 참이면 A, A 가 거짓이면 B
# print(f"환영합니다. {user_name}님!")
print()

# 2. 연산자와 문자열 유용한 기능
a,b = 10,3 # 10,3 => 튜플로 저장 => 언패킹 되서 a,b 에 알아서 들어감
print("사칙연산: ", a+b, a-b, a*b, a/b)
print("몫, 나머지, 제곱: ", a//b, a%b, a**b)
print("비교, 논리: ", a>=b, (a>5) and (b>5)) # and 앞 뒤가 모두 참 인경우

# 문자열의 여러 유용한 기능함수들
message= "     Python Review, Python   "
print(message.strip())  # 양쪽 앞뒤의 공백만 지움
print(message)          # 원본은 유지
print(message.strip().lower())  # 소문자로만 표현
print(message.replace("Python", "파이썬", 1)) # 앞글자를 뒷글자로 변경 index 로 확인 -1(default) 모두 변경
print("사과,바나나,오렌지".split(","))  # 기준 글자로 나눠서 list 로 받기
print("Py" in message)  # 내부에 있는가?
print(len(message))     # 글자수

# 3. 제어문(조건, 반복)
# 점수에 따른 학점 산출
score = 82
if score >= 90 :
    grade = "A"
elif score >= 80 :
    grade = "B"
elif score >= 70 :
    grade = "C"
else :
    grade = "F"
print(f"학점 : {grade}")

# 반복문
for n in range(1,6) : # 1~5 까지 반복
    if n == 3:
        break       # break 위의 조건이 만나면 반복문 탈출 continue 위의 조건이 만나면 다시 위로
    print(n)

count=0
while count<3:
    print(count)
    count += 1 # 1을 더해서 넣어

# 4. (중요) 리스트[], 튜플(), 딕셔너리{key:value}, Set{}, 컴프리헨션
# 리스트
fruits=["사과","바나나","사과"] # 순서대로 저장, 수정 가능, 중복데이터 허용
print(fruits)
fruits.append("포도") # 뒤에 추가
print(fruits)
fruits[1] = "오렌지" # 특정 위치에 수정
print(fruits)

# 튜플tuple
point =(10,20) # 요소의 추가, 수정 불가
print(point, point[0], point[1])

# dictionary
student = {"name":"sam", "score":100} # key : value
print(student)
student["score"] = 90
print(student["score"], student.get("nam", "NAN")) 
    # [] 인덱싱 중 Key 값이 없으면 Key Error, 
    # .get("") 키값이 없으면 default 값을 지정할 수 있음

# Set 중복 데이터를 허용하지 않는 타입
unique_fruits = set(fruits) # set 으로 형변환 set()
print(unique_fruits) # 순서는 보장 못함, 중복 허용 안함

# 리스트 컴프리헨션
# 1부터 5의 제곱값을 저장하는 리스트 생성
squars = [n**2 for n in range(1, 6) ] # for 문 앞에 연산을 시킴
print(squars)

# 조건 성적을 뽑아내는 것
passing = [n for n in [65, 90, 73, 82] if n >= 80] # 시험 패스 조건을 통과한 점수만 뽑기
print(passing)
print()

# 5. 함수, lambda
def greet(person, greeting="안녕하세요"):
    return f"{greeting}, {person}님!"

print(greet("영희"))
print(greet("철수", "반가워요"))

def average(numbers):
    return sum(numbers) / len(numbers) # sum, len 내장(표준)함수

print("평균: ", average([80, 95, 75]))

#제곱해주는 기능 함수 --> lambda 함수로
def square(x):
    return x*x

square2=lambda x : x*x

print(square(5))
print(square2(5))

# 내장 함수 중에서 자주 사용
print("정렬: ", sorted([3,1,6,2]))
print("최소값: ", min([3,1,6,2]))
print("최대값: ", max([3,1,6,2]))

# 6. 파일 입출력 기능함수
# 현재 파일이 있는 폴더에 결과 txt 문서를 저장
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent
    # Path(__file__) : 파일의 상대경로
    # .resolve() : 절대경로로 변경
    # .parent : 부모 폴더
file_path = BASE_DIR / "aaa.txt" 
    # 경로는 문자열이지만, Path의 경우 경로로 알고 있기 때문에 경로로 인식해서 '/' 를 이해함
file = open(file_path, "w", encoding="utf-8") # write 모드, 파일이 없으면 만들어 줌
file.write("파이썬 복습\n파일 입출력 예제\n")
file.close()

with open(file_path, "r", encoding="utf-8") as file: # file 작성에 대한 부분은 여기로
    print("파일내용: \n", file.read())
    # with 를 사용하면, close 자동으로 됨

# 예외처리 (예외가 발생해도 다운되지 않도록)
try:
    number = int("80asb") # cast
    print(number+10)
except ValueError as error:
    print("예외발생", error)
finally:    # 예외 여부와 상관없이 무조건 실행
    print("예외 여부와 상관없이 무조건 실행") # 리소스 정리