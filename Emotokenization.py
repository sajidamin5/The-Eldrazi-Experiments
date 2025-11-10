import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def EmotionalTokenization(emotion=""): 
  
  # emotion exists, not on some infinite axis or continuum, rather a closed loop
  # emotion is still a primal/primitive pathway that we use as our rudder, sometimes for the better, sometimes worse
  # observationally, emotion works through myself in cyclic patterns/frequencies/rhythms. I'm not experiencing new ones,
  # rather, convolutions of the same few at varying levels of intesity
  # lets model this as some point in a circular queue
  
  # FORMAT # {emotion : [order, tokens] }
  # the values of the dictionary are meant to be dynamic variables for each given emotion
  e1 = {"Rage": [1, 22]}
  e2 = {"Love": [2, 18]}
  e3 = {"Glee": [3, 17]}
  e4 = {"Fear": [4, 9]}
  e5 = {"Guilt": [5, 6]}
  e6 = {"Grief": [6, 5]}
  e7 = {"Lust": [7, 10]}
  e8 = {"Shame": [8, 1]}
  
  emotional_gradient = deque([e1, e2, e3, e4, e5, e6, e7, e8])
  emotion = emotion.lower()

  if emotion in emotional_gradient:
    return 1
  else:
    return 0
    
