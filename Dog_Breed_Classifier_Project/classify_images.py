# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function.
    
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                        and classifier labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet, alexnet, or vgg (string)
              
    Returns:
      None - results_dic is mutable, so no return needed.
    """
    for key in results_dic:
        # Obtain the full image path
        image_path = images_dir + key
        
        # Run classifier() on the image to get the predicted label (model_label)
        model_label = classifier(image_path, model)
        
        # Convert the classifier label to lowercase and strip leading/trailing whitespace
        model_label = model_label.lower().strip()
        
        # Get the pet image label from the results dictionary
        truth = results_dic[key][0]
        
        # Determine if the pet label is found in the classifier label string
        if truth in model_label:
            match = 1  # If match, set to 1
        else:
            match = 0  # If no match, set to 0
        
        # Append the classifier label and the match result (1 or 0) to the results dictionary
        results_dic[key].extend([model_label, match])
