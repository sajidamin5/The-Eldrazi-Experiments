import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random


'''
Citations (Platform, Model)

(Ollama, gemma3:1b)
🦴 Code Skellies 🦴
- compositions (a, b, c, composed_function)
'''
# takes a dictionary of labeled funtions as a parameter with no cap size
# this is not a new concept at all, I just am visualization optimzation of 
# multi national economics using mathematics -  Multimodal Function Optimizer
def MFO(a, b, c, d):
  # this is already abstracted/derived, like legitametly we either apply something from a 
  # a multivariable calc textbook or pump it through a model
  
  # TODO: the novelty may be optimizating classical or inorganic functions (0 byproduct)
  #       with 'quantum' or organic functions (>0 byproduct)
  functions = {"Entity 1" : composition(a), "Entity 2" : multivar(b, c), "Entity 3" : simple_mult(d)}  
  
  ret = 0
  for x in range(len(functions)):
    ret *= functions.values(x)
  return ret

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
    # grab the order and value index so we don't need multiple calls
    order = emotional_gradient[emotion][0]
    token_value = emotional_gradient[emotion][1]
    return MFO(token_value, token_value, order, random.randint(0, 69))

def simple_mult(x=0):
  """
  A simple function that takes a value and returns a result.
  """
  return x * 2  # Example: doubles the input

def simple_add(x):
  """
  A function that applies a function to an input.
  """
  return x + 1

def simple_frac(x):
  """
  A function that applies a function to an input.
  """
  return x / 3  # Example: multiplies the input by 3

def composition(x):
  """
  A composition of functions.  Applies function B to function C of input x.
  """
  return simple_frac(simple_add(simple_mult(x)))

def multivar(y, z):
  """
  A multivariable function.  Result of multivar conditions on params y and z
  """
  return composition(y) * simple_frac(y*z)


def a(x=0):
  """
  A simple function that takes a value and returns a result.
  """
  return x * 2  # Example: doubles the input

# functions_test = {"fn1" : a}
# functions_test2 = {"fn1" : a()}

# print(functions_test["fn1"])
# print(functions_test2["fn1"]) 

# Rage -> 1271 (non determenistic; pre factorization)
# Rage -> None (deterministic: post factorization) *probably a bug*
print(EmotionalTokenization("Rage"))