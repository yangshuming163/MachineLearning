import  re
def load_data():
    with open("1.txt",'r',encoding='GB18030') as file:
        data = file.read()
        #print(data)
    return data

def cut(data):
    newdata=data.split('\x1d\n')#split把一个字符串分成多个字符串组成的列表
    #print(newdata)
    for line in range(0,len(newdata)-1):#每一行的数据
        #print(newdata[line])
        newdata[line]=newdata[line].split('\x1e')
        #print(newdata[line])
        for i in range(0,len(newdata[line])):
            newdata[line][i]=newdata[line][i].split('\x1f')
        #print(newdata[line])
    #print(type(newdata))
    return newdata

#把数据中的一些没用数据清除
def clean(newdata):
    data=[]
    #去掉数据中的空行
    for new in newdata:
        if(len(new)>6):
            new=new[2:]
            data.append(new)
        else:
           print(new)
        #print(new)
    newdata=data

    alldata=[]
    for line in newdata:
        while(len(line[1])==2):
            line.pop(1)
        while(len(line[2])==2):
            line.pop(2)
        #print(line)
        data=[]
        for i in line:
            i_len=len(i)
            if(i_len==1):
                #print(i)
                continue
            if (i_len == 2):
                if (i[0] == '  ' and re.match(
                        'ar|ad|[a-z]+ +[a-z]{1,3} +[0-9]+[a-z]+|[a-z]\d|a[\u4E00-\u9FA5]+\d*版|[a-z]有书目|a读者对象|a[\u4E00-\u9FA5]+[，,]*\(\d+[～-]|a封面题名|a有索引|a丛书第|a有目录|a附光盘|a编著?者还有|a\(\d+\)[a-z]\d+|a著者译名|a责任者译名为|a版权页译者题|a版权页题名|a责任者规范汉译姓|[a-z] +[a-z]\d+[a-z]{2-4}',
                        i[1]) != None):
                    continue
                elif (i[0] == '' and re.match('a\d+', i[1]) != None):
                    continue
            if (i_len >= 2):
                # 删除格式为['  ','aCN','??']、['  ','achi','??']、['  ','aeng','??']的元素
                if (re.match('\d?\s+', i[0]) != None and re.match('aCN|achi|aeng', i[1])!=None):
                    continue
            data.append(i)
        alldata.append(data)
    newdata=alldata
    #for h in newdata:
      #print(h)
    return newdata

data=clean(cut(load_data()))
finaldata=[]

lastlist=[]
for line in data:
    book_dict = {'name': '', 'price': '', 'introduction': '', 'autor':''}
    line[0][1]=line[0][1].replace('-','')
    #print(line)
    #查看价格信息
    price=''
    for i in line[0]:
        if(re.match('^dCNY\d{2}.\d{2,3}$',i)!=None):
            price=re.match('^dCNY\d*.\d*$',i).group()
            book_dict['price']=price
    #print(book_dict['price'])

    for name in line[1]:
       if(re.match('^a(.*)',name)!=None):
            thename=re.match('^a(.*)',name).group(1)
            book_dict['name']=thename
       if(re.match('^f(.*)著$|^f(.*)编$',name)!=None):
            theautor=re.match('^f(.*著)$|^f(.*编)$',name).group(1)
            if((re.match('^f(.*)著$|^f(.*)编$',name).group(1))==None):
                theautor = re.match('^f(.*著)$|^f(.*编)$', name).group(2)
            book_dict['autor']=theautor
    #print(book_dict['name'])
    #print(book_dict['autor'])

    introduction_list=[]
    for introduction in line:
        if(len(introduction)==2):
            introduction_list.append(introduction)

    #print(introduction_list)

    newtroduction_list=[]
    for newtroduction in introduction_list:
        if(len(newtroduction)==2):
            newtroduction=newtroduction[1:]
        newtroduction_list.append(newtroduction)
    #print(newtroduction_list)

    book_dict['introduction']=book_dict['name']
    for lastintroduction in newtroduction_list:
        if(re.match('a(.*)',lastintroduction[0])!=None):
            if(len(lastintroduction[0])>len(book_dict['introduction'])):
                book_dict['introduction']=re.match('a(.*)',lastintroduction[0]).group(1)

    #print(book_dict['introduction'])
    lastlist.append(book_dict)
    print(book_dict)




