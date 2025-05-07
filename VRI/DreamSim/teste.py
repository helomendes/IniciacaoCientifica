from dreamsim import dreamsim
from PIL import Image

model, preprocess = dreamsim(pretrained = True, cache_dir="/home/hbm22/.cache", device='cpu')

img1 = preprocess(Image.open("/home/hbm22/hmmetria/images/BO097Osteoide2.PNG"))

embedding = model.embed(img1)

img1 = preprocess(Image.open("/home/hbm22/hmmetria/images/BO097Osteoide2.PNG"))
img2 = preprocess(Image.open("/home/hbm22/hmmetria/images/BO097Osteoide3.PNG"))

distance = model(img1, img2)

print(distance)
