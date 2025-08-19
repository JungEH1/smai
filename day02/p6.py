import pickle

from day01.p2 import result

if __name__ == '__main__':
    sts = [
        {"name": "가다인", "age": 24, "major": "간호"},
        {"name": "정태원", "age": 24, "major": "전자공"},
        {"name": "김송희", "age": 22, "major": "전자공"},
        {"name": "정수현", "age": 23, "major": "전자공"},
    ]

    pickle.dump(sts,open('data/sts.pkl','wb'))
    result = pickle.load(open('data/sts.pkl','rb'))
    print(type(result))
    print(result)