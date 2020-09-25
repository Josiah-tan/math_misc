#================================================================
#
#   File name   : metrics.py
#   Author      : Josiah Tan
#   Created date: 21/07/2020
#   Description : evaluation metrics
#
#================================================================

#================================================================

import numpy as np

class Metrics:
    def __init__(self, labels, preds, preds_type = "binary_softmax", labels_type = "binary"):
      self.preds = preds
      self.labels = labels
      self.preds_type = preds_type
      self.labels_type = labels_type

      self._accuracy = None
      self._tp = None
      self._tn = None
      self._fp = None
      self._fn = None
      self._recall = None
      self._precision = None
      self._f1_score = None

      # change preds and labels appropriately
      self.preprocess()

    def preprocess(self):
      if self.preds_type == "binary_softmax" and self.labels_type == "binary":
        assert self.preds.shape[1] == 2
        self.preds = np.argmax(self.preds, axis = 1)
        assert self.preds.shape == self.labels.shape
  
    @property
    def accuracy(self):
      if self._accuracy is None:
        self._accuracy = np.squeeze(np.mean(self.preds == self.labels))
      return self._accuracy

    @property
    def tp(self):
      if self._tp is None:
        self._tp = np.sum(self.preds * self.labels) 
      return self._tp

    @property
    def tn(self):
      if self._tn is None:
        self._tn = np.sum((1 - self.preds) * (1 - self.labels))
      return self._tn
    
    @property
    def fp(self):
      if self._fp is None:
        self._fp = np.sum(self.preds) - self.tp
      return self._fp
    
    @property
    def fn(self):
      if self._fn is None:
        self._fn = np.sum(self.labels) - self.tp
      return self._fn
    
    @property
    def precision(self):
      if self._precision is None:
        if self.tp + self.fp == 0:
          self._precision = 1
        else:
          self._precision = self.tp / (self.tp + self.fp)
      return self._precision

    @property
    def recall(self):
      if self._recall is None:
        if self.tp + self.fn == 0:
          self._recall = 1
        else:
          self._recall = self.tp / (self.tp + self.fn)
      return self._recall
    
    @property
    def f1_score(self):
      if self._f1_score is None:
        if self.precision + self.recall == 0:
          self._f1_score = 0
        else: 
          self._f1_score = 2 * self.precision * self.recall / (self.precision + self.recall)
      return self._f1_score
if __name__ == '__main__':
  
  # for two binary output?
  preds = np.array([[1,0],[0,1],[0,1],[1,0],[0,1]])
  
  labels = np.array([0,1,0,1,0])

  metrics = Metrics(labels, preds, preds_type = "binary_softmax")
  print(metrics.f1_score)
  print(metrics.accuracy)
  print(metrics.recall)
  print(metrics.precision)
  
  #for single binary output
  preds = [0, 1, 1, 0, 1]
  metrics = Metrics(labels, preds, preds_type = "binary")
  print(metrics.f1_score)
  print(metrics.accuracy)
  print(metrics.recall)
  print(metrics.precision)
