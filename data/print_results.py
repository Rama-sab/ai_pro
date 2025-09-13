#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Rama Sab
# DATE CREATED: 2025-09-09
# REVISED DATE:2025-09-13
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints a summary of the results (counts + percentages), and optionally
    the misclassified dog/not-dog images and misclassified dog breeds.

    Args:
        results_dic (dict): {filename: [pet_label, classifier_label, match, pet_is_dog, clf_is_dog]}
        results_stats_dic (dict): computed stats (counts + percentages)
        model (str): cnn architecture used ('resnet' | 'alexnet' | 'vgg')
        print_incorrect_dogs (bool): if True, list dog/not-dog mistakes
        print_incorrect_breed (bool): if True, list breed mistakes
    """
    # --- Header ---
    model_name = model.upper() if isinstance(model, str) else "(UNSPECIFIED)"
    print(f"\n\n*** Results Summary for CNN Model Architecture: {model_name} ***")

    # --- Core counts (same across all models for the same dataset) ---
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of 'Not-a-Dog' Images: {results_stats_dic['n_notdogs_img']}")

    # --- Percentages (print all keys that start with 'pct_' in a tidy order) ---
    pct_keys = sorted(k for k in results_stats_dic.keys() if k.startswith('pct_'))
    print("")  # blank line
    for k in pct_keys:
        label = {
            'pct_match': "% Match",
            'pct_correct_dogs': "% Correct Dogs",
            'pct_correct_breed': "% Correct Breed",
            'pct_correct_notdogs': "% Correct 'Not-a-Dog'",
        }.get(k, k)
        print(f"{label}: {results_stats_dic[k]:.1f}")

    # --- Misclassified Dogs (one label says dog, the other says not-dog) ---
    # Only print if user asked AND mistakes exist:
    # mistakes exist when n_correct_dogs + n_correct_notdogs != n_images
    if print_incorrect_dogs and (
        results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']
        != results_stats_dic['n_images']
    ):
        print("\nINCORRECT Dog/Not-Dog Assignments:")
        any_bad = False
        for fname, vals in results_dic.items():
            # vals[3] + vals[4] == 1  --> disagreement: exactly one says dog
            if sum(vals[3:5]) == 1:
                any_bad = True
                print(f"  {fname}: pet='{vals[0]}'  vs  clf='{vals[1]}'"
                      f"  [pet_is_dog={vals[3]} clf_is_dog={vals[4]}]")
        if not any_bad:
            print("  None.")

    # --- Misclassified Breeds (both agree it's a dog, but breed mismatch) ---
    # Only print if user asked AND such mistakes exist:
    if print_incorrect_breed and (
        results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']
    ):
        print("\nINCORRECT Dog Breeds:")
        any_bad = False
        for fname, vals in results_dic.items():
            # Both dog (sum==2) but labels don't match (vals[2]==0)
            if sum(vals[3:5]) == 2 and vals[2] == 0:
                any_bad = True
                print(f"  {fname}: pet='{vals[0]}'  vs  clf='{vals[1]}'")
        if not any_bad:
            print("  None.")

                
