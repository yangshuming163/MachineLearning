def load_data():
    with open('shuju.txt','r',encoding='GB18030') as file:
        data = file.read()
        print(data)
    return data

data=load_data()
newdata=data.split('\x1d\n')
print(newdata[0])