import torch
from fastai.vision import open_image, load_learner, defaults
import os.path

imageNum = 0

defaults.device = torch.device('cpu')

cwd = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(cwd, "../classifier/")
learn = load_learner(path)

def save_image(image):

    global cwd
    global imageNum
    imageNum+=1
    with open(cwd+'/tmp/'+str(imageNum)+str(image), 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)

    return cwd+'/tmp/'+str(imageNum)+str(image)

def predict(imagePath):

    global learn

    img = open_image(os.path.join(imagePath))
    pred_class,pred_idx,outputs = learn.predict(img)
    return pred_class