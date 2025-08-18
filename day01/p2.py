a = 10
b = 10.1567
c = 'a'
d = '"aaa"'
e = True
num1 = "100"
num2 = "200"
result = int(num1) + int(num2)

if __name__ == '__main__':
    print(f"num1은 {num1} num2는 {num2} 결과는 {result}")
    print(f"결과는 {d}")
    print(b)
    print(type(b))
    print(type(a))
    print('결과값: %d이고 %.3f'%(a,b))
    print(f'결과는 {a} {b} {e}입니다.')