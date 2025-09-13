#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED: 2025-09-09
# REVISED DATE:2025-09-13
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    # Create results dictionary
    results_dic = dict()

    # Get filenames from the provided image_dir
    try:
        filename_list = listdir(image_dir)
    except FileNotFoundError:
        # If a relative path was given that doesn't exist from current working dir,
        # try to gracefully hint by raising with a clearer message.
        raise FileNotFoundError(f"Image directory not found: {image_dir}")

    # Loop through filenames, skip hidden/system files
    for filename in filename_list:
        if filename.startswith('.'):
            continue  # skip hidden files like .DS_Store

        # Create a label from filename:
        #  - lowercase
        #  - split by '_'
        #  - keep only alphabetical tokens
        #  - join by single space and strip
        lower_name = filename.lower()
        tokens = lower_name.split('_')
        words = [t for t in tokens if t.isalpha()]
        pet_label = ' '.join(words).strip()

        # Add to dictionary as list [label]
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            # Warn but do not overwrite
            # (Following the project guidance to avoid duplicates)
            # You can print or log; here we keep it quiet to avoid noisy output.
            pass

    return results_dic
