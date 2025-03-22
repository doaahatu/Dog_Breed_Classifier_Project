def print_results(results, results_stats, model_name, print_incorrect_dogs, print_incorrect_breed):
    print(f"Results Summary for Model: {model_name}")
    print(f"Number of Images: {results_stats['n_images']}")
    print(f"Correctly Classified Dogs: {results_stats['n_correct_dogs']}")

    # Print incorrect dog classifications if requested
    if print_incorrect_dogs:
        print("Incorrectly Classified Dogs:")
        for key in results:
            if sum(results[key][3:]) == 1:  # Dog misclassified as not a dog or vice versa
                print(f"Misclassified Dog: {key}")
