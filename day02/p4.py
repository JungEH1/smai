
if __name__ == '__main__':
    # set 중복안됨
    print("--------set--------")
    t1 = {1,2,3,4,5}
    print(type(t1))
    print(t1)
    t1.add(6)
    t1.add(5)
    print(t1)

    # tuple 수정불가
    print("--------Tuple--------")
    t2 = (1,2,3,4,5)
    print(type(t2))
    print(t2)

    # 딕셔너리 key, value
    print("--------딕셔너리--------")
    d1 = {"a":1, "b":2,"c":3}
    print(type(d1))
    print(d1)
    print(d1["a"])

    d2 = {"name":"가다인","age":24,"major":"nursing"}
    print(d2["name"])
    print(d2["age"])

    # 응용
    sts = [
        {"name": "가다인", "age": 24, "major": "간호"},
        {"name": "정태원", "age": 24, "major": "전자공"},
        {"name": "김송희", "age": 22, "major": "전자공"},
        {"name": "정수현", "age": 23, "major": "전자공"},
    ]

    #전체 학생들의 나이의 합과 평균을 출력 하시오
    sum = 0
    for i in sts:
        sum += i["age"]
    print(f"나이의 합:{sum} 평균:{sum/len(sts)}")

    # 전자공학과 학생들의 나이의 합과 평균을 출력 하시오
    sum = 0
    count =0
    for i in sts:
        if i["major"]=="전자공":
            sum += i["age"]
            count += 1
    print(f'전자공학과 학생들의 나이의 합: {sum} 평균: {sum / count}')

