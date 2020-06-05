#!/bin/env python
#-*- coding: utf-8 -*-

def printlog(logfile,search_word):
    f = open(logfile)
    logdata = f.read()
    f.close()

    index = logdata.find(search_word)

    if index >= 0 :
        print("-" * 70)
        print("Log file:" , logfile)
        print("Find this word: ", search_word)
        print(index)
        print("-" * 70)