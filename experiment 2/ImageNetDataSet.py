
from PIL import Image
import torch 
from torch.utils.data import Dataset

class ImageNetDataset(Dataset):
    """ImageNet Dataset"""
    def __init__(self,txt_file,root_dir,transform=None):
        meta = open(txt_file, 'r')
        imgs =[]
        for line in meta:
            line = line.strip('\n')
            words = line.split() 
            imgs.append((words[0],int(words[1])))
        self.imgs = imgs
        self.transform = transform 
        self.target_transform = target_transform
        
    def __getitem__(self, index):
        fn, label = self.imgs[index]
        path = root_dir + '/' + fn
        img = Image.open(path).convert('RGB')
        if self.transform is not None:
            img = self.transform(img)
        return img,label

    def __len__(self):
        return len(self.imgs)