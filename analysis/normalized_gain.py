#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:45:36 2023

Grade the two data files from PENGUIN after running run_stat_results

@author: michaeltown
Updated by prowe
"""

# libraries
import pandas as pd
import numpy as np


# Our modules
import stats_params as prm
from clean import clean


# Clean the test (interv) and comparison (control) data
interv = clean(prm.FILES, prm.AGE, prm.KNOW, prm.DEMO, prm.QPRE, prm.QPOST)
comp = clean(
    prm.COMPFILES, prm.AGE, prm.KNOW, {}, prm.QPRE_COMP, prm.QPOST_COMP
)


# eval questions q3 - q19 using param.KNOW icorrect for correct answer
# _x is the pre, _y is the post


know_keys = prm.KNOW.keys()
cols = know_keys
comp_pre = pd.DataFrame(columns=cols)
comp_post = pd.DataFrame(columns=cols)
interv_pre = pd.DataFrame(columns=cols)
interv_post = pd.DataFrame(columns=cols)


# loop through the data to grade
# Students get a 1 for a correct answer, 0 for incorrect
for k in know_keys:
    icor = prm.KNOW[k]["icorrect"]
    cor = prm.KNOW[k]["options"][icor]  # correct answer
    comp_pre[k] = comp[k + "_x"].apply(lambda x: 1 if x == cor else 0)
    comp_post[k] = comp[k + "_y"].apply(lambda x: 1 if x == cor else 0)
    interv_pre[k] = interv[k + "_x"].apply(lambda x: 1 if x == cor else 0)
    interv_post[k] = interv[k + "_y"].apply(lambda x: 1 if x == cor else 0)

# mean student score for questions, for each student
ncols = len(cols)
comp_pre["score"] = comp_pre.sum(axis=1) / ncols
comp_post["score"] = comp_post.sum(axis=1) / ncols
interv_pre["score"] = interv_pre.sum(axis=1) / ncols
interv_post["score"] = interv_post.sum(axis=1) / ncols

comp_post["normgain"] = (comp_post.score - comp_pre.score) / (
    1 - comp_pre.score
)
interv_post["normgain"] = (interv_post.score - interv_pre.score) / (
    1 - interv_pre.score
)

# print stats
print("\n***************")
print("comp group: ")
print("mean pre score: " + str(np.round(comp_pre.score.mean(), 2)))
print("mean post score: " + str(np.round(comp_post.score.mean(), 2)))
print("mean normalized gain: " + str(np.round(comp_post.normgain.mean(), 2)))
print("***************")
print("interv group: ")
print("mean pre score: " + str(np.round(interv_pre.score.mean(), 2)))
print("mean post score: " + str(np.round(interv_post.score.mean(), 2)))
print("mean normalized gain: " + str(np.round(interv_post.normgain.mean(), 2)))
print("***************")
