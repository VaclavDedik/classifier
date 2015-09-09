# Classifier

This library is a nice interface around several python machine learning libraries. In particular:

* scikit-learn
* scipy
* numpy
* nltk

## Usage

First, you need to create a feature selector (StopWordsSelector, TFIDFSelector) and then feed the selector to the model you are going to use (e.g. SVM, NaiveBayes, CART...). For example:

    from classifier import selectors, models, kernels
    
    selector = selectors.TFIDFDecorator(selectors.StopWordsDecorator(selectors.BasicSelector()))
    model = models.SVM(feature_selector=selector, kernel=kernels.GaussianKernel(), C=20)

Thanks to the decorator design pattern, you can chain several feature extraction techniques into each other to get a desired combination of feature selection.

## Selectors

There is currently one concrete selector (BasicSelector) and several selector decorators. For example TFIDFDecorator, StopWordsDecorator, LSIDecorator or ChiSquaredDecorator. See classifier/selectors.py for documentation of the interface.

## Models

Only 3 models are currently implemented. NaiveBayesModel, SVMModel and CARTModel. There is also a BaselineModel that always predict the most common label. See classifier/models.py for more information and documentation of the interface.


