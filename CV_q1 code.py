import cv2 
image_path= ("C://Users//BABU//OneDrive//Desktop//CV practicals//cv_pr1.jpg")
image= cv2.imread("C://Users//BABU//OneDrive//Desktop//CV practicals//cv_pr1.jpg")
gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale image', gray_image)
cv2.waitkey(0)
cv2.destroyAllWindows()
