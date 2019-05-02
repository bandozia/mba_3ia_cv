import cv2
import numpy as np
import matplotlib.pyplot as plt
from anutils import fig_to_mat, show_penca_de_windows,create_gradient_by_v

def predocolor(img_path):
    img = cv2.imread(img_path)
    cv2.cvtColor(img, cv2.COLOR_BGR2HSV, dst=img)
    hist = cv2.calcHist([img], [0], None, [360], [0,360])

    # *2 porque estou trabalhando com 360 graus e o histograma esta calculando 180
    top_colors = np.argpartition(hist.ravel(), -3)[-3:] * 2

    fig = plt.figure()
    plt.plot(hist)
    cv2.cvtColor(img, cv2.COLOR_HSV2BGR, dst=img)
    print(get_maisoumenos_nome_das_cores(top_colors, False))
    show_penca_de_windows([img,fig_to_mat(fig),create_gradient_by_v(top_colors,200,70)])


def get_maisoumenos_nome_das_cores(huelist, halfdisk=True):
    cores = []
    if not halfdisk:
        huelist = huelist / 2

    for h in huelist:
        if h >= 0 and h <= 15:
            cor = "vemelho"
        elif h > 15 and h <= 22:
            cor = "laranja"
        elif h > 22 and h <= 30:
            cor = "amarelo"
        elif h > 30 and h <= 37:
            cor = "amarelo"
        elif h > 37 and h <= 60:
            cor = "verde"
        elif h > 60 and h <= 75:
            cor = "verde"
        elif h > 75 and h <= 90:
            cor = "magenta"
        elif h > 90 and h <= 105:
            cor = "magenta"
        elif h > 105 and h <= 120:
            cor = "azul"
        elif h > 120 and h <= 135:
            cor = "roxo"
        elif h > 135 and h <= 150:
            cor = "rosa"
        elif h > 150 and h <= 165:
            cor = "rosa"
        elif h > 165 and h <= 180:
            cor = "vermelho"
        cores.append(cor)
    return set(cores)



predocolor("../images/a1/simpsons.jpeg")
