import cv2
import numpy as np
import matplotlib.pyplot as plt
from anutils import fig_to_mat, show_penca_de_windows

def predocolor(img_path):
    img = cv2.imread(img_path)
    cv2.cvtColor(img, cv2.COLOR_BGR2HSV, dst=img)
    hist = cv2.calcHist([img], [0], None, [180], [0,180])

    top_colors = np.argpartition(hist.ravel(), -3)[-3:]
    print(top_colors)
    
    #fig = plt.figure()
    #plt.plot(hist)
    #show_penca_de_windows([img,fig_to_mat(fig)])


predocolor("images/a1/futebol.jpg")
