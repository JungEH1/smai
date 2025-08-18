
if __name__ == '__main__':
    num1 = int(input("num1을 입력 하세요"))
    print(num1)
    num2 = int(input("num2을 입력 하세요"))
    print(num2)
    num3 = int(input("num3을 입력 하세요"))
    print(num3)


    result = 0
    max = 0
    min = 0
    if num1 > num2:
        max = num1
        min = num2
    else:
        min = num1
        max = num2
    if min > num3:
        min =num3
    if max < num3:
        max = num3

    print(f'최댓값: {max}, 최솟값: {min}')




