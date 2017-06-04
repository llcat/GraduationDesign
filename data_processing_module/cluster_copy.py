"""
    尝试下能不能进行聚类实现
    1. 本身数据提取的特征值不一定是准确的,我们进行聚类的条件是啥?
    2. 是将所有的特征值散布到坐标上去吗?比如每个词条只取排在前三的
    高频词,对所有的高频词在做一次清洗,去除重复的高频词,并将高频词
    按照一定顺序分布在xyz三个坐标轴上,每个坐标轴上保证顺序一致,那么
    我们每个词条可以看作是空间中的一个点,用k-means算法应该是可以给出
    聚类结果的,但是准确率应该很低

    05/11 update new idea
    查看了《机器学习》的聚类算法一章,里面给出了相关的思路
    对于我的数据来言
    lemma_title: 漫步者H260
    freq_words: [('耳套', 4), ('漫步者', 3), ('入耳式', 3), ('磁体', 2), ('耳塞', 2), ('密闭式', 2), ('单元', 2), ('磁能', 2)]
    lemma_title: 华盛顿特区联足球俱乐部
    freq_words: [('冠军', 12), ('足球', 7), ('名字', 4), ('特区', 4), ('季军', 3), ('球队', 3), ('职业', 3), ('俱乐部', 3)]

    对于我的每个样本来说,我们关注的是高频词本身,如耳套,漫步者 ....
    我的样本属性的特征是不连续，离散型的,我们也不能通过属性值直接计算样本距离.
    那么我们应该换一种方式进行两个词条间的相似度测量
    假设两个词条中的高频词有重合的部分，我们认为两个词条是可连通的,
    重合度越高的情况下，我们认为两个样本点近似度越高
    每条连通通道的权重可以根据词频在高频词中占比来计算
    采用基于密度的聚类算法来实现（density-based clustering)

    DBSCAN算法：
    input: 样本集D_lemma_contents = {lemma_content1, lemma_content2, ....}
    　　　　临域参数　（样本连通通强度,MinPts)

    process:
    1. 计算所有样本点的邻域并确定核心对象集
    2. 随机取一个核心样本点,遍历这个核心样本点的领域,初始化密度直达及可达列表
    3. 遍历可达队列,查找这个样本点邻域中其他核心点,并将其他核心点中的密度直达的点加入到可达队列,非核心点加入到簇中

    update 05/13
    已经实现了,但是存在问题如下
    1. 时间复杂度较高, 样本集一旦数目较大,需要较长时间计算
    2. 需要确定一个合适的邻域参数, 连通强度以及核心点的确定直接影响到聚类结果
    情况如下:

"""
#from data_processing_module.segment_doc import DBUtil
from segment_doc import DBUtil
import random
import pymongo
import time


class DBScan(object):
    """
        基于密度的聚类算法实现
    """
    def __init__(self):
        self.db_util = DBUtil()
        self.coll_contents = self.db_util.coll_content
        self.coll_related_infos = self.db_util.db['related_infos']
        self.coll_cluster_result = self.db_util.db['cluster_result']
        self.coll_related_infos.create_index([("lemma_id", pymongo.ASCENDING)], unique=True)

    def init_sample_collection(self, skip=0, limit=0):
        """
        初始化样本点集合
        :return:
        """
        if limit == 0:
            limit = self.coll_contents.count()

        q_results = self.coll_contents.find(skip=skip, limit=limit)
        re = []
        for content in q_results:
            sample = {}
            sample['id'] = content['lemma_id']
            sample['title'] = content['lemma_title']
            sample['freq_words'] = content['freq_words']
            re.append(sample)
        return re

    def get_existed_samples(self, skip=0, limit=0):
        if limit == 0:
            limit = self.coll_related_infos.count()

        q_results = self.coll_related_infos.find(skip=skip, limit=limit)
        re = []
        for content in q_results:
            sample = {}
            sample['id'] = content['lemma_id']
            sample['area'] = content['area']
            re.append(sample)
        return re

    def cal_connect_strength(self, sample1, sample2):
        """
        计算两个样本点的连通强度,也就是计算邻域参数e
        :param sample1:
        :param sample2:
        :return:两个样本点的连通强度和
        """
        strength = 0
        connect_length = 1
        f_w1 = sample1['freq_words']
        f_w2 = sample2['freq_words']
        w1 = []
        w2 = []
        c_freq1 = 0
        c_freq2 = 0

        if len(f_w1) == 0 or len(f_w2) == 0:
            return strength

        for s in f_w1:
            w1.append(s[0])
            c_freq1 += s[1]

        for s in f_w2:
            w2.append(s[0])
            c_freq2 += s[1]

        for i in range(len(f_w1)):
            # 遍历sample1的高频词有多少是与sample2连通的
            # 计算单个连通的强度
            for j in range(len(f_w2)):
                if w1[i] in w2[j]:
                    # 计算在各自样本中的词频占比多少
                    percentage1 = f_w1[i][1] / c_freq1
                    percentage2 = f_w2[j][1] / c_freq2
                    delta_p = abs(percentage1-percentage2)
                    related_degree = self.cal_related_degree(delta_p)
                    strength += connect_length*related_degree
        return strength

    @staticmethod
    def cal_related_degree(x):
        return 1-x

    def get_core_sample(self, samples, minpts):
        """
        获取核心对象集合
        :param samples:
        :param minpts:
        :return:
        """
        re = []
        for sample in samples:
            if len(sample['area']) >= minpts:
                re.append(sample)
        return re

    def all_sample_area(self, samples, strength, minpts):
        """
        １. 计算所有样本点的邻域
        2. 返回样本中所有核心点集合
        :param samples:
        :param strength:
        :param minpts:
        :return:
        """
        print("start calculate all area")
        samples_len = len(samples)
        # print("sample collection size: ", samples_len)
        core_points = []
        all_cost_time = 0
        for i in range(samples_len):
            # print("sample ", i, "start...")
            t1 = time.time()
            area = []
            for j in range(samples_len):
                if i != j:
                    s = self.cal_connect_strength(samples[i], samples[j])
                    if s > strength:
                        area.append((samples[j]['id'], round(s, 3)))
            samples[i]['area'] = area
            if len(area) >= minpts:
                core_points.append(samples[i])
            if i % 1000 == 0:
                print("had calculated ", i, "pts .....")
            t2 = time.time()
            cost_time = (t2-t1)
            all_cost_time += cost_time
            print("cal pt", i, "'s area cost ", round(cost_time, 3), "seconds")
        print("cal all pt's area cost", round((all_cost_time/3600), 3), "hours")
        print("calculate all sample area ...")
        return core_points

    def cluster(self, core_pts, samples, minpts):
        # 初始化聚类簇数及聚类簇
        k = 0
        clusters = {}
        all_cost_time = 0
        while len(core_pts) > 0:
            t1 = time.time()
            clusters[str(k)] = []
            # 随机选取一个核心点样本
            core = core_pts.pop(random.randint(0, len(core_pts)-1))
            # 该核心样本点的密度直达的样本集合
            access_set = set()
            clusters[str(k)].append(core)
            for pt in core['area']:
                access_set.add(pt[0])

            # 从样本集合中去除本次循环的核心
            samples.remove(core)
            # 本轮密度可达的核心点集合
            reachable_core = {}
            reachable_core[core['id']] = core['area']
            while len(access_set) > 0:
                # print("第二层循环中", len(samples))
                # 遍历密度直达的集合,加入到聚类结果中
                pt_id = access_set.pop()
                pt = self.find_pt(samples, pt_id)

                if pt is not None:
                    # 新增一个判断条件
                    # 假设一个样本点跟多个核心点都有关联,不应该将其随便
                    # 从样本集合中去除添加进簇，应该考虑这个点跟那个核心点的连通强度是最高的

                    # 后续加入的点不一定是密度直达的点，不能这样算强度
                    strength_this = 0
                    for a in core['area']:
                        if pt_id == a[0]:
                            strength_this = a[1]
                            # print("pt direct in this core", strength_this)
                            break

                    if strength_this == 0:
                        # 不是直达的那么就是密度可达的,就算本轮还暂时不在已访问的密度可达核心队列中也没关系，后续遍历到这个与他连通最大的核心点时还是会将该点归簇
                        for key, v in reachable_core.items():
                            for vi in v:
                                if pt_id == vi[0] and vi[1] >= strength_this:
                                    strength_this = vi[1]
                                    # print("in reachable core")

                    strength_max = 0
                    for c in core_pts:
                        # 如果这个可达点是核心点，这里会造成问题是他与自身连通强度最大，所以需要加一个判断条件
                        if c['id'] != pt_id:
                            # core_pts中肯定已经除去了他的直达核心点
                            # 需要考虑的仅有他的可达核心点会不会造成干扰
                            s = self.get_strength(c, pt_id)

                        if s > strength_max:
                            strength_max = s

                    if strength_this > strength_max:
                        samples.remove(pt)
                        clusters[str(k)].append(pt)
                        # print("pt", pt['id'], " area len", len(pt['area']))
                        if len(pt['area']) >= minpts:
                            # 如果pt是个核心点,从核心点集合中移除该点并遍历pt的邻域,更新密度可达集合
                            # print(pt['id'], "is a core")
                            reachable_core[pt['id']] = pt['area']
                            core_pts.remove(pt)
                            for pt in pt['area']:
                                access_set.add(pt[0])
                    else:
                        # print(pt['id'], "has another strength core")
                        pass
                else:
                    # print("the pt id is", pt_id, " had collected in cluster")
                    pass

            t2 = time.time()
            cost_time = t2-t1
            all_cost_time += cost_time
            # if len(clusters[str(k)]) == 1:
            #     pt_no_cluster = clusters[str(k)].pop()
            #     samples.append(pt_no_cluster)
            #     k += 0
            # else:
            print("生成第", k, "簇", "剩余样本数：", len(samples), "消耗时间：", round(cost_time, 3), "second")
            # 更新簇标记
            k += 1
        # 返回聚类结果
        print("samples left length", len(samples), "all cost time:", round((all_cost_time/3600), 3), "hours")
        return clusters

    def find_pt(self, samples, pt_id):
        # print("in find pt_id", pt_id, type(pt_id), len(samples))
        for sample in samples:
            if sample['id'] == pt_id:
                return sample
        return None

    def get_strength(self, core, pt_id):
        """
        求取与核心点的连通强度
        :param core:
        :param pt_id:
        :return:
        """
        strength = 0
        for area in core['area']:
            if area[0] == pt_id:
                strength = area[1]
        return strength

    def save_area(self, samples):
        for sample in samples:
            data = {}
            data['lemma_id'] = sample['id']
            data['area'] = sample['area']
            try:
                self.coll_related_infos.insert_one(data)
            except Exception as e:
                print(e.args)

    def save_result(self, results):
        for i in range(len(results)):
            label = i
            cluster = c_result.get(str(label))
            c_data = []
            for item in cluster:
                try:
                    c_data.append(item['id'])
                    self.coll_related_infos.update_one({'lemma_id': item['id']}, {'$set': {'cluster_label': label}})
                except Exception as e:
                    print(e.args)
            try:
                self.coll_cluster_result.insert_one({'label': label, 'clusters': c_data})
            except Exception as e:
                print(e.args)


if __name__ == "__main__":
    dbscan = DBScan()
    area_strength = 3
    min_access = 5
    # r = dbscan.init_sample_collection(5, 2000)

    # cores = dbscan.all_sample_area(r, area_strength, min_access)
    # dbscan.save_area(r)
    r = dbscan.get_existed_samples(0,2000)
    cores = dbscan.get_core_sample(r, min_access)

    print("核心对象数目:", len(cores))

    c_result = dbscan.cluster(cores, r, min_access)
    # dbscan.save_result(c_result)
    print("聚类数目: ", len(c_result))
    length = 0
    count_one = 0
    for i in range(len(c_result)):
        print("类簇 - ", i)
        c = c_result.get(str(i))
        if len(c) ==1:
            count_one +=1
        for item in c:
            length += 1
            print(item['id'], item['area'])

    print("已经聚类的样本数目:", length, "单簇只有一个元素数目：", count_one)

    # for c in cores:
    #     print(c['title'], c['area'])

