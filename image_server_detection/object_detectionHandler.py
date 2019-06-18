import tensorflow as tf
import matplotlib.pyplot as plt
from im_recognition import image_object_detect

'''
pic1 = base64.b64encode(pic.read())
pic = base64.b64decode(pic1)
str_to_num = np.fromstring(pic, np.uint8)
im = cv2.imdecode(str_to_num, cv2.IMREAD_COLOR)
'''
def object_detection(path):
    # 定义默认图，并将存储的图结构导入
    detect_graph = tf.Graph()
    with detect_graph.as_default():
        graph_def = tf.GraphDef()
        with tf.gfile.GFile('E:\\model_data\\ssd_inception_v2.pb', 'rb') as fid:
            graph_def.ParseFromString(fid.read())
            tf.import_graph_def(graph_def, name='')
        sess = tf.Session(graph=detect_graph)  # 启动会话
        out_image = image_object_detect(path, sess, detect_graph)  # 基于json格式的数据进行转化
    return out_image
        #plt.imshow(out_image)
        #plt.show()
