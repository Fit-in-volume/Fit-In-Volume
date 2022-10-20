import cv2

src = cv2.imread('/Users/krc/Downloads/Fit_in_Volume/rembg/Rembg_밴드2.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

bsize1 = 19
dst1 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, bsize1, 5) # C값은 5를 줌
bsize2 = 31
dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, bsize2, 5) # C값은 5를 줌
bsize3 = 51
dst3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, bsize3, 5) # C값은 5를 줌

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imwrite('./bsize19.jpg',dst1)
cv2.imwrite('./bsize31.jpg',dst2)
cv2.imwrite('./bsize51.jpg',dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()