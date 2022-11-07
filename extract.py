import numpy as np
import cv2 
import os

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def extract_img(data, dir):
    for i in range(len(data[b'data'])):
        img = np.reshape(data[b'data'][i],(3,32,32))
        img = np.transpose(img, (1,2,0))
        path = os.path.join(dir, str(label_names[b'fine_label_names'][data[b'fine_labels'][i]].decode("utf-8")))
        filename = str(data[b'filenames'][i].decode("utf-8"))
        if not os.path.isdir(path):
            os.mkdir(path)
        cv2.imwrite(os.path.join(path , filename) , img)

if not os.path.isdir("training_set"):
    os.mkdir("training_set")
if not os.path.isdir("testing_set"):
    os.mkdir("testing_set")

train_data = unpickle("train")
test_data = unpickle("test")
# b'filenames'
# b'batch_label'
# b'fine_labels' -> classes e.g. baby, boy, girl, man, woman
# b'coarse_labels' -> superclass e.g. people
# b'data' -> images

label_names = unpickle("meta")
# b'fine_label_names'
# b'coarse_label_names'

extract_img(train_data, "training_set")
extract_img(test_data, "testing_set")
