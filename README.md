# Image-Morphing
### 1. Defining Correspondences
       [im1_pts, im2_pts] = click_correspondences(im1, im2)
- (INPUT) im1: *H1* x *W1* x 3 matrix representing the first image
- (INPUT) im2: *H2* x *W2* x 3 matrix representing the second image
- (INPUT) im1_pts: *N* x 2 matrix representing correspondences in the first image
- (INPUT) im2_pts: *N* x 2 matrix representing correspondences in the second image
### 2. Image Morph Via Triangulation
       [morphed_im] = morph_tri( im1, im2, im1_pts, im2_pts, warp_frac, dissolve_frac)
- (INPUT) im1: *H1* x *W1* x 3 matrix representing the first image
- (INPUT) im2: *H2* x *W2* x 3 matrix representing the second image
- (INPUT) im1_pts: *N* x 2 matrix representing correspondences in the first image
- (INPUT) im2_pts: *N* x 2 matrix representing correspondences in the second image
- (INPUT) warp_frac: 1 x *M* vector representing each frame’s shape warping parameter
- (INPUT) dissolve_frac: 1 x *M* vector representing each frame’s cross-dissolve parameter
- (OUTPUT) morphed_im: Data structure containing output images
