#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Rama Sab
# DATE CREATED: 2025-09-09
# REVISED DATE: 2025-09-13
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels. This function inputs:
#            - The Image Folder as image_dir within classify_images function
#              and as in_arg.dir for the function call within main.
#            - The results dictionary as results_dic within classify_images
#              function and results for the function call within main.
#            - The CNN model architecture as model within classify_images function
#              and in_arg.arch for the function call within main.
#          This function uses the extend function to add items to the list
#          that's the 'value' of the results dictionary. You will be adding the
#          classifier label as the item at index 1 of the list and the comparison
#          of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images
import os
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case
    letters and stripping the leading and trailing whitespace characters.
    For example, the classifier function returns = 'Maltese dog, Maltese terrier, Maltese'
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog
    names separated by commas when a particular breed of dog has multiple dog
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian' (pet label) and it will match to the classifier label
    'dalmatian, coach dog, carriage dog' if the classifier function correctly
    classified the pet images of dalmatians.

    Parameters:
      images_dir (str): full path to folder of images to classify
      results_dic (dict): { filename: [pet_label] } — this function extends each
                          list to [pet_label, classifier_label, match_flag]
      model (str): CNN model architecture: 'resnet', 'alexnet', or 'vgg'

    Returns:
      None (results_dic is mutated in place)
    """
    # Iterate through all filenames in results_dic
    for filename, data in results_dic.items():
        # Build full image path safely
        image_path = os.path.join(images_dir, filename)

        # Get raw classifier label
        try:
            clf_label = classifier(image_path, model)
        except Exception:
            # If classifier errors (e.g., path issue), set empty label so checks continue
            clf_label = ''

        # Normalize classifier label: lower-case & strip whitespace
        clf_label = clf_label.lower().strip()

        # Compare: if pet label is found within classifier label terms -> match
        pet_label = data[0]
        match = 1 if pet_label in clf_label else 0

        # Append classifier label and match flag (index 1 and 2)
        data.extend([clf_label, match])
