def accuracy(predictions: list, test_labels: list) -> float:
    """
    Test Model-Prediction <==> Test Label Correspondence
    """
    # Finding number of matching predictions
    number_of_matching_predictions = 0
    
    # Adding to number of matching predictions
    for i in range(len(predictions)):
        if (predictions[i] == test_labels[i]):
            number_of_matching_predictions += 1
    
    # Returning proportion of matching predictions
    return number_of_matching_predictions / len(predictions) 

# This is the actual solution
def model_predict(train_data: dict, train_labels: list, test_data: dict) -> list:
    """
    This is the actual solution! 

    Given a list of training data, training labels, and test 
    data,build your own algorithm that returns a list of 
    predictions.
    """
    # Getting data that forms a meaningful pattern, AKA signal
    temp_faren_list = test_data["temp_faren"]
    bottles_list = test_data["water_bottles_finished"]

    # Defining predicted decision boundary
    DECISION_BOUNDARY_TEMPERATURE = 80
    DECISION_BOUNDARY_BOTTLES = 5

    # Creating a predictions list
    predictions = []

    # Making predictions
    for i in range(len(temp_faren_list)):
        # Mr. Jackson always fails when hotter than 80 degrees
        if temp_faren_list[i] > DECISION_BOUNDARY_TEMPERATURE:
            predictions.append(False)
        # Mr. Jackson also fails when he drinks > 5 bottles
        elif bottles_list[i] > DECISION_BOUNDARY_BOTTLES:
            predictions.append(False)
        else:
            # Otherwise he seems to succeed
            predictions.append(True)
            
    # Returning predictions
    return predictions


# Defining training and test data and labels
train_data = {"temp_faren": [70, 65, 95, 88, 64, 73], 
              "water_bottles_finished": [3, 3, 5, 6, 7, 9],
               "number_of_memes_clicked": [22, 11, 7, 36, 44, 5]}

train_labels = [True, True, False, False, False, False]


test_data = {"temp_faren": [75, 72, 82, 85, 88, 64], 
              "water_bottles_finished": [4, 3, 8, 5, 6, 2],
               "number_of_memes_clicked": [11, 67, 53, 24, 48, 32]}
test_labels = [True, True, False, False, False, True]

# Predicting test labels model trained on train_data
try:
    # Getting output predictions from model
    predictions: list = model_predict(train_data, train_labels, 
    test_data)

    # Computing training accuracy
    training_accuracy = accuracy(model_predict(train_data,  
    train_labels, train_data), train_labels)

    # Displaying training prediction, ensuring model fit properly
    print(f"training accuracy {training_accuracy}")
    assert training_accuracy >= 0.8, """Model did not perform
    sufficiently"""
# If error with model
except:
    print("Model errored out")

# Computing accuracy (done for you)
acc = accuracy(predictions, test_labels)

# Displaying test set predictions and accuracy
print(f"model predictions: {predictions}")
print("test set accuracy: {:0.2f}".format(acc))

# Ensuring model fit properly
assert acc >= 0.8, "Model did not perform sufficiently"
print("Model successfully exceeded 80% accuracy!")