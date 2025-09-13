#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Rama Sab
# DATE CREATED: 2025-09-09
# REVISED DATE: 2025-09-13    
# PURPOSE: For each entry in results_dic, append:
#   index 3 -> 1/0 if PET label is-a-dog / is-not-a-dog
#   index 4 -> 1/0 if CLASSIFIER label is-a-dog / is-not-a-dog
# Using dog names loaded from dognames.txt (lowercased, stripped, one per line).

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts results_dic in-place to indicate if labels are dogs.

    Args:
        results_dic (dict): { filename: [pet_label, classifier_label, match_flag] }
        dogfile (str): path to dog names file (one name per line, lowercased)

    Returns:
        None (mutates results_dic)
    """
    # Load dog names into a fast-lookup dict (could also be a set)
    dognames_dic = {}
    with open(dogfile, 'r', encoding='utf-8') as f:
        for line in f:
            name = line.rstrip().lower()
            if not name:
                continue
            if name in dognames_dic:
                # Optional: warn about duplicates
                # print(f"** Warning: duplicate dog name in dogfile: {name}")
                pass
            else:
                dognames_dic[name] = 1

    # Update each result entry with pet_is_dog (idx 3) and clf_is_dog (idx 4)
    for _, vals in results_dic.items():
        pet_label = vals[0]
        clf_label = vals[1]

        # pet label check (exact match to a dog name)
        pet_is_dog = 1 if pet_label in dognames_dic else 0

        # classifier label may contain multiple comma-separated synonyms
        clf_terms = [t.strip() for t in clf_label.split(',') if t.strip()]
        clf_is_dog = 1 if any(term in dognames_dic for term in clf_terms) else 0

        vals.extend([pet_is_dog, clf_is_dog])
