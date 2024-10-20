import torchvision.models as models
import torch 
import torch.nn as nn


class Encoder_CNN(nn.Module):
    def __init__(self, embed_size,train_CNN=False):
        super(Encoder_CNN,self).__init__()
        self.train_CNN=train_CNN
        self.resnet50=models.resnet50(weights=models.ResNet50_Weights.default)
        self.resnet50.fc=nn.Linear(self.resnet50.fc.in_features,embed_size)
        self.relu=nn.ReLU()
        self.times=[]
        self.dropout=nn.Dropout(0.2)
        
    def forward(self,images):
        features=self.resnet50(images)
        return self.dropout(self.relu(features))
    
    