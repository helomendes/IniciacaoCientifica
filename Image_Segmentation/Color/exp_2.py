import skimage as ski
import os
import matplotlib.pyplot as plt

def main():
    camera = ski.data.camera() 
    print(type(camera))
    print(camera.shape)
    coins = ski.data.coins()
    threshold_value = ski.filters.threshold_otsu(coins)
    print(threshold_value)
    filename = os.path.join(ski.data_dir, 'moon.png')    
    moon = ski.io.imread(filename)

if  __name__=="__main__":
    main()

