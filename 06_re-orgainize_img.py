# KF 12/13/2018

# Choose first 20 images in each folder of the 61 classes 

import os
import shutil
import json

#image_base_dir = '/home/kefeng/PlantDiseaseRecognition/disease_datasets/dataset_for_keras/train'

with open('label_to_disease_full.json','r') as f:
    l = json.load(f)


source_dir = '/home/kefeng/img_for_database'
dist_dir = 'img_with_names'

if not os.path.exists(dist_dir):
    os.makedirs(dist_dir)

# loop for all folders in the base directory
for d in range(61):

    source_sub_dir = os.path.join(source_dir, str(d))
    for line in l:
        if line[0] == d:
            dist_sub_dir = os.path.join(dist_dir, '_'.join([line[1], line[2]]))
            if not os.path.exists(dist_sub_dir):
                os.makedirs(dist_sub_dir)

    for f in os.listdir(source_sub_dir):
       shutil.copy(os.path.join(source_sub_dir, f), dist_sub_dir) 

        


