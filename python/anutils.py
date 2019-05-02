import cv2
import numpy as np
import matplotlib.pyplot as plt
import os,glob,math

######################### helpers para o ex 1 aula 1 #############################
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


def hsv_to_rgb(h,s,v, bgr=True):
    C = v * s
    X = C * (1 - abs((h / 60) % 2 - 1))
    m = v - C

    erregbes = [(C,X,0),(X,C,0),(0,C,X),(0,X,C),(X,0,C),(C,0,X)]
    (r,g,b) = erregbes[math.floor(h / 60)]
    if bgr:
        return ( round((b+m)*255), round((g+m)*255), round((r+m)*255) )
    else:
        return ( round((r+m)*255), round((g+m)*255), round((b+m)*255) )


def create_gradient_by_v(vs,w,h,d=10):
    mat = np.zeros((h * len(vs),w,3), dtype=np.uint8)
    cw = round(w / d)
    for j,v in enumerate(vs):
        for i in range(0,d):
            cv2.rectangle(mat, (i*cw,h*j), ((i*cw)+cw, (h*j)+h), hsv_to_rgb(v, i / d, i / d), -1)

    return mat


######################### helpers para o ex 3 aula 2 #############################

def load_image_folder(path,labels):
    matlist = []
    for l in labels:
        for f in glob.glob(os.path.join(path,l,"*")):
            mat = cv2.imread(f)
            if not mat is None:
                matlist.append((mat,l))

    return matlist
