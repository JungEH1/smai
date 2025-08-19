# 정상일 때(숫자 입력)도 있고 예외일 때(문자 등)도 있음 ->예외상황
from logging import exception

if __name__ == '__main__':
    try:
        num = int(input("Input Number.?"))
        result = num + 100
        print(f"결과 {result}")
    except:
        print("숫자만 입력 하세요")
