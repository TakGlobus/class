
import os
import time
import argparse
import numpy as np
import tensorflow as tf

from tensorflow.python.keras.layers import *                                                    
from tensorflow.python.keras.models import Model
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.client import timeline

# Hyper-parameters
learning_rate = 0.01
epoch = 100
nbatch = 32

# image shapes
height = 32
width  = 32

def main(args):
    # Select model
    #   mlp or mobilenet or resnet
    if args.mtype == 'mlp': 
      from mlp import model_class
    elif args.mtype == 'mobilenet': 
      from mobilenet import mobilenet as model_class
    elif args.mtype == 'resnet': 
      from resnet import resnet as model_class

    # get data
    mnist = input_data.read_data_sets(os.path.abspath("./MNIST_data/"), one_hot=True)
    train_images =  mnist.train.images
    train_labels =  mnist.train.labels

    # build data pipeline 
    dataset = input_fn(train_images, train_labels, mtype=args.mtype)
    train_iterator = dataset.make_initializable_iterator()
    imgs, labels = train_iterator.get_next()

    # Attempting to connect all nodes in `tf.train.ClusterSpec`.
    # worker : idaten : 10.143.3.3
    # ps     : takuya's windows WSL 10.150.51.30:2222
    # ps     : CS Linux UChicago 128.135.164.173:2222
    # ps/worker : local-servers 127.0.0.1:2222
    cluster_spec = tf.train.ClusterSpec({
        'worker': [
            '10.143.3.3:2222',
        ],
        'ps': ['128.135.164.173:2222'],
    })
        #'ps': ['128.135.164.173:2222'],

    server = tf.train.Server(cluster_spec,
                             job_name=args.job_name,
                             task_index=args.task_index)

    if args.job_name == "ps":
        # `server.join()` means it's NEVER killed
        server.join()
    else:
        # Store the variables into `ps`.
        print("\n   Worker Wake up!   \n", flush=True)
        with tf.device(tf.train.replica_device_setter(
                cluster=cluster_spec)):

            global_step = tf.train.create_global_step()
            get_global_step = tf.train.get_global_step()

            # Model
            try:
              if args.mtype == 'mlp' :
                model = model_class(net_name='mlp')
              elif args.mtype ==  'mobilenet':
                model = model_class(net_name='mobilenet', model_layer=17, input_h=height, input_w=width, num_classes=10)
              elif args.mtype ==  'resnet':
                model = model_class(net_name='resnet', model_layer=50, input_h=height, input_w=width, num_classes=10)
            except:
              raise NameError("\n ###  Error! Make sure your model type argument is mlp or mobilenet or resnet ###\n")


            # mlp
            preds = model.build(imgs)

            # Metrics
            loss = tf.reduce_mean(tf.losses.softmax_cross_entropy(onehot_labels=labels, logits=preds))
            optimizer = tf.train.AdamOptimizer(learning_rate)
            train_op = optimizer.minimize(loss, global_step=global_step)

            is_chief = (args.task_index == 0)

            hooks = [tf.train.StopAtStepHook(last_step=epoch),
                     tf.train.CheckpointSaverHook('./example-save',
                                                  save_steps=epoch,
                                                  saver=tf.train.Saver(max_to_keep=1))]

            # Initialize the variables, if `is_chief`.
            config = tf.ConfigProto(
                    allow_soft_placement=True,
                    device_filters=[
                    '/job:ps', '/job:worker/task:%d' % args.task_index],
            )
            with tf.train.MonitoredTrainingSession(
                    is_chief=is_chief,
                    config=config,
                    master=server.target,
                    hooks=hooks) as sess:

                sess.run(train_iterator.initializer)
                start_time = time.perf_counter()
                start_clock = time.clock()
                while not sess.should_stop():
                    step, _, train_loss = sess.run([get_global_step, train_op, loss])
                    print('In {step} step: loss = {loss}'
                          .format(step=step, loss=train_loss))
                stop_time = time.perf_counter()
                stop_clock = time.clock()
        
                print('  Duration (via time.perf_counter()): %f (%f - %f)' % (stop_time - start_time, stop_time, start_time))
                print('  Clock (via time.clock()): %f (%f - %f)' % (stop_clock - start_clock, stop_clock, start_clock))

        # It's able to fetch variables in another session.
        #if is_chief:
        #    with tf.Session(server.target) as sess:
        #        w, b, acc = sess.run([w, b, accuracy],
        #                             feed_dict={x: X_test, y: y_test})
        #        print('accuracy in validation = ', acc)
        #        print('bias = ', b)
        #        print('weight = ', w)

def input_fn(images, labels, height=32, width=32, mtype='mlp',prefetch=1):
  """ 
    INPUT:  imagess : MNIST image [batch, height, width, channel]. np.ndarray
            labels  : MNIST image labels.  This should be one-hot 
            height/width : resized height, width
            mtype   : model type
            nbatch : batch size

    OUTPUT: tf.data object
  """
  # reshape other than mlp model
  images = images.reshape(-1,28,28,1)
  images = tf.image.resize(images, (height, width))
  if mtype == 'mlp':
    images = tf.reshape(images, [-1,height*width])
  
  dataset = tf.data.Dataset.from_tensor_slices((images, labels))
  dataset = dataset.shuffle(500).repeat().batch(nbatch).prefetch(prefetch)
  return dataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--job-name', dest='job_name', type=str,
                        choices=['ps', 'worker'])
    parser.add_argument('--task-index', dest='task_index', type=int,
                        default=0)
    parser.add_argument('--mtype', dest='mtype', type=str,
                        default='mlp')
    main(parser.parse_args())
