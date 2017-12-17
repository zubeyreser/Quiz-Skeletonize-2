# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:39:21 2017

@author: ESER
"""

import os
import matplotlib.pyplot as plt
from skimage.data import data_dir
from skimage import io
from skimage.morphology import skeletonize




def plot_comparison(original, filtered, filter_name):

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,
                                   sharey=True)
    ax1.imshow(original, cmap=plt.cm.gray)
    ax1.set_title('original')
    ax1.axis('off')
    ax1.set_adjustable('box-forced')
    ax2.imshow(filtered, cmap=plt.cm.gray)
    ax2.set_title(filter_name)
    ax2.axis('off')
    ax2.set_adjustable('box-forced')

horse = io.imread(os.path.join(data_dir, "horse.png"), as_grey=True)

sk = skeletonize(horse == 0)
plot_comparison(horse, sk, 'skeletonize')