# Need this flag to prevent useless warnings on OSX
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

# Constant nodes
# takes no inputs, and it outputs a value it stores internally
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly

# Just prints info about the nodes. Doesn't actually run them.
# printing ("hello world")
print(node1, node2)

# Here, we actually run the nodes in a session
sess = tf.Session()
print(sess.run([node1, node2]))
