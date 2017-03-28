import tensorflow as tf
hello=tf.constant("Hello, Tensorflow")
Sess=tf.Session()
print(Sess.run(hello))
print(Sess.run(hello))
