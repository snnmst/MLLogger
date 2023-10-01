# MLLogger

## Overview

The ML Logging Class is a Python library that simplifies the process of logging and tracking machine learning experiments. It helps data scientists and machine learning engineers keep a record of model training runs, hyperparameters, evaluation metrics, and more. This README.md provides an overview of the ML Logging Class and how to use it effectively.

## Features

- Log machine learning experiments to a CSV or Excel file.
- Record key information including model type, hyperparameters, and evaluation metrics.
- Support for custom evaluation metrics and interpretation of model fit.
- Easily integrate with popular machine learning libraries like scikit-learn and TensorFlow.

## Getting Started

![Sample output of logger class](https://github.com/snnmst/MLLogger/blob/main/ml_logger.png?raw=true)


### Installation

To use the ML Logging Class, you can install it via pip:

```bash
pip install ml-logging-class
Basic Usage
Here is a simple example of how to use the ML Logging Class:

python

# Library Import
import cls_logger
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Dummy Classification Dataset
X,y = make_classification(n_samples = 1000, n_features = 20, random_state=42)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 42)


# Initialize the logger
logger = cls_logger.ClassificationMLLogger('MLLogger_v1')

# Initialize Logistic Regression Model
model = LogisticRegression()

# Fit a machine learning model and log the results
logger.fit_and_log(model, X_train, y_train, X_test, y_test)
```

Documentation
For detailed usage instructions and additional features, please refer to the Documentation.

Examples
We've provided several example notebooks in the Examples directory to demonstrate how to use the ML Logging Class in different machine learning scenarios.

Contributing
Contributions are welcome! Please read our Contributing Guidelines for details on how to contribute to this project.

License
This project is licensed under the Apache License 2.0  - see the LICENSE file for details.

Acknowledgments
We would like to thank the open-source community for their contributions and support in making this project possible.



