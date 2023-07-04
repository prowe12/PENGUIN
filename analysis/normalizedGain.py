#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:45:36 2023

Grade the two data files from PENGUIN after running run_stat_results

@author: michaeltown
"""

# libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import stats_params as param
import path_params
from clean import clean


# Clean the test (interv) and comparison (control) data
interv = clean(param)
param.FILES = param.COMPFILES
param.QPRE = param.QPRE_COMP
param.QPOST = param.QPOST_COMP
comp = clean(param)



# eval questions q3 - q19 using param.KNOW icorrect for correct answer
# assume that the first set of answers (_x) is the pre, the second set of answers (_y) is the 
# post

# databases are comp and interv

ks = param.KNOW.keys()
cols = ks
compEvalPre = pd.DataFrame(columns = cols)
compEvalPost = pd.DataFrame(columns  = cols)
intervEvalPre = pd.DataFrame(columns = cols)
intervEvalPost = pd.DataFrame(columns = cols)


# loop through the data to grade
for k in ks:
    corAnsInd = param.KNOW[k]['icorrect']
    compEvalPre[k] = comp[k+'_x'].apply(lambda x: 1 if x == param.KNOW[k]['options'][corAnsInd] else 0)
    compEvalPost[k] = comp[k+'_y'].apply(lambda x: 1 if x == param.KNOW[k]['options'][corAnsInd] else 0)
    intervEvalPre[k] = interv[k+'_x'].apply(lambda x: 1 if x == param.KNOW[k]['options'][corAnsInd] else 0)
    intervEvalPost[k] = interv[k+'_y'].apply(lambda x: 1 if x == param.KNOW[k]['options'][corAnsInd] else 0)
    
# scores, 14 columns
compEvalPre['score'] = compEvalPre.sum(axis = 1)/14
compEvalPost['score'] = compEvalPost.sum(axis = 1)/14
intervEvalPre['score'] = intervEvalPre.sum(axis = 1)/14
intervEvalPost['score'] = intervEvalPost.sum(axis = 1)/14

compEvalPost['normGain'] = (compEvalPost.score-compEvalPre.score)/(1-compEvalPre.score)
intervEvalPost['normGain'] = (intervEvalPost.score-intervEvalPre.score)/(1-intervEvalPre.score)

# print stats

print('***************')
print('comp group: ')
print('mean pre score: ' + str(np.round(compEvalPre.score.mean(),2))  )
print('mean post score: ' + str(np.round(compEvalPost.score.mean(),2))  )
print('mean normalized gain: ' + str(np.round(compEvalPost.normGain.mean(),2))  )
print('***************')
print('interv group: ')
print('mean pre score: ' + str(np.round(intervEvalPre.score.mean(),2))  )
print('mean post score: ' + str(np.round(intervEvalPost.score.mean(),2))  )
print('mean normalized gain: ' + str(np.round(intervEvalPost.normGain.mean(),2))  )
print('***************')




# 

