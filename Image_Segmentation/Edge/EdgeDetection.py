import cv2 as cv
import numpy as np

class EdgeDetection:
    def __init__(self, image):
        self.image = image
        self.sobel_operator_x = [[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]]
        self.sobel_operator_y = [[-1, -2, -1],
                      [0, 0, 0],
                      [1, 2, 1]]


    def detectEdges(self):
        self.my_sobel()
        self.canny()
        self.laplacian()
        self.prewitt()
        self.robertsCross()
        self.scharr()

    def sobelKernel(self, flag):
        if flag == 0:
            kernel = self.sobel_operator_x
        elif flag == 1:
            kernel = self.sobel_operator_y
        else:
            return self.image.blur
        
        aux = np.zeros(self.image.blur.shape)
        for i, row in enumerate(self.image.blur):
            if i+2 < self.image.blur.shape[0]:
                for j, value in enumerate(row):
                    if j+2 < self.image.blur.shape[1]:
                        soma = 0
                        for k in range(3):
                            for l in range(3):
                                soma += int(self.image.blur[i+k][j+l]) * kernel[k][l]
                        aux[i+1][j+1] = soma
        return aux
 
    def sobel(self):
        gx = cv.Sobel(self.image.blur, cv.CV_64F, 1, 0, ksize=3)
        gy = cv.Sobel(self.image.blur, cv.CV_64F, 0, 1, ksize=3)
        g = np.sqrt(gx**2+gy**2)
        self.gx = np.uint8(255*np.abs(gx)/np.max(gx))
        self.gy = np.uint8(255*np.abs(gy)/np.max(gy))
        self.sobel = np.uint8(255*g/np.max(g))

    def my_sobel(self):
        gx = self.sobelKernel(0)
        gy = self.sobelKernel(1)
        g = np.sqrt(gx**2+gy**2)
        self.gx = np.uint8(255*np.abs(gx)/np.max(gx))
        self.gy = np.uint8(255*np.abs(gy)/np.max(gy))
        self.sobel = np.uint8(255*g/np.max(g))
       
    def canny(self):
        self.canny = cv.Canny(self.image.blur, 100,200)

    def laplacian(self):
        self.laplacian = cv.Laplacian(self.image.blur, cv.CV_64F)

    def prewitt(self):
        prewitt_operator_x = np.array([[-1, 0, -1],
                              [-1, 0, -1],
                              [-1, 0, -1]])
        prewitt_operator_y = np.array([[-1, -1, -1],
                              [0, 0, 0],
                              [1, 1, 1]])
        horizontal_edges = cv.filter2D(self.image.gray, -1, prewitt_operator_x)
        horizontal_edges = np.float32(horizontal_edges)
        vertical_edges = cv.filter2D(self.image.gray, -1, prewitt_operator_y)
        vertical_edges = np.float32(vertical_edges)
        gradient_magnitude = cv.magnitude(horizontal_edges, vertical_edges)

        threshold = 50

        _, edges = cv.threshold(gradient_magnitude, threshold, 255, cv.THRESH_BINARY)
        self.prewitt = edges

    def robertsCross(self):
        roberts_operator_x = np.array([[1, 0],
                                       [0, -1]])
        roberts_operator_y = np.array([[0, 1],
                                       [-1, 0]])
        horizontal_edges = cv.filter2D(self.image.gray, -1, roberts_operator_x)
        horizontal_edges = np.float32(horizontal_edges)
        vertical_edges = cv.filter2D(self.image.gray, -1, roberts_operator_x)
        vertical_edges = np.float32(vertical_edges)

        gradient_magnitude = cv.magnitude(horizontal_edges, vertical_edges)

        threshold = 50

        _, self.robertsCross = cv.threshold(gradient_magnitude, threshold, 255, cv.THRESH_BINARY)
        
    def scharr(self):
        gx = cv.Scharr(self.image.blur, cv.CV_64F, 1, 0)
        gy = cv.Scharr(self.image.blur, cv.CV_64F, 0, 1)
        self.scharr = cv.magnitude(gx, gy)
