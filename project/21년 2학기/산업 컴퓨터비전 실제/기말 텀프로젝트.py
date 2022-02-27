import cv2
import numpy as np

images = []
images.append(cv2.imread('/Users/park/PycharmProjects/photo/project2/1.png', cv2.IMREAD_COLOR))
images.append(cv2.imread('/Users/park/PycharmProjects/photo/project2/2.png', cv2.IMREAD_COLOR))
images.append(cv2.imread('/Users/park/PycharmProjects/photo/project2/3.png', cv2.IMREAD_COLOR))

stitcher = cv2.createStitcher()
ret, pano = stitcher.stitch(images)

if ret == cv2.STITCHER_OK:
    pano = cv2.resize(pano, dsize=(0, 0), fx=1, fy=1)
    cv2.imshow('panorama', pano)
    cv2.waitKey()

    cv2.destroyAllWindows()

else:
    print('Error during stiching')

