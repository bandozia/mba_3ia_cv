import numpy as np
import cv2
from anutils import load_image_folder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def media_brilho(mat):
    hsv_mat = cv2.cvtColor(mat, cv2.COLOR_BGR2HSV)
    sb = np.sum(hsv_mat[:,:,2])
    a = mat.shape[0] * mat.shape[1]
    return sb / a


def featurizar_por_brilho(mlList):
    feature_list = []
    for mat,label in mlList:
        res_mat = cv2.resize(mat, (1000,600), interpolation=cv2.INTER_LINEAR)
        bm = media_brilho(mat)
        label_enc = 1 if label == "day" else 0
        feature_list.append((bm,label_enc))
    return feature_list


train_set = load_image_folder("../images/a2/training", ["day","night"])
test_set = load_image_folder("../images/a2/test", ["day","night"])

features_train = featurizar_por_brilho(train_set)
features_test = featurizar_por_brilho(test_set)

X_train = np.array([x[0] for x in features_train]).reshape(-1,1)
y_train = np.array([y[1] for y in features_train])

classificador = SVC(kernel="linear")
classificador.fit(X_train,y_train)

X_test = np.array([x[0] for x in features_test]).reshape(-1,1)
y_test =  np.array([y[1] for y in features_test])

y_pred = classificador.predict(X_test)

print("Acuracia do modelo:")
print(accuracy_score(y_test,y_pred))

cv2.imshow("teste", test_set[0])
cv2.waitKey()
