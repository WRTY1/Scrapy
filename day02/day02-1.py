
posts = [{'id':1, 'title':'测试标题1', 'author':'匿名用户1', 'publish':'2018-01-01','content':'这里是帖子的测试内容1……','replay':[{'publish':'2018-01-06', 'content':'这里是回复内容1……'},{'publish':'2018-01-05', 'content':'这里是回复内容2……'}]},
{'id':2, 'title':'测试标题2', 'author':'匿名用户3', 'publish':'2018-02-11','content':'这里是帖子的测试内容2……','replay':[{'publish':'2018-02-15', 'content':'这里是回复内容3……'},{'publish':'2018-01-12', 'content':'这里是回复内容4……'}]},]
uid = 0
print("论坛帖子\n=========================")
while uid<len(posts):
    print(f"postId:{posts[uid]['id']}\ntitle:{posts[uid]['title']}\nauthor:{posts[uid]['author']}\npublish:{posts[uid]['publish']}")
    print(f"-------------------------\n{posts[uid]['content']}\n")
    reposts = posts[uid]['replay']
    for i in range(len(reposts)):
        repost = posts[uid]['replay'][i]
        print(f"回复<{repost['publish']}>:{repost['content']}") 
    print("\n\n")
    uid += 1