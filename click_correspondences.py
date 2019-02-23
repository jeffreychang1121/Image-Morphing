'''
  File name: click_correspondences.py
  Author: 
  Date created: 
'''

'''
  File clarification:
    Click correspondences between two images
    - Input im1: source image
    - Input im2: target image
    - Output im1_pts: correspondences coordiantes in the source image
    - Output im2_pts: correspondences coordiantes in the target image
'''

import cpselect as cp
import numpy as np
import scipy.misc as sm

def click_correspondences(im1, im2):
  '''
    Tips:
      - use 'matplotlib.pyplot.subplot' to create a figure that shows the source and target image together
      - add arguments in the 'imshow' function for better image view
      - use function 'ginput' and click correspondences in two images in turn
      - please check the 'ginput' function documentation carefully
        + determine the number of correspondences by yourself which is the argument of 'ginput' function
        + when using ginput, left click represents selection, right click represents removing the last click
        + click points in two images in turn and once you finish it, the function is supposed to 
          return a NumPy array contains correspondences position in two images
  '''
  im1_pts, im2_pts, src_im, trg_img  = cp.cpselect(im1, im2)

  np.save('source.npy', im1_pts)
  np.save('target.npy', im2_pts)
  sm.imsave('source.jpg', src_im)
  sm.imsave('target.jpg', trg_img)

  return im1_pts, im2_pts, src_im, trg_img
