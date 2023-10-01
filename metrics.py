from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.metrics import mean_absolute_error, mean_squared_error

class Metrics:
    def __init__(self, y_true, y_pred, y_pred_prob=None):
        self.y_true = y_true
        self.y_pred = y_pred
        self.y_pred_prob = y_pred_prob

    def evaluate_accuracy(y_true, y_pred, y_pred_prob=None):
        return accuracy_score(y_true, y_pred)

    def evaluate_f1_score(y_true, y_pred, y_pred_prob=None):
        return f1_score(y_true, y_pred, average='weighted')

    def evaluate_roc_auc(y_true, y_pred, y_pred_prob=None):
        return roc_auc_score(y_true, y_pred_prob, multi_class='ovr')

    def evaluate_confusion_matrix(y_true, y_pred, y_pred_prob=None):
        return confusion_matrix(y_true, y_pred)

    def evaluate_mean_absolute_error(y_true, y_pred, y_pred_prob=None):
        return mean_absolute_error(y_true, y_pred)

    def evaluate_mean_squared_error(y_true, y_pred, y_pred_prob=None):
        return mean_squared_error(y_true, y_pred)

    def evaluate_root_mean_squared_error(y_true, y_pred, y_pred_prob=None):
        return mean_squared_error(y_true, y_pred, squared = False)