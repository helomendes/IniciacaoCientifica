import matplotlib.pyplot as plt
import cv2 as cv

class Image:
    def __init__(self, img):
        self.original = img 
        assert self.original is not None, "file could not be read"
        self.rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        self.blur = cv.GaussianBlur(self.gray, (3,3), 0)  

    def saveFig(self, name, alg):
        plt.figure(figsize=(15,10))

        '''
        plt.subplot(3,3,1)
        plt.imshow(self.rgb)
        plt.title('Original Image')
        plt.axis('off')

        plt.subplot(3,3,2)
        plt.imshow(self.gray, cmap='gray')
        plt.title('Gray Image')
        plt.axis('off')
        '''

        i = 1 
        for method in (["sobel", "Sobel"], ["canny", "Canny"], ["laplacian", "Laplacian"], ["prewitt", "Prewitt"], ["robertsCross", "RobertsCross"], ["scharr", "Scharr"]):
            plt.subplot(2,3,i)
            attr = getattr(alg, method[0])
            if method[0] == 'laplacian':
                plt.imshow(attr, cmap='gray', vmin=0, vmax=255)
            else:
                plt.imshow(attr, cmap='gray')
            plt.title(method[1], fontsize=25)
            plt.axis('off')
            i += 1

        plt.savefig(name)

