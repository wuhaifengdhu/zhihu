### Requirements
1, Install python 2.7+.                   
2, Install libs: zhihu_oauth, redis, pandas, csv          
Example: ```pip install zhihu_oauth```


### Running
```python main.py```



### Crawl Data Format
用户id、    
该用户的回答时间list、      
发表的文章时间list、        
评论的时间list，       
该用户关注的专栏、       
该用户关注的话题、       
问题时间list、        
关注了的人的id list、      
以及关注他的人的id list、         
用户知乎live时间list、        
他的文章的时间的list  ==> 感觉跟发表的文章重复            
他的想法的时间list    ===> 找不到        

新增       
所有的动态时间list      
