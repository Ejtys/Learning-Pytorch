import matplotlib.pyplot as plt

def plot_predictions(train_data, train_labels, test_data, test_labels, predictions = None):
    plt.scatter(train_data, train_labels, c="b", s=2, label="Training data")
    plt.scatter(test_data, test_labels, c="g", s=6, label="Testing data")
    if predictions:
        plt.scatter(test_data, predictions, c="r", s=6, label="Predictions")
    plt.legend()