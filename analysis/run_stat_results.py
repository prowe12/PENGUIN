#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:28:45 2023

@author: prowe
"""


# My modules
import path_params
import stats_params as prm
from make_plots import make_all_plots, print_stats, make_demo_plots
from clean import clean


# Clean the intervention (interv) and comparison (comp) data
# intervention => surveys of students who took the module
# comparison => surveys of students who did not take the modules
interv = clean(prm.FILES, prm.AGE, prm.KNOW, prm.QPRE, prm.QPOST)
comp = clean(prm.COMPFILES, prm.AGE, prm.KNOW, prm.QPRE_COMP, prm.QPOST_COMP)

make_demo_plots(interv, False, path_params.OUT_DIR)
print_stats(interv, comp)
make_all_plots(interv, comp, False, path_params.OUT_DIR)
