#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:28:45 2023

@author: prowe
"""


# My modules
import path_params
import clim_modeling_params as param
from make_plots import make_all_plots_cm, print_stats_cm
from clean import clean_climate_modeling


# Clean the test (interv) data
interv = clean_climate_modeling(param)

print_stats_cm(interv)
# make_all_plots_cm(interv, True, path_params.OUT_DIR)
