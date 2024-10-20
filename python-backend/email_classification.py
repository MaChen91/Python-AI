import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import jieba.analyse
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
# from sklearn.naive_bayes import MultinomialNB
import nltk 
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')


# dir_path = 'C:\XDUAN3\Python\Porjects\Email_classification'
# file_path = dir_path + '\财务中台公邮清单.xlsx'
dir_path = './'
file_path = '.\财务中台公邮清单.xlsx'
df = pd.read_excel(file_path,dtype="str",usecols=['模块','邮件标题','邮件内容'])
sid=SentimentIntensityAnalyzer()
df.fillna('', inplace=True)
df['邮件标题']=df['邮件标题'].str.lower().apply(lambda x:x.replace('fw:','').replace('re:','').replace('回复:',''))
df['sentiment']=df['邮件内容'].apply(lambda x:sid.polarity_scores(x)['compound'])
df['邮件内容']=df['邮件内容'].str.lower().apply(lambda x:x.replace('\n','').replace(' ',''))
# 示例邮件数据

segments=(df['邮件标题']+df['邮件内容']).apply(lambda x:' '.join(jieba.analyse.extract_tags(x,topK=20)))
print(segments)
# 示例邮件类别
categories = df['模块']

# 定义X
# X=df['邮件标题']+segments
# print(X)
print(df['sentiment'])
# class_weight_dict = {0: 2, 1: 1}
# 使用TfidfVectorizer提取邮件文本特征并用LogisticRegression进行分类
vectorizer = TfidfVectorizer()
model = make_pipeline(vectorizer, LogisticRegression())

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    segments, categories, test_size=0.3,random_state=0
)
# 训练模型
model.fit(X_train, y_train)

# 进行预测
y_pred = model.predict(X_test)
print("y_pred:",y_pred)

# 评估模型准确度
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# 保存模型到 model.joblib 文件
joblib.dump(model, dir_path+"\model.joblib",compress=1)

# 加载模型文件，生成模型对象
new_model = joblib.load(dir_path+"\model.joblib")
text='RE: cannot reject thee authorized project code request'
jieba_text=','.join(jieba.analyse.extract_tags(text,topK=20))
X_test1=[jieba_text]
print(jieba_text)
print(new_model.predict(X_test1))

