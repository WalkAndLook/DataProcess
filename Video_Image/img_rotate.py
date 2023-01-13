# 判断是否要进行旋转图像

import cv2
path = r'C:\Users\xukechao\Desktop\图片11_10'

img =cv2.imread('test.jpg')
img_rotate =cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow('img_rotate',img_rotate)
k = cv2.waitKey(0)
if k==27:                    #ESC
   cv2.destroyAllWindows()
elif k==ord('s') :           #按下s
    cv2.imwrite('test.jpg',img_rotate) # 保存图像
    cv2.destroyAllWindows()