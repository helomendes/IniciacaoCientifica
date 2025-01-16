from skimage import color
from skimage import io
from matplotlib import pyplot as plt

def main():
    img = io.imread('/home/hbm22/Pictures/Biopsy/BO097Osteoide2.PNG')[:,:,:3]
    imgGray = color.rgb2gray(img)
    io.imshow(imgGray)
    plt.show()

if __name__=="__main__":
    main()
