import os
import io
import sys
#sys.path.append('D:\\program file\\python program1\\untitled\\objection detection\\models_master\\research\object_detection')
import pandas as pd
import tensorflow as tf
from PIL import Image
from utils import dataset_util
from utils import label_map_util
from collections import namedtuple, OrderedDict

"""
Usage:  
   # From tensorflow/models/ 
   # Create train data:  python generate_tfrecord.py --csv_input=data/tv_vehicle_labels.csv  --output_path=train.record 
   # Create test data:  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=test.record
"""
#os.chdir('D:\\tensorflow-model\\models\\research\\object_detection\\')
'''flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
FLAGS = flags.FLAGS
'''
def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

def create_tf_example(group, label_map_dict, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size
    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(label_map_dict[row['class']]) #这里需要知道对应的标签映射

    tf_example = tf.train.Example(features=tf.train.Features(
        feature={'image/height': dataset_util.int64_feature(height),
                 'image/width': dataset_util.int64_feature(width),
                 'image/filename': dataset_util.bytes_feature(filename),
                 'image/source_id': dataset_util.bytes_feature(filename),
                 'image/encoded': dataset_util.bytes_feature(encoded_jpg),
                 'image/format': dataset_util.bytes_feature(image_format),
                 'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
                 'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
                 'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
                 'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
                 'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
                 'image/object/class/label': dataset_util.int64_list_feature(classes),
                 }))
    return tf_example
def main(_):
    #writer = tf.python_io.TFRecordWriter(FLAGS.output_path) # .record格式的文件输出位置（按照教程中的数据进行就可以了，不要随意更改）
    writer = tf.python_io.TFRecordWriter("D:\\program file\\python program1\\untitled\\objection detection\\payment_detection\\data\\test.record")  # .record格式的文件输出位置
    #label_map_dict = label_map_util.get_label_map_dict(FLAGS.label_map_path) # 数字与标签之间的转化文件存储路径
    label_map_dict = label_map_util.get_label_map_dict('D:\\program file\\python program1\\untitled\\objection detection\\payment_detection\\training\\payment_label_map.pbtxt')  # 数字与标签之间的转化文件存储路径
    #path = os.path.join(os.getcwd(), 'images') # 图片的存储位置
    path = os.path.join('D:\\program file\\python program1\\untitled\\objection detection\\payment_detection', 'images')
    #print(os.getcwd())
    #examples = pd.read_csv(FLAGS.csv_input)   # csv文FLAGS.label_map_path件的输出位置
    #examples = pd.read_csv(os.getcwd())
    examples = pd.read_csv('D:\\program file\\python program1\\untitled\\objection detection\\payment_detection\\data\\payment_labels.csv')
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, label_map_dict, path)
        writer.write(tf_example.SerializeToString())
    writer.close()
    #output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    output_path = os.path.join("D:\\program file\\python program1\\untitled\\objection detection\\payment_detection\\data")
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == "__main__":
    print("ad")
    tf.app.run()
    # main(_)