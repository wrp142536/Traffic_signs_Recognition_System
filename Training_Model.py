from System.AlexNet import AlexNet
from System.Interface1 import Interface1
from System.OperationInterface import OperationInterface

class Training_Model(OperationInterface):
    """如果之后设计了别的网络结构，可以再增加一个选择网络结构的功能，然后在这个类里选用
    def __init__():
        # 设定激活函数、图片格式等


        pass

    def Training():
        # AlexNet.AlexNetTraining(图片路径)


        pass
