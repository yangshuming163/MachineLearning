import pandas as pd
import jieba
from jieba import analyse
import numpy

#分隔符为\t
news=pd.read_table('val.txt',names=['category','theme','URL','content'],encoding='utf-8')
news=news.dropna()
#print(news.head())
#转换成list格式
#jieba分词需要list类型的数据
content=news.content.values.tolist()

#分词
content_s=[]
for line in content:
    current_segment=jieba.lcut(line)
    if len(current_segment)>1 and current_segment !='\r\n':
        content_s.append(current_segment)
#DataFrame 类型类似于数据库表结构的数据结构，其含有行索引和列索引,
#用包含等长的列表或者是NumPy数组的字典创建DataFrame对象

df_content=pd.DataFrame({'content_S':content_s})
#print(df_content)
stopwords=pd.read_csv('stopwords.txt',index_col=False,sep='\t',quoting=3,names=['stopword'])
#print(stopwords.head())

def clean_stopwords(contents,stopwords):
    content_clean=[]
    all_word=[]
    for line in contents:
        line_clean=[]
        for word in line:
            if word in stopwords:
                continue
            line_clean.append(word)
            all_word.append(word)
        content_clean.append(line_clean)
    return content_clean,all_word

stopwords=stopwords.stopword.values.tolist()
#print(stopwords)
contents=df_content.content_S.values.tolist()
content_clean,all_word=clean_stopwords(contents,stopwords)
#print(content_clean[2000])
#print(''.join(content_clean[2000]))


df_content=pd.DataFrame({'content_s':content_clean})
#print(df_content.head(1))
df_allword=pd.DataFrame({'all_word':all_word})
#print(df_allword.head())

index=3000
#原来的content
print(news['content'][index])
#分词后合并的content
str=''.join(content_clean[index])
print(str)
#基于TF-IDF提取关键字
result=jieba.analyse.extract_tags(str,topK=5 )
print(result)