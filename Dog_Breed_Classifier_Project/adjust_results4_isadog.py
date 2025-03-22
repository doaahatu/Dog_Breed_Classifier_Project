#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List containing:
                      index 0 = pet image label (string)
                      index 1 = classifier label (string)
                      index 2 = 1/0 (int) for label match (1) or not (0)
                      NEW - index 3 = 1/0 (int) - pet label 'is-a-dog' (1) or 'not-a-dog' (0)
                      NEW - index 4 = 1/0 (int) - classifier label 'is-a-dog' (1) or 'not-a-dog' (0)
                      
     dogfile - A text file containing dog names (1 per line)
               Dog names may have multiple variants, separated by commas.
    
    Returns:
           None - results_dic is mutable, modified in-place.
    """
    dognames_dic = {}
    
    # Reads dognames from file and stores them as keys in dognames_dic.
    with open(dogfile, "r") as infile:
        for line in infile:
            dogname = line.strip()  # Remove newline characters
            dognames_dic[dogname] = 1  # Add dogname to dictionary with value 1

    # Iterate through results_dic and update indices [3] and [4]
    for key in results_dic:
        # Check if pet image label and classifier label match dog names
        pet_label_is_dog = 1 if results_dic[key][0] in dognames_dic else 0
        classifier_label_is_dog = 1 if results_dic[key][1] in dognames_dic else 0
        
        # Append the dog/not-dog status to the list
        results_dic[key].extend((pet_label_is_dog, classifier_label_is_dog))
