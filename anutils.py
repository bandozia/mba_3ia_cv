import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def fig_to_mat(fig):
    fig.canvas.draw()
    buffer = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8)
    buffer  = buffer.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    buffer = cv2.cvtColor(buffer, cv2.COLOR_RGB2BGR)

    return buffer


def show_penca_de_windows(matList):
    for i,mat in enumerate(matList):
        cwn = "win_%s" % i
        cv2.namedWindow(cwn)
        if i > 0:
            cv2.moveWindow(cwn, matList[i-1].shape[1],0)
        else:
            cv2.moveWindow(cwn, 0,0)
        cv2.imshow(cwn, mat)
    cv2.waitKey()


def hsv_to_rgb(h,s,v):
    C = v * s
    X = C * (1 - abs((h / 60) % 2 - 1))
    m = v - C

    erregbes = [(C,X,0),(X,C,0),(0,C,X),(0,X,C),(X,0,C),(C,0,X)]
    (r,g,b) = erregbes[math.floor(h / 60)]
    return ( round((r+m)*255), round((g+m)*255), round((b+m)*255) )
