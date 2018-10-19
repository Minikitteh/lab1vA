#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:05:03 2018

@author: yamel
"""

class Node(object):
    #attributes
    password = ""
    count = -1
    next = None
    
    
    
    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next
        