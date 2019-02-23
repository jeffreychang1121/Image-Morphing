'''
  File name: morph_tri.py
  Author:
  Date created:
'''

'''
  File clarification:
    Image morphing via Triangulation
    - Input im1: source image
    - Input im2: target image
    - Input im1_pts: correspondences coordiantes in the source image
    - Input im2_pts: correspondences coordiantes in the target image
    - Input warp_frac: a vector contains warping parameters
    - Input dissolve_frac: a vector contains cross dissolve parameters

    - Output morphed_im: a set of morphed images obtained from different warp and dissolve parameters.
                         The size should be [number of images, image height, image Width, color channel number]
'''
import numpy as np
from scipy.spatial import Delaunay
from helpers import interp2

def morph_tri(im1, im2, im1_pts, im2_pts, warp_frac, dissolve_frac):

  # Tips: use Delaunay() function to get Delaunay triangulation;
  # Tips: use tri.find_simplex(pts) to find the triangulation index that pts locates in.

  num_of_frames = warp_frac.shape[0]
  row, col, ch = im1.shape
  # create meshgrid of x,y coordinate
  x, y = np.meshgrid(np.arange(col), np.arange(row))
  y = y.flatten()
  x = x.flatten()
  # create pixel coordinate in (x,y)
  pixel = np.stack((x,y), axis=1)
  # initialize morphing image
  morph_im = np.zeros([num_of_frames, row, col, ch], dtype='uint8')
  warp_src = np.zeros([num_of_frames, row, col, ch], dtype='uint8')
  warp_trg = np.zeros([num_of_frames, row, col, ch], dtype='uint8')

  for i in range(num_of_frames):
    # find interpolated points for Delaunay triangulation
    interp_pts = (1 - warp_frac[i]) * im1_pts + warp_frac[i] * im2_pts
    tri = Delaunay(interp_pts)
    # find the triangulation index that interp_pts locates in
    location = tri.find_simplex(pixel)
    # location = location.reshape(row, col)

    for j in range(np.shape(tri.simplices)[0]):
      # loop through every Delaunay triangles
      coor = pixel[np.where(location == j)]  # pixels that belongs to triangle j
      x = coor[:,0]
      y = coor[:,1]
      pixel_coor = np.row_stack((x, y, np.ones(x.shape[0])))

      # vertices of Delaunay triangles
      vertices = interp_pts[tri.simplices[j]]
      vertices = np.transpose(vertices)
      vertices = np.row_stack((vertices, np.ones([1,3])))
      inv_vertices = np.linalg.inv(vertices)

      # barycentric coordinates for each pixel
      bary_coor = np.dot(inv_vertices, pixel_coor)

      # vertices of Delaunay triangles from source picture
      vertices_src = im1_pts[tri.simplices[j]]
      vertices_src = np.transpose(vertices_src)
      vertices_src = np.row_stack((vertices_src, np.ones([1, 3])))
      source_coor = np.dot(vertices_src, bary_coor)

      # vertices of Delaunay triangles from target picture
      vertices_trg = im2_pts[tri.simplices[j]]
      vertices_trg = np.transpose(vertices_trg)
      vertices_trg = np.row_stack((vertices_trg, np.ones([1, 3])))
      target_coor = np.dot(vertices_trg, bary_coor)

      # interpolate through every pixel in source and target
      for k in range(ch):
        warp_src[i, y, x, k] = interp2(im1[:, :, k], source_coor[0, :], source_coor[1, :])
        warp_trg[i, y, x, k] = interp2(im2[:, :, k], target_coor[0, :], target_coor[1, :])

      morph_im[i, :, :, :] = (1-dissolve_frac[i]) * warp_src[i,:,:,:] + dissolve_frac[i] * warp_trg[i,:,:,:]

  # pixel value should be between [0,255]
  morph_im = np.clip(morph_im, 0, 255)

  return morph_im


