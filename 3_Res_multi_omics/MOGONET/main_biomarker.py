""" Example for biomarker identification
script that looks for important features 
"""
import os
import copy
from feat_importance import cal_feat_imp, summarize_imp_feat
import torch
torch.manual_seed(14)

if __name__ == "__main__":
    data_folder = 'SPLIT2'
    model_folder = os.path.join(data_folder, 'models')
    view_list = [1, 2, 3]
    if data_folder == 'ROSMAP':
        num_class = 2
    if data_folder == 'BRCA':
        num_class = 5
    if data_folder == 'ABOVE_25':
        num_class = 2
    elif data_folder == 'SPLIT2':
        num_class = 2
    elif data_folder == 'SPLIT3':
        num_class = 2
    elif data_folder == 'SPLIT4':
        num_class = 2
    elif data_folder == 'SPLIT5':
        num_class = 2

    featimp_list_list = []
    for rep in range(5):
        featimp_list = cal_feat_imp(data_folder, os.path.join(model_folder, str(rep+1)), 
                                    view_list, num_class)
        print("Done first step")
        featimp_list_list.append(copy.deepcopy(featimp_list))
    summarize_imp_feat(featimp_list_list)
    