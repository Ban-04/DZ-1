import cv2
image = cv2.imread('images/SS.png')

print(f'Image shape: {image.shape}')

height = image.shape[0]
width = image.shape[1]
depth = image.shape[2]

roi = image [:height// 2, :]

roi[:,:,0] = 0
roi[:,:,1] = 0
roi[:,:,2] = 0

image [height// 2+1:, :] = roi

#image[:, 50:150]=(255,255,0)
cv2.imshow('Sliced Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



