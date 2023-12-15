#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:50:08 2023

@author: sammy

Python assignment, Question1
"""

def stack(*arguments):
  result = arguments[0]
  
  if arguments[1] == "add":
  	arguments[0].insert(0, arguments[2])
  elif arguments[1] == "remove":
  	arguments[0].pop(0)
  return result
  
    
def queue(*arguments):
  result = arguments[0]
  if arguments[1] == "add":
  	arguments[0].append(arguments[2])
  elif arguments[1] == "remove":
  	arguments[0].pop(0)    
  return result;
  
    

new_list = [1, 2, 3, 4]
print("Adding new element to the stack")
new_list = stack(new_list, 'add', 0)
print (new_list)
print("Adding remove an element from stack")
new_list = stack(new_list, 'remove')
print (new_list)
print ("Adding new element to the queue")
new_list = queue (new_list, 'add', 5)
print (new_list)
print("Adding remove and element from the queue")
new_list = queue (new_list, 'remove')
print(new_list)