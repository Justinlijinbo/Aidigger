# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:59:16 2018

@author: JINBOLI 
"""
'''
随机梯度下降实现 一个两层的神经网络(无隐藏层)
假设输出层的大小为1.
'''

import numpy as np

class Network(object):
    
    def __init__(self, num_input, num_output = 1):
        
        '''
        num_input, num_output 标书输入层输出层的 数据个数
        biases 表示 每个神经元的偏移值 (输入层无偏移值)
        weights 表示 比重 
        biases 和 weights 初始值为随机值
        '''
        self.num_input = num_input
        self.num_output = output
        self.num_layers = 2
        #self.biases = np.zeros(num_output)
        self.weights = np.random.randn(num_output, num_input)
        
    def GD(self, input_data, output_data, epochs, eta, max_error):
        '''
        training_data 训练数据
        eps 迭代次数
        eta 学习步长
        max_error 假设最大输出层的误差值
        '''
        y = []
        y.append(output_data)
        error_max = 1.0
        for i in range(epochs):
            '''y_i 为期望得到的输出值 '''
            y_i = self.feedforword(input_data)
            print('y'+str(i)+'为'+ str(y_i))    
            error = abs(y_i - output_data[0])
            print('第' + str(i) + '次迭代误差值:' + str(error))
            if max_error <= error and error_max > error:
                error_max = error
                y.append(y_i)
                delta_i = sigmoid_prime(y_i) * (sigmoid(y_i) - output_data[0]) * eta
                print(delta_i)                       
                n_w = self.backprop(input_data,output_data,delta_i)
                self.weights = n_w
            else: break
        print(self.weights)
            
        
            
    def backprop(self, input_data, output_data, delta):
            
        nabla_w = self.weights - delta * input_data
        
        return nabla_w
        

    def feedforword(self, a):
        """
        以a为输入值 运行一次神经网络得到输出值a
        """
        a = sigmoid(np.dot(self.weights, a))
        return a


def sigmoid(z):
    """
    sigmoid 方程
    """
    return 1.0/(1.0 + np.exp(-z))

def sigmoid_prime(z):
    """
    sigmoid 方程的导数
    """
    return sigmoid(z)*(1-sigmoid(z))


if __name__ == "__main__":
    
    input = np.array([3,7,4,8])
    output = np.array([0.7])
    
    net = Network(4,1)
    net.GD(input,output,20,0.1,0.01)