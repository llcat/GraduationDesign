'''
    实现一个简单的k-means算法，对二维平面上的点（x，y)进行聚类
    为后续实现复杂场景打个基础
    data source: 30个二维平面上的点（x,y) { 0< x <200,0<y<200},从文件data.txt读取
    target:聚成4类
'''
import random
import math
#from k_means import draw_points_cluster
import draw_points_cluster
class KmeansDemo(object):

    def __init__(self,raw_data):
        self.raw_data = raw_data
        self.stand_data =[]

    def point_cluster(self,cluster_num = 4):
        #将数据规格化
        self._get_stand_data()
        #取得4个随机的初始聚心
        init_points = self._get_init_points(cluster_num)
        #init_points =[{'x': 0.84, 'y': 0.27}, {'x': 0.19, 'y': 0.79}, {'x': 0.49, 'y': 0.105}, {'x': 0.155, 'y': 0.395}]

        next_centroid, result = self.once_cluster(init_points, self.stand_data)
        temp_centroid = next_centroid
        while True:
            next_centroid, result = self.once_cluster(next_centroid, self.stand_data)
            if temp_centroid[0]['x'] == next_centroid[0]['x'] and temp_centroid[0]['y'] == next_centroid[0]['y'] and temp_centroid[1]['x'] == next_centroid[1]['x'] and temp_centroid[1]['y'] == next_centroid[1]['y']and temp_centroid[2]['x'] == next_centroid[2]['x'] and temp_centroid[2]['y'] == next_centroid[2]['y']and temp_centroid[3]['x'] == next_centroid[3]['x'] and temp_centroid[3]['y'] == next_centroid[3]['y']:
                break
            else:
                temp_centroid = next_centroid
                continue

        ss = sorted(result.items(),key=lambda item:item[0])
        draw_points_cluster.ResultShow().draw(ss)


    #每次返回下次聚类需要的聚心和分成的聚堆元素
    def once_cluster(self,centroids,all_points):
        next_centroids = []
        result= {"0":[],"1":[],"2":[],"3":[]}
        for point in all_points:
            diss = []
            for centroid in centroids:
                distance = math.sqrt(pow(centroid['x']-point['x'],2)+pow(centroid['y']-point['y'],2))
                diss.append(distance)
            min = diss[0]
            for dis in diss:
                if dis < min:
                    min = dis
            index = diss.index(min)
            if index == 0:
                result['0'].append(point)
            elif index == 1:
                result['1'].append(point)
            elif index == 2:
                result['2'].append(point)
            elif index == 3:
                result['3'].append(point)
            else:
                pass

        sorted_result = sorted(result.items(),key = lambda item:item[0])
        for res in sorted_result:
            if len(res[1]) != 0:
                sum_x = 0
                sum_y = 0
                for point in res[1]:
                    sum_x += point['x']
                    sum_y += point['y']
                new_pos_x = sum_x/len(res[1])
                new_pos_y = sum_y/len(res[1])
                next_centroids.append({'x':new_pos_x,'y':new_pos_y})
            else:
                next_centroids.append(centroids[int(res[0])])

        return next_centroids,result






    def _get_init_points(self,cluster_num):
        init_points =[]
        for x in range(cluster_num):
            point = self.stand_data[random.randint(0,len(self.stand_data)-1)]
            init_points.append(point)
        return init_points

    def _stand(self,pos):
        return float(pos)/200

    def _get_stand_data(self):
        for data in self.raw_data:
            pos_x,pos_y = map(self._stand,data.split(","))
            self.stand_data.append({"x":pos_x,"y":pos_y})



raw_data = open("data.txt","r").readlines()
k_mean = KmeansDemo(raw_data)
k_mean.point_cluster(4)


