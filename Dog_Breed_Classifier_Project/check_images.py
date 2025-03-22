#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Doaa Hatu
# DATE CREATED: 21 March 2025
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#
#          The program will evaluate the performance of three CNN architectures:
#          AlexNet, VGG, and ResNet. The true identity of the pet (or object) in
#          each image is inferred from the filename, and the classifications
#          will be compared with ground-truth labels to assess the model's accuracy.
#
# Command Line Arguments (Example Call):
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions to check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Measure total program runtime by collecting start time
    start_time = time()

    # Retrieve 3 command-line arguments as input: image directory, CNN model architecture, and dognames file
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Create results dictionary by extracting pet image labels from filenames
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    # Classify images and update results dictionary with classifier labels
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)    

    # Adjust results dictionary to mark images classified as 'a dog' or 'not a dog'
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # Calculate statistics from classification results
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    # Print results and allow options to print incorrectly classified dogs and breeds
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()

    # Compute overall runtime in seconds and print it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int(tot_time // 3600)) + ":" + str(int((tot_time % 3600) / 60)) + ":" + str(int((tot_time % 3600) % 60)))
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
