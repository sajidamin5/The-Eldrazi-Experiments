import numpy as np
import matplotlib.pyplot as plt
from collections import deque


'''
Citations (Platform, Model)

(Ollama, gemma3:1b)
🦴 Code Skellies 🦴
- compositions (a, b, c, composed_function)
'''

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

# takes a dictionary of labeled funtions as a parameter with no cap size
# this is not a new concept at all, I just am visualization optimzation of 
# multi national economics using mathematics

def MultimodalFunctionOptimzation(functions={}):
  # this is already abstracted/derived, like legitametly we either apply something from a 
  # a multivariable calc textbook or pump it through a model
  
  # TODO: the novelty may be optimizating classical or inorganic functions (0 byproduct)
  #       with 'quantum' or organic functions (>0 byproduct)
  functions = {"Country 1" : composition(), "Country 2" : multivar(), "Country 3" : a()}  
  return 777

def a(x=0):
  """
  A simple function that takes a value and returns a result.
  """
  return x * 2  # Example: doubles the input

def b(x):
  """
  A function that applies a function to an input.
  """
  return x + 1

def c(x):
  """
  A function that applies a function to an input.
  """
  return x * 3  # Example: multiplies the input by 3

def composition(x):
  """
  A composition of functions.  Applies function B to function C of input x.
  """
  return b(c(x))

def multivar(y, z):
  """
  A multivariable function.  Result of multivar conditions on params y and z
  """
  return y * z


def a(x=0):
  """
  A simple function that takes a value and returns a result.
  """
  return x * 2  # Example: doubles the input

# functions_test = {"fn1" : a}
# functions_test2 = {"fn1" : a()}

# print(functions_test["fn1"])
# print(functions_test2["fn1"])