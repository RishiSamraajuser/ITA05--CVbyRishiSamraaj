Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> image= cv2.imread("C://Users//BABU//OneDrive//Desktop//CV practicals//cv_pr1.jpg")
>>> c=cv2.GaussianBlur(img,(5,5),0)
>>> cv2.imshow("original",img)
>>> cv2.imshow("blur",c)
>>> 