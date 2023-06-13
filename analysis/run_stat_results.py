#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:28:45 2023

@author: prowe
"""


# My modules
import path_params
import stats_params as param
from make_plots import make_all_plots, print_stats, make_demo_plots
from clean import clean


# Clean the test (interv) and comparison (control) data
interv = clean(param)
param.FILES = param.COMPFILES
param.QPRE = param.QPRE_COMP
param.QPOST = param.QPOST_COMP
comp = clean(param)

make_demo_plots(interv, False, path_params.OUT_DIR)
# print_stats(interv, comp)
# make_all_plots(interv, comp, False, path_params.OUT_DIR)
