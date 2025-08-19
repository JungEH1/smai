from calc.calcfnc import plus, minus

if __name__ == '__main__':
    while True:
        cmd = input("명령을 입력하세요(p,m,q)")
        if cmd =='p':
            print("Plus..")
            num1 = int(input("Input Num1 .."))
            num2 = int(input("Input Num2 .."))
            result = plus(num1, num2)
            print(f"결과는 {result}")
        elif cmd =='m':
            print("Minus")
            num1 = int(input("Input Num1 .."))
            num2 = int(input("Input Num2 .."))
            result = minus(num1, num2)
            print(f"결과는 {result}")
        elif cmd =='q':
            print("Bye")
            break