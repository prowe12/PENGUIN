#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:28:45 2023

@author: prowe
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# My modules
import path_params
import stats_params as prm
from make_plots import make_all_plots, print_stats, make_demo_plots, plot_demo
from clean import clean

# from make_plots import plot_test_v_control_bycourse


def extra_table():
    # Loop over students and see how each did
    # ipolar = ["Q5", "Q6", "Q7", "Q8", "Q10", "Q11", "Q12", "Q19"]
    ipolar = ["Q6", "Q8", "Q19"]
    istat = ["Q3", "Q4", "Q10", "Q13", "Q14", "Q15", "Q16"]
    corr_polar_bef = np.zeros(len(interv))
    corr_stat_bef = np.zeros(len(interv))
    corr_polar_aft = np.zeros(len(interv))
    corr_stat_aft = np.zeros(len(interv))
    for key, val in prm.KNOW.items():
        print(val["title"])
        corr = val["options"][val["icorrect"]]
        if key in ipolar:
            corr_polar_bef[interv[key + "_x"] == corr] += 1
            corr_polar_aft[interv[key + "_y"] == corr] += 1
        elif key in istat:
            corr_stat_bef[interv[key + "_x"] == corr] += 1
            corr_stat_aft[interv[key + "_y"] == corr] += 1
        # else:
        #     raise ValueError("missing a few")

    plt.figure()
    isort = np.argsort(interv["sid"])
    plt.plot(interv["sid"].iloc[isort], corr_stat_bef[isort])
    plt.plot(interv["sid"].iloc[isort], corr_stat_aft[isort])

    isort = np.argsort(corr_stat_aft)
    plt.figure()
    plt.plot(corr_stat_bef[isort])
    plt.plot(corr_stat_aft[isort])
    np.mean(corr_stat_aft)
    np.std(corr_stat_aft)

    isort = np.argsort(corr_polar_aft)
    plt.figure()
    plt.plot(corr_polar_bef[isort])
    plt.plot(corr_polar_aft[isort])
    plt.title("polar")

    plt.hist(100 * corr_polar_bef / len(ipolar), np.arange(-5, 100, 10))
    plt.hist(100 * corr_stat_bef / len(istat), np.arange(-5, 100, 10))

    randx = [random.random() * 0.3 for c in corr_stat_aft]
    randy = [random.random() * 0.3 for c in corr_stat_aft]
    plt.figure()
    plt.plot(corr_stat_bef + randx, corr_stat_aft + randy, "*")


# Clean the intervention (interv) and comparison (comp) data
# intervention => surveys of students who took the module
# comparison => surveys of students who did not take the modules
interv = clean(prm.FILES, prm.AGE, prm.KNOW, prm.DEMO, prm.QPRE, prm.QPOST)
comp = clean(
    prm.COMPFILES, prm.AGE, prm.KNOW, {}, prm.QPRE_COMP, prm.QPOST_COMP
)


print_stats(interv, comp, prm.POLARQS, prm.STATSQS, prm.KNOW)

# Choose the order of the questions
names = [
    "Q5",
    "Q7",
    "Q8",
    "Q6",
    "Q10",
    "Q11",
    "Q12",
    "Q19",
    "Q15",
    "Q13",
    "Q4",
    "Q3",
    "Q14",
    "Q16",
]
make_all_plots(interv, comp, prm, names, False, path_params.OUT_DIR)


# Demographics plots
plot_demo(interv, prm.DEMO, 1, False, path_params.OUT_DIR)


# Create plot about comfort with Rstudio


# Abandoned
# Get dataframes for each class
# intervs = []
# for files in prm.FILES:
#     intervs.append(
#         clean([files], prm.AGE, prm.KNOW, prm.DEMO, prm.QPRE, prm.QPOST)
#     )
# comps = [comp]
#
# for i in range(int(len(names) / 2)):
# i = 0
# plot_test_v_control_bycourse(interv, comp, prm, names[2 * i : 2 * (i + 1)], i)
#    plt.savefig(f"{outdir}/stats_knowledge_comp{i}.png")
