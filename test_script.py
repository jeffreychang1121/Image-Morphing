'''
  File name: test_script.py
  Author: 
  Date Created:
'''

'''
  File clarification:
    Check the accuracy of your algorithm
'''


import numpy as np
from morph_tri import morph_tri



# test triangulation morphing
def test_tri(im1, im2, im1_pts, im2_pts, warp_frac, dissolve_frac):
  # generate morphed image
  morphed_ims = morph_tri(im1, im2, im1_pts, im2_pts, warp_frac, dissolve_frac)

  # check output output image number
  if morphed_ims.shape[0] != 2:
    print ("The number of output image is wrong.")
    return False

  morphed_im1 = morphed_ims[0, :, :, :]
  # check the color channel number
  if morphed_im1.shape[2] != 3:
    print ("What happened to color channel?")
    return False

  # check the image size
  if morphed_im1.shape[0] != 50 or morphed_im1.shape[1] != 50:
    print ("Something wrong about the size of output image.")
    return False

  print ("Triangulation Morphing Test Passed!")
  return True



# the main test code
def main():
  # dummy image 1 and 2
  im1 = np.ones((50, 50, 3))
  im2 = np.zeros((50, 50, 3))

  # dummy correspondence
  im1_pts = np.array([[0, 0], [0, 49], [49, 0], [49, 49], [25, 25]])
  im2_pts = np.array([[0, 0], [0, 49], [49, 0], [49, 49], [20, 20]])

  # dummy warp_frac and dissolve_frac
  warp_frac, dissolve_frac = np.array([0.2, 0.3]), np.array([0.1, 0.3])

  # test triangulation morphing
  if not test_tri(im1, im2, im1_pts, im2_pts, warp_frac, dissolve_frac):
    print ("The Triangulation Morphing test failed.")
    return


  print("All tests passed! ")
  return


if __name__ == "__main__":
  main()
