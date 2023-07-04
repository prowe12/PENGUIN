#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:28:45 2023

@author: prowe
"""

import pandas as pd

# My modules
import path_params
import clim_modeling_params as prm
from make_plots import make_all_plots_cm, print_stats_cm
from clean import clean_climate_modeling, clean_single_cm
from clean import clean_single_cm_ignore_id
from analysis_resources import get_num_correct, get_fisher


# Clean the test (interv) data
# interv = clean_climate_modeling(prm)
# print_stats_cm(interv, prm)
# make_all_plots_cm(interv, prm, False, path_params.OUT_DIR)


# Repeat the above but for all cases
# Get the pre and post
pre_res = []
post_res = []
for group in prm.DATA:
    print(group["pre_file"])
    pre = clean_single_cm_ignore_id(group["pre_file"], prm.AGE, group["pre"])
    print(group["post_file"])
    post = clean_single_cm_ignore_id(
        group["post_file"], prm.AGE, group["post"]
    )

    # Merge into one big dataframe and return
    pre_res.append(pre)
    post_res.append(post)

pre_res = pd.concat(pre_res)
post_res = pd.concat(post_res)
# print("\n\n, Correct,, Change, n, Odds, P")
print()
print(
    "Question, Before (%), After (%), Change (pts), n Bef, n Aft, odds, pvalue"
)
# ", (%), , Ratio, ")
for key, name in prm.KNOW.items():
    corr = prm.KNOW[key]["options"][prm.KNOW[key]["icorrect"]]
    bef_corr, bef_wrong = get_num_correct(pre_res[key], corr)
    aft_corr, aft_wrong = get_num_correct(post_res[key], corr)
    # befpc, aftpc, chg, nstud, odds, pval = getstats(interv, key, corr)
    # print(f"{key}, {befpc}, {aftpc}, {chg}, {nstud}, {odds}, {pval}")
    nbef = bef_corr + bef_wrong
    naft = aft_corr + aft_wrong
    pcbef = round(100 * bef_corr / nbef)
    pcaft = round(100 * aft_corr / naft)
    chg = pcaft - pcbef
    odds, pval = get_fisher(bef_corr, bef_wrong, aft_corr, aft_wrong)

    print(f"{key}, {pcbef}, {pcaft}, {chg}, {nbef}, {naft}, {odds}, {pval}")
