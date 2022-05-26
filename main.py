import cv2

path = "C:\\Users\\yagmu\\Documents\\aras.jpeg"
img = cv2.imread(path)

cv2.imshow('image', img)
(B, G, R) = cv2.split(img)
cv2.imshow('Blue', B)
cv2.imshow('Green', G)
cv2.imshow('Red', R)

print(img.shape)

for x in range(0,768):
    for y in range(0,1024):
        if B[x,y] > 100:
            B[x,y] = 10

a = cv2.merge([B,G,R])
cv2.imshow('merged', a)

cv2.waitKey(0)
