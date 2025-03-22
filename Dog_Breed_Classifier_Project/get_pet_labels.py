import os

def get_pet_labels(image_dir):
    results_dict = {}

    # Get all filenames from the given directory
    filenames = os.listdir(image_dir)

    for filename in filenames:
        # Skip hidden files like .DS_Store
        if filename[0] != '.':
            # Extract pet label from filename
            label = ' '.join([word.lower() for word in filename.split('_') if word.isalpha()])
            results_dict[filename] = [label]
    
    return results_dict
