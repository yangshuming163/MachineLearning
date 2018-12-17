import re,collections

def yuliao():
    with open('big.txt','r') as file:
        text=file.read()
        #print(text)
        return text

def chuli(text):
    data=re.findall('[a-z]+',text.lower())
    #print(data)
    return data

def train(text):
    model=collections.defaultdict(lambda:1)
    for i in text:
        model[i]+=1
    #print(model)
    return model

#返回可编辑距离为1的单词的集合
def distance1(word):
    length=len(word)
    delete=set(word[0:i]+word[i+1:]for i in range(length))    #删除
    transposition=set([word[0:i]+word[i+1]+word[i]+word[i+2:]for i in range(length-1)])#换位
    alter=set(word[0:i]+chr(c)+word[i+1:] for i in range(length) for c in range(97,123))#修改
    insert=set(word[0:i]+chr(c)+word[i:]for i in range(length+1)for c in range(97,123))#插入
    nset=delete|transposition|alter|insert
    #print(alter)
    return nset

#返回编辑距离为2的单词的集合
def distance2(word):
    nset=set(j for i in distance1(word)for j in distance1(i))
    return nset

#优化 将在编剧距离内的单词 并在语料库中的单词筛选出来
#return set(w for w in words if w in yuliao())
def known(words):
    txt=train(chuli(yuliao()))
    nset=set()
    for i in words:
        if i in txt:
            set1=set([i])
            nset=nset|set1
    return nset

def correct(word):
    candidates = known([word]) or known(distance1(word)) or distance2(word) or [word]
    txt=train(chuli(yuliao()))
    a=max(candidates, key=lambda w: txt[w])
    print(a)

correct('somtheng')
#print(train(chuli(yuliao())))
