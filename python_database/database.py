from py2neo import Node, Graph, Relationship, NodeMatcher, RelationshipMatcher
import test1

mach = NodeMatcher(gra)
node1 = mach.match('Person', real_name = '李纪波').first()
node2 = mach.match('Organization', name = '浪潮集团').first()
rel = gra.match([node1, node2], None).first()
#print(node1)
print(rel)

lisor = ['浪潮集团', '浪潮国际', '软件集团', '浪潮信息', '浪潮金融','浪潮优派']
def shortestpath(gra,cur_node, PER):
    shortest_path = gra.run('match (a:Organization{name:"%s"}),(b:Person{real_name:"%s"}),\
                           p = allShortestPaths((a)-[*]-(b)) return p' % (cur_node, PER)).data()
    if len(shortest_path) > 1:
        lis_path = sorted(shortest_path, key=lambda x: len(x['p']))  # sorted path by node number
        #first = lis_path[0]['p'].end_node
        return lis_path[0]
    else:
        # first = shortest_path[0]['p'].end_node
        return shortest_path
if __name__ == "__main__":
    gra = Graph(url = 'http://localhost:7474', user = 'neo4j', password = '6742099')
    pa = shortestpath(gra, "浪潮集团", "张民")
    mid = len(pa['p'])-1 # 知道使用者的ID后，根据开始节点的属性，可以唯一地确定一条路线
    for i in range(0, 3):
        midnode = pa['p'][mid - i].start_node['name'] #从路径的结尾关系开始，查找每组对应的关系（每两个节点之间建立关系）的起始点
        if midnode in lisor:
            print('info')
            break


lisor = ['浪潮集团', '浪潮国际', '软件集团', '浪潮信息', '浪潮金融']
# 起始点为人，人隶属于组织
node = gra.run("match (a)-[]->(b) where b.real_name='李纪波' return ID(a),a.name").data()
# print(node[0])
while node[0]['a.name'] not in lisor:
    nodeid = node[0]['ID(a)']
 # ID便于设置节点的唯一性
    node = gra.run("match (a)-[]->(b) where ID(b) = " + str(nodeid) + " return ID(a),a.name").data()
    print(node)
if node[0]['a.name'] in lisor:
    pass
    print('Payment info:')



if __name__ == '__main__':
    print('d')


file_list = []
i = 0
with open('E:/temp/single_img_info.txt','rb') as csvfil:
   for line in csvfil.readlines():
         img_name = line.decode(encoding='utf-8').replace('\n','').split(',')[0]
         if img_name[:4] != 'name':
           print(len(img_name))
           i = i+1
'''
with open('/home/xiaxin/image/data/label_files/csv/records_rectify.csv','rb') as file_:
     for lin in file_.readlines():
         img_info = lin.replace('\n','').split(',')
         img_name = img_info[0]
         img_weight = img_info[2]
         img_height = img_info[3]
         (x1,y1) = img_info[6:7]
         (x2,y2) = img_info[8:9]
         (x3,y3) = img_info[10:11]
         (x4,y4) = img_info[12:13]
         print(img_info)
         print(img_name)
         print(img_weight)
         print(img_height)
         print(type(img_height))
         print(x1,y1)
         print(x2,y2)
         print(x3,y3)
         print(x4,y4)
         print(type(x1))
'''