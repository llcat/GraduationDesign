# GraduationDesign
#### 课题
关于网页内容的聚类算法实现

**进度- week1(03/19-03/26)**

-  重构数据采集模块,之前的爬虫速度较慢,不能很好的完成工作,重构后大体结构如下:  
![baike_spider_frame](./img/baike_spider_frame.png)
- 实验k-means聚类算法,将一百个二维平面上的点聚为4类,实验结果如下:  
![k-means_result_show](./img/k-means_result.png)

    说明:这个星期的进度比较慢,重构了一下数据采集模块,还有部分编码工作没完成.   
    下个星期的目标是继续完成上星期未完成的编码工作,在做两个聚类算法的实验,以及引入分词,争取能在这个星期结束时完成所有的数据准备工作.

**进度- week2(03/27-04/02)** 

-  无进度,未更新其他东西,看了下层次聚类的两个算法,未实践

**进度- week3(04/03 - 04/09)**

- 本周准备对数据进行清洗,正式引入分词包提取高频词,准备采用开源分词包 --- [结巴分词](https://github.com/fxsjy/jieba)进行处理.
- 已完成高频词的提取工作, 提取的方法是只提取高频词中的名词, 并统计词频,写入数据库留待备用

> 结巴分词相关资料
HMM(隐马尔可夫模型)及viterbi算法:
[HMM及viterbi](http://www.cnblogs.com/skyme/p/4651331.html)


     **Question:**
     上周在考虑后续聚类实现时想到一个问题,我们采集的数据可  
     能分为n个类别,如果我们采用求距离的方式进行聚类,那我们  
     每个数据需要认为是一个n维的数据吗?即使他在某些维度上  
     的值为0

**进度-week4(04/10 - 04/16)**

- 本周需要增加spider模块解析的内容,情况如下:
    - 增加词条点赞,分享次数
    - 增加词条统计信息(历史浏览次数,历史编辑次数,最近编辑时间,词条创建者,全部历史记录
    - 增加百度百科词条自己的人工分类,作为后续聚类实现的对比结果
    - 鉴于先前的将词条设计为唯一索引不太合理,分析词条页面发现每个词条都有一个lemma-id,而且词条的相关信息也是后续基于lemma-id通过异步请求取得的,如分享,点赞次数,词条浏览次数等
    - 先前已经存在的collection中,需要增加新的字段lemma_id,替换该字段为唯一主键去重
  
  重构document结构如下
```
\\ new_urls
{
	"_id" :
	\\唯一索引
	"lemma_id" :
	"url" : 
}

\\ old_urls
{	
	"_id" :
	\\唯一索引
	"lemma_id" :
	"url" : 
}
\\ lemma_contents
{	
	"_id" : 
	\\唯一索引
	"lemma_id" :
	"lemma_title" :
	"lemma_url" : 
	"lemmaid_enc" :
	"lemma_paras" :
	"lemma_freq_words" :
	"tags" : ['tag_a','tag_b']
	"like_count":
	"share_count":
	"history_view_count":
	"history_edit_count":	
	"last_update_time" :
	"lemma_creator":
}
\\这个作为后续追加的内容，如果时间比较充分就加上去
\\lemma_edit_histories
{
	"_id" : 
	"lemma_id":
	"histories":[
				( contibutor_name, update_time, reason),
				...
				...
				] 
}
```
    
**暂定目标**

- 编写爬虫收集网页数据
- 完成几个简单的聚类算法实现
    - k-means (HCM)
    - FCM (Fuzz Cluster)
    - 层次聚类
- 引入分词模块,完成采集的内容中高频词汇的提取工作
 
     
