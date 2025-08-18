

if __name__ == '__main__':
    num1 = int(input("num1을 입력 하세요"))
    print(num1)
    num2 = int(input("num2을 입력 하세요"))
    print(num2)
    op = input("연산자를 입력 하세요")
    print(op)

    result = 0
    if op =='+':
        result = int(num1) + int(num2)
    elif op =='-':
        result = int(num1) - int(num2)
    elif op =='*':
        result = int(num1) * int(num2)
    elif op == '/':
        result = int(num1) / int(num2)
    print(f"결과 값은 {num1}{op}{num2}=%.2f" %(result))