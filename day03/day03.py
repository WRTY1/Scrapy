import requests,re,jieba,wordcloud
head = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
       }
req = requests.get("https://cuiqingcai.com/927.html",headers = head)
a_list = "".join(re.findall(r'[\u4e00-\u9fa5]', req.text))
mylist  =" ".join(jieba.lcut(a_list))
w = wordcloud.WordCloud(
    background_color="white",
    width=1920,
    height=1080,
    min_font_size=5,                 
    max_font_size=200,
    font_path="E:\\python\\信息基础认知与实践\\day03\\simiti.ttf"
)  # 把词云当做一个对象
w.generate(mylist)
w.to_file("pywordcloud2.png")