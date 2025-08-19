
if __name__ == '__main__':
# File Write & Read
    with open("data/mytext.txt","w",encoding="utf-8")as f:
        print("파일 라인 1", file=f)
        f.write("파일 Write")
        f.close()


    with open("data/mytext.txt","r",encoding="utf-8")as f:
        data=f.readline()
        print(data)
        f.close()


    with open("data/mytext.txt","r",encoding="utf-8")as f:
        data=f.readlines()
        for d in data:
            print(d)
        f.close()