""" Example for MOGONET classification
main script to choose folders and add our data to original script
"""
from train_test import train_test
import torch

torch.manual_seed(14) #128

if __name__ == "__main__":    
    data_folder = 'SPLIT5' 
    view_list = [1, 2, 3] 
    num_epoch_pretrain = 300 # 500
    num_epoch = 1200 #1200
    lr_e_pretrain = 1e-3
    lr_e = 5e-4 #5e-4
    lr_c = 1e-4 #1e-4
    
    if data_folder == 'ROSMAP':
        num_class = 2
    elif data_folder == 'BRCA':
        num_class = 5
    elif data_folder == 'SPLIT2':
        num_class = 2
    elif data_folder == 'SPLIT3':
        num_class = 2
    elif data_folder == 'SPLIT4':
        num_class = 2
    elif data_folder == 'SPLIT5':
        num_class = 2
    elif data_folder == 'ABOVE_25':
        num_class = 2
    

    train_test(data_folder, view_list, num_class,
               lr_e_pretrain, lr_e, lr_c, 
               num_epoch_pretrain, num_epoch)             
    
