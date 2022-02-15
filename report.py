

# -*- coding: utf-8 -*-
#from src.imgtests import isblur,isnoise,isscrolled,isaligned,checkscale,mirror,blackspots, ssim_score, brisque_score
from imgtests import *
from configmain import *
import csv


def generate_report(camid, test_img_path, perfect_img_path):
    # preprocessing test and perfect images
    test_img = cv2.imread(test_img_path)
    test_img = cv2.resize(test_img, (IMG_WIDTH, IMG_HEIGHT))
    perfect_img = cv2.imread(perfect_img_path)
    perfect_img = cv2.resize(perfect_img, (IMG_WIDTH, IMG_HEIGHT))
    test_img_rotate = cv2.imread(test_img_path)
    # preprocessing image for image shift calculation
    # 0 means image is read in grayscale mode
    test_img_shift = cv2.imread(test_img_path, 0)
    # 0 means image is read in grayscale mode
    perfect_img_shift = cv2.imread(perfect_img_path, 0)
    # reading original image for scrolling calculation
    test_img_scrolled = cv2.imread(test_img_path)
    # preprocessing images for SSIM calculation
    # 0 means image is read in grayscale mode
    test_img_SSIM = cv2.imread(test_img_path, 0)
    test_img_SSIM = cv2.resize(test_img_SSIM, (IMG_WIDTH, IMG_HEIGHT))
    # 0 means image is read in grayscale mode
    perfect_img_SSIM = cv2.imread(perfect_img_path, 0)
    perfect_img_SSIM = cv2.resize(perfect_img_SSIM, (IMG_WIDTH, IMG_HEIGHT))
    #test_img_rotate = cv2.resize(test_img_rotate, (100, 100), interpolation = cv2.INTER_NEAREST)
    # align_homography
    # im - Read image to tested
    #im_test = cv2.imread(test_img_path, cv2.IMREAD_COLOR)
   # imReference -perfect Image
    #im_perfect = cv2.imread(perfect_img, cv2.IMREAD_COLOR)
    # cv2.imread(

    # image_test_results = [isblur(test_img),
    #                       checkscale(test_img),
    #                       isnoise(test_img),
    #                       isscrolled(test_img),
    #                       isaligned(test_img, perfect_img),
    #                       isshifted(perfect_img_shift, test_img_shift),
    #                       mirror(test_img, perfect_img),
    #                       blackspots(test_img_path),
    #                       ssim_score(test_img, perfect_img),
    #                       static_lines(test_img, perfect_img),
    #                       rotation_degrees(test_img_rotate)
    #                       ]
    """  image_test_results = [isblur(test_img),
                          checkscale(test_img),
                          isnoise(test_img),
                          isscrolled(test_img),
                          isaligned(test_img,perfect_img),
                          mirror(test_img,perfect_img),
                          blackspots(test_img_path),
                          ssim_score(test_img,perfect_img),
                          brisque_score(test_img_brisque)  
                          ] """

    # image_test_results = [not_inverted(test_img, perfect_img),
    #                       not_mirrored(test_img, perfect_img),
    #                       rotation(test_img),
    #                       not_cropped_in_ROI_region(test_img, perfect_img),
    #                       no_noise_staticline_scrolling(test_img, perfect_img),
    #                       isblur(test_img),
    #                       checkscale(test_img),
    #                       isnoise(test_img),
    #                       isscrolled(test_img),
    #                       isaligned(test_img, perfect_img),
    #                       isshifted(test_img_shift, perfect_img_shift),
    #                       mirror(test_img, perfect_img),
    #                       blackspots(test_img_path),
    #                       static_lines(test_img, perfect_img),
    #                       ssim_score(test_img, perfect_img),
    #                       brisque_score(test_img_path)
    #                       ]
    image_test_results = [Image_Not_Inverted(test_img, perfect_img),
                          Image_Not_Mirrored(test_img, perfect_img),
                          Image_Rotation(test_img),
                          Image_Horizontal_Shift(
                              test_img_shift, perfect_img_shift),
                          Image_Vertical_Shift(
                              test_img_shift, perfect_img_shift),
                          Image_Not_Cropped_In_ROI(test_img, perfect_img),
                          Image_Has_No_Noise_Staticlines_Scrolling(
                              test_img, test_img_scrolled),
                          SSIM_score(test_img_SSIM, perfect_img_SSIM),
                          BRISQUE_score(test_img_path)
                          ]
    image_test_results = [camid] + image_test_results
    save_results(image_test_results)
    return image_test_results


def save_results(image_test_results):
    #fields = ['CamId','Blur','color_scale','noise','scrolled','allign','mirror','blackspots','ssim_score','brisque_score']
    filepath = BASE_PATH + "/result.csv"

    with open(filepath, "a+") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(image_test_results)
