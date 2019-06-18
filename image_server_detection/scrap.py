from keras import backend as K
from keras.models import load_model
import tensorflow as tf


def angle_difference(x, y):
    """
    Calculate minimum difference between two angles.
    """
    return 180 - abs(abs(x - y) - 180)

def angle_error(y_true, y_pred):
    """
    Calculate the mean diference between the true angles
    and the predicted angles. Each angle is represented
    as a binary vector.
    """
    diff = angle_difference(K.argmax(y_true), K.argmax(y_pred))
    return K.mean(K.cast(K.abs(diff), K.floatx()))

def freeze_session(session, model, keep_var_names=None, output_names=None, clear_devices=True):

    from tensorflow.python.framework.graph_util import convert_variables_to_constants
    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []


        if len(output_names) > 0:
            for i in range(len(output_names)):
                tf.identity(model.outputs[i], name=output_names[i])

        output_names += [v.op.name for v in tf.global_variables()]
        input_graph_def = graph.as_graph_def()

        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = convert_variables_to_constants(session, input_graph_def,output_names, freeze_var_names)

        return frozen_graph

# 测试用
if __name__ == "__main__":

    model_path = "/program files/git/RotNet/train/models/rotnet_street_view_resnet50.hdf5"
    print('0')
    model = load_model(model_path,custom_objects={'angle_error':angle_error})
    print('1')
    frozen_graph = freeze_session(K.get_session(), model, output_names=["outname"])
    tf.train.write_graph(frozen_graph, "./", "model.pb", as_text=False)



