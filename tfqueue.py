import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from inspect import isfunction

class CustomFIFOQueue(tf.compat.v1.FIFOQueue):
    def dequeue_many(self, n, name=None):
        print(type(n), n)
        try:
            n = n()
        except Exception as e:
            pass
        return super().dequeue_many(n, name=name)