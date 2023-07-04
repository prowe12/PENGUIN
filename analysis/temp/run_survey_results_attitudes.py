#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:32:57 2023

@author: prowe
"""


from analysis.survey_results_attitudes import combine_results, makefig

# makefigs

# Directories and files
maindir = "/Users/prowe/Sync/projects/NSF_PENGUIN/surveys/"
outdir = maindir + "analysis/"

# fl1 = "results_2021_fall/Statistics Knowledge Post-Survey Dataset.xlsx"
# fl2 = "results_2022_spring/Spring 2022 PENGUIN Statistics Knowledge Post-Survey Dataset.xlsx"
# fl3 = "results_2022_fall/Fall 2022 PENGUIN Statistics Knowledge Post-Survey Dataset.xlsx"

# Files containing the survey data for students who took the module
fl1 = "results_2021_fall/StatsPostSurvey_mod.xlsx"
fl2 = "results_2022_spring/StatsPostSurvey.xlsx"
fl3 = "results_2022_fall/StatsPostSurvey.xlsx"

# The data
data = [
    {
        "datafile": maindir + fl1,
        "climateknowledge": {
            "qbef": "Q26_1",
            "qaft": "Q26_2",
        },
        "cs": {
            "qbef": "Q20_1",
            "qaft": "Q20_2",
            "title": "Comfort with Rstudio",
        },
        "polarimport": {
            "qbef": "Q25_1",
            "qaft": "Q25_2",
        },
        "subjectknowledge": {
            "qbef": "Q27_1",
            "qaft": "Q27_2",
        },
        "ranking": {
            "qaft": "Q29",
        },
        "learnmore": {
            "qaft": "Q32",
        },
    },
    {
        "datafile": maindir + fl2,
        "climateknowledge": {
            "qbef": "Q26_1",
            "qaft": "Q26_2",
        },
        "cs": {
            "qbef": "Q20_1",
            "qaft": "Q20_2",
            "title": "Comfort with Rstudio",
        },
        "polarimport": {
            "qbef": "Q25_1",
            "qaft": "Q25_2",
        },
        "subjectknowledge": {
            "qbef": "Q27_1",
            "qaft": "Q27_2",
        },
        "ranking": {
            "qaft": "Q29",
        },
        "learnmore": {
            "qaft": "Q32",
        },
    },
    {
        "datafile": maindir + fl3,
        "climateknowledge": {
            "qbef": "Q26_1",
            "qaft": "Q26_2",
        },
        "cs": {
            "qbef": "Q20_1",
            "qaft": "Q20_2",
            "title": "Comfort with Rstudio",
        },
        "polarimport": {
            "qbef": "Q25_1",
            "qaft": "Q25_2",
        },
        "subjectknowledge": {
            "qbef": "Q27_1",
            "qaft": "Q27_2",
        },
        "ranking": {
            "qaft": "Q29",
        },
        "learnmore": {
            "qaft": "Q32",
        },
    },
]


savefigs = True  # Save the figures to outdir
org = combine_results(data)
# makefigs(org, outdir + "stats_post_totals_", savefigs)
makefig(org, outdir + "stats_attitudes", savefigs)
