sys.path.append('/content/drive/MyDrive/utilize/')

from metrics import Metrics
from ml_logger import *


class RegressionMLLogger(MLLogger):

  def __init__(self, *args, **kwargs):
    super(RegressionMLLogger, self).__init__(*args, **kwargs)


  def fit_and_log(self,model, X_train, y_train, X_test, y_test,metrics=['mae', 'mse', 'rmse'],  custom_metric_names=None):
      model.fit(X_train, y_train)
      train_predictions = model.predict(X_train)
      test_predictions = model.predict(X_test)
      test_pred_prob = model.predict_proba(X_test)  # For ROC AUC

      metric_results = {}

      if custom_metric_names:
          for name in custom_metric_names:
              metric_func = self.custom_metrics[name]
              print(metric_func)
              train_metric = metric_func(y_train, train_predictions)
              test_metric = metric_func(y_test, test_predictions)
              metric_results[name] = {'train': train_metric, 'test': test_metric}

      for metric_name in metrics:
          if metric_name in self.metric_functions:
              metric_func = self.metric_functions[metric_name]
              if metric_name == 'roc_auc':
                  #test_metric = metric_func(y_test, test_pred_prob)
                  #metric_results[metric_name] = {'test': test_metric}
                  pass
              elif metric_name == 'confusion_matrix':
                  confusion_mat_tr = metric_func(y_train, train_predictions)
                  confusion_mat_te = metric_func(y_test, test_predictions)
                  metric_results[metric_name] = {'train': confusion_mat_tr, 'test': confusion_mat_te}
              else:
                  train_metric = metric_func(y_train, train_predictions)
                  test_metric = metric_func(y_test, test_predictions)
                  metric_results[metric_name] = {'train': train_metric, 'test': test_metric}
          else:
              raise ValueError(f"Invalid metric specified: {metric_name}")

      self._log_metrics(model, metric_results)
    