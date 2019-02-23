import numpy as np
from PIL import Image   # read image in RGB
import imageio
import cv2              # read image in BGR
from click_correspondences import click_correspondences
from morph_tri import morph_tri

im1 = cv2.imread('before.jpg')
b,g,r = cv2.split(im1)
im1_rgb = cv2.merge([r,g,b])

im2 = cv2.imread('after.jpg')
b,g,r = cv2.split(im2)
im2_rgb = cv2.merge([r,g,b])

# corresponding points and resized images
# im1_pts, im2_pts, source, target = click_correspondences(im1_rgb, im2_rgb)

im1_pts = np.load('source.npy')
im2_pts = np.load('target.npy')

# add corner points to form corner triangles
im1_pts = np.row_stack((im1_pts, np.array([[0, 0], [0, 500], [500, 0], [500, 500]])))
im2_pts = np.row_stack((im2_pts, np.array([[0, 0], [0, 500], [500, 0], [500, 500]])))

# create 60 frames in the range [0,1] for warping and cross-dissolving
warp_frac = np.arange(0,1,1/59)
warp_frac = np.concatenate((warp_frac, [1]), axis=0)    # append 1 at the end
dissolve_frac = warp_frac

# morphed image
morph_im = morph_tri(im1_rgb, im2_rgb, im1_pts, im2_pts, warp_frac, dissolve_frac)

# create gif
res_list = []
for i in range(warp_frac.shape[0]):
    res_list.append(morph_im[i,:,:,:])
imageio.mimsave('morphing.gif', res_list)






