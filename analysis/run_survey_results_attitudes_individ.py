#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:44:31 2023

@author: prowe
"""

from survey_results_attitudes_individ import plot_before_after
import path_params

# Directories and files
maindir = path_params.DATA_DIR
outdir = maindir + "analysis/supplemental/"
statspostfile = "StatsPostSurvey.xlsx"


# Fall 2021 Stats
data_dir = maindir + "results_2021_fall/"
datafile = statspostfile
print(datafile)
outfile = "stats_post_2021_fall_"
# The data
befaft = {
    "title": "2021 Fall: Statistics",
    "cs": {
        "qbef": "Q20_1",
        "qaft": "Q20_2",
        "title": "Comfort with Rstudio",
    },
    "polarimport": {
        "qbef": "Q25_1",
        "qaft": "Q25_2",
    },
    "climateknowledge": {
        "qbef": "Q26_1",
        "qaft": "Q26_2",
    },
    "icecoreknowledge": {
        "qbef": "Q27_1",
        "qaft": "Q27_2",
    },
}
plot_before_after(befaft, data_dir + datafile, outdir + outfile)

# Spring 2022 Stats
data_dir = maindir + "results_2022_spring/"
datafile = statspostfile  # "Spring 2022 PENGUIN Statistics Knowledge Post-Survey Dataset.xlsx"
print(datafile)
outfile = "stats_post_2022_spring_"
# The data
befaft = {
    "title": "2022 Spring: Statistics",
    "cs": {
        "qbef": "Q20_1",
        "qaft": "Q20_2",
        "title": "Comfort with Rstudio",
    },
    "polarimport": {
        "qbef": "Q25_1",
        "qaft": "Q25_2",
    },
    "climateknowledge": {
        "qbef": "Q26_1",
        "qaft": "Q26_2",
    },
    "icecoreknowledge": {
        "qbef": "Q27_1",
        "qaft": "Q27_2",
    },
}
plot_before_after(befaft, data_dir + datafile, outdir + outfile)

# Fall 2022 Stats
data_dir = maindir + "results_2022_fall/"
datafile = statspostfile  # "Fall 2022 PENGUIN Statistics Knowledge Post-Survey Dataset.xlsx"
print(datafile)
outfile = "stats_post_2022_fall_"
# The data
befaft = {
    "title": "2022 Fall: Statistics",
    "cs": {
        "qbef": "Q20_1",
        "qaft": "Q20_2",
        "title": "Comfort with Rstudio",
    },
    "polarimport": {
        "qbef": "Q25_1",
        "qaft": "Q25_2",
    },
    "climateknowledge": {
        "qbef": "Q26_1",
        "qaft": "Q26_2",
    },
    "icecoreknowledge": {
        "qbef": "Q27_1",
        "qaft": "Q27_2",
    },
}
plot_before_after(befaft, data_dir + datafile, outdir + outfile)

# Fall 2021 modeling
data_dir = maindir + "results_2021_fall/"
datafile = "PENGUIN Climate Modeling Post-Survey Dataset.xlsx"
print(datafile)
outfile = "modeling_post_2021_fall_"
# The data
befaft = {
    "title": "2021 Fall: Climate Modelling",
    "cs": {
        "qbef": "Q9_1",
        "qaft": "Q9_2",
        "title": "Comfort with Python",
    },
    "polarimport": {
        "qbef": "Q14_1",
        "qaft": "Q14_2",
    },
}
plot_before_after(befaft, data_dir + datafile, outdir + outfile)

# Fall 2022 modeling
data_dir = maindir + "results_2022_fall/"
datafile = "Fall 2022 PENGUIN Climate Modeling Post-Survey Dataset_mod.xlsx"
print(datafile)
outfile = "modeling_post_2022_fall_"
# The data
befaft = {
    "title": "2022 Fall Climate Modeling",
    "polarimport": {
        "qbef": "Q11_1",
        "qaft": "Q11_2",
    },
    "climateknowledge": {
        "qbef": "Q12_1",
        "qaft": "Q12_2",
    },
}
plot_before_after(befaft, data_dir + datafile, outdir + outfile)
