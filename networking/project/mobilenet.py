import tensorflow as tf
import tensorflow.contrib as tc

channel_num = 3

#MobileNetV2
class mobilenet(object):
    def __init__(self, net_name, model_layer, input_h, input_w, num_classes, is_training=True):
        """ net_name : model name (user specification)
            model_layer : number of layer ?
            input_h : height
            input_w : width
            num_class : number of label class
        """
        self.net_name = net_name
        self.model_layer_num = model_layer
        self.img_h = input_h
        self.img_w = input_w
        self.input_size = input_h * input_w * channel_num
        self.num_classes = num_classes
        self.is_training = is_training
        self.normalizer = tc.layers.batch_norm
        self.bn_params = {'is_training': self.is_training}
        self.model_size = 0

    def build(self, input):
        with tf.variable_scope(self.net_name + '_instance'):
            self.i = 0
            output = tc.layers.conv2d(input, 32, 3, 2, normalizer_fn=self.normalizer, normalizer_params=self.bn_params)
            self.model_size += (3 * 3 * channel_num * int(input.shape[1]) + 1) * 32

            net, net_size = self._inverted_bottleneck(output, 1, 16, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 24, 1)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 24, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 32, 1)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 32, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 32, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 64, 1)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 64, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 64, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 64, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 96, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 96, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 96, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 160, 1)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 160, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 160, 0)
            self.model_size += net_size
            net, net_size = self._inverted_bottleneck(net, 6, 320, 0)
            self.model_size += net_size

            net = tc.layers.conv2d(net, 1280, 1, normalizer_fn=self.normalizer, normalizer_params=self.bn_params) 
            self.model_size += (1 * 1 * int(net.shape[1]) + 1) * 1280

            avg_num = int(self.img_h // 32)
            # commet off below if user use original mnist size
            #avg_num = int(self.img_h // 28)
            net = tc.layers.avg_pool2d(net, avg_num)
            net = tc.layers.conv2d(net, self.num_classes, 1, activation_fn=None)
            self.model_size += (1 * 1 * int(net.shape[1]) + 1) * self.num_classes

            logits = tf.squeeze(net)
        return logits

    def _inverted_bottleneck(self, input, up_sample_rate, channels, subsample):
        with tf.variable_scope('inverted_bottleneck{}_{}_{}'.format(self.i, up_sample_rate, subsample)):
            layer_size = 0
            self.i += 1
            stride = 2 if subsample else 1
            num_outputs = up_sample_rate*input.get_shape().as_list()[-1]
            output = tc.layers.conv2d(input, num_outputs, 1,
                                      activation_fn=tf.nn.relu6,
                                      normalizer_fn=self.normalizer, normalizer_params=self.bn_params)
            layer_size += (1 * 1 * int(input.shape[1]) + 1) * num_outputs

            output = tc.layers.separable_conv2d(output, None, 3, 1, stride=stride,
                                                activation_fn=tf.nn.relu6,
                                                normalizer_fn=self.normalizer, normalizer_params=self.bn_params)

            layer_size += (3 * 3 * int(output.shape[1]) + 1) * channels

            output = tc.layers.conv2d(output, channels, 1, activation_fn=None,
                                      normalizer_fn=self.normalizer, normalizer_params=self.bn_params)
            layer_size += (1 * 1 * int(output.shape[1]) + 1) * channels

            if input.get_shape().as_list()[-1] == channels:
                output = tf.add(input, output)
                
            return output, layer_size

    def cost(self, logits, labels):
        with tf.name_scope('loss'):
            cross_entropy = tf.losses.softmax_cross_entropy(onehot_labels=labels, logits=logits)
        cross_entropy_cost = tf.reduce_mean(cross_entropy)

        with tf.name_scope('optimizer_test'):
            update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
            with tf.control_dependencies(update_ops):
                train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy_cost)

        return train_step

    def getModelInstanceName(self):
        return (self.net_name + " with layer: " + str(self.model_layer_num)) 

    def getModelMemSize(self):
        return self.model_size * 4 / (1024**2)
