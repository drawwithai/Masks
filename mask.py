#!/usr/bin/python3.7

# import cv2
# import numpy as np
#
# # read image
# img = cv2.imread('rose.png')
#
# #mask it - method 1:
# # read mask as grayscale in range 0 to 255
# mask1 = cv2.imread('mask.png',0)
# result1 = img.copy()
# result1[mask1 == 0] = 0
# result1[mask1 != 0] = img[mask1 != 0]
#
# # mask it - method 2:
# # read mask normally, but divide by 255.0, so range is 0 to 1 as float
# # mask2 = cv2.imread('mask.png') / 255.0
# # mask by multiplication, clip to range 0 to 255 and make integer
# # result2 = (img * mask2).clip(0, 255).astype(np.uint8)
#
# cv2.imshow('image', img)
# cv2.imshow('mask1', mask1)
# cv2.imshow('masked image1', result1)
# # cv2.imshow('masked image2', result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # save results
# cv2.imwrite('pink_flower_masked1.png', result1)
# # cv2.imwrite('pink_flower_masked2.png', result2)
import cv2
import numpy as np
from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(description='Mask all images from input dir to output dir')
parser.add_argument('input', type=str, help='Input directory')
parser.add_argument('output', type=str, help='Output directory')

args = parser.parse_args()

for file in os.listdir(args.input):
    if file.endswith(".jpg") :
        input = os.path.join(args.input, file)
        output = os.path.join(args.output, file)
        # print(input, output)

        image = cv2.imread(input)
        mask = np.zeros(image.shape, dtype=np.uint8)
        mask = cv2.circle(mask, (260, 300), 225, (255,255,255), -1)
        masked = cv2.bitwise_and(image, mask)
        cv2.imwrite(output, masked)
