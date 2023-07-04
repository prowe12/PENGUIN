#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:02:33 2023

@author: prowe
"""

try:
    import path_params

    MAINDIR = path_params.DATA_DIR
except:
    msg = "Create a file called path_params with DATA_DIR = '/path-to-data'"

    raise ValueError()

# File and question names
dir21 = MAINDIR + "results_2021_fall/"
DATA = [
    {
        "pre_file": dir21 + "climate_modeling_2021_fall_pre.xlsx",
        "post_file": dir21 + "climate_modeling_2021_fall_post_mod.xlsx",
        "pre": {
            "Q3": "sum",
            "Q4": "power",
            "Q6": "pdf",
            "Q7": "Arctic_change_2021",
            "Q9": "sid",
            "Q10": "month",
            "Q11": "day",
        },
        "post": {
            "Q3": "sum",
            "Q4": "power",
            "Q6": "pdf",
            "Q7": "Arctic_change_2021",
            "Q27": "sid",
            "Q28": "month",
            "Q29": "day",
        },
    },
    {
        "pre_file": MAINDIR + "results_2022_fall/ClimateModelingPre.xlsx",
        "post_file": MAINDIR + "results_2022_fall/ClimateModelingPost.xlsx",
        "pre": {
            "Q3": "pdf",
            "Q4": "Alaska_NOAA",
            "Q5": "warming_region",
            "Q6": "jet_stream",
            "Q7": "Arctic_change",
            "Q9": "sid",
            "Q10": "month",
            "Q11": "day",
        },
        "post": {
            "Q3": "pdf",
            "Q4": "Alaska_NOAA",
            "Q5": "warming_region",
            "Q6": "jet_stream",
            "Q7": "Arctic_change",
            "Q21": "sid",
            "Q22": "month",
            "Q23": "day",
        },
    },
]

# "Q6": "pdf",
# "Q7": "Alaska_NOAA",
# "Q8": "warming_region",
# "Q9": "jet_stream",
# "Q10": "Arctic_change",
# "Q21": "sid",
# "Q22": "month",
# "Q23": "day",


AGE = "Q1"

# knowledge questions
KNOW = {
    "pdf": {
        "title": "Probability density functions",
        "text": "Of the two probability density functions shown below, which "
        + "curve indicates a greater temperature variability?",
        "options": [
            "Blue",
            "Black",
            "Not sure",
        ],
        "labels": [
            "Blue",
            "Black",
            "Not sure",
        ],
        "icorrect": 0,
    },
    "Alaska_NOAA": {
        "title": "Alaska NOAA Station",
        "text": "Which site below refers to the location of a NOAA station "
        + "in Alaska?",
        "options": [
            "BLD",
            "BRW",
            "MLO",
            "SMO",
            "SPO",
            "SUM",
            "THD",
            "Not sure",
        ],
        "labels": [
            "BLD",
            "BRW",
            "MLO",
            "SMO",
            "SPO",
            "SUM",
            "THD",
            "Not sure",
        ],
        "icorrect": 1,
    },
    "warming_region": {
        "title": "Dataset from 2000s",
        "text": "The chart below displays two datasets from Alaska. One "
        + "refers the 1970s, and the other refers to the 2000s. Which "
        + "dataset refers to the 2000s?",
        "options": [
            "Dataset 1",
            "Dataset 2",
            "Not sure",
        ],
        "labels": [
            "Dataset 1",
            "Dataset 2",
            "Not sure",
        ],
        "icorrect": 0,
    },
    "jet_stream": {
        "title": "Cause of Jet Stream Meander",
        "text": "Increasing north-south meanders of the Jet Stream are "
        + "thought to be due to which cause?",
        "options": [
            "1. More warming over land, compared to oceans",
            "2. The reverse of (1.) (more warming over oceans compared to land)",
            "3. More warming in polar regions, compared to mid-latitudes",
            "4. The reverse of (3.) (more warming at mid-latitudes, compared to polar regions)",
            "5. Not sure",
        ],
        "labels": [
            "warming over land",
            "warming over ocean",
            "warming at poles",
            "warming mid-lats",
            "Not sure",
        ],
        "icorrect": 2,
    },
    "Arctic_change_2021": {
        "title": "Arctic climate change",
        "text": "Which best describes climate change in the Arctic?",
        "options": [
            "Warming is mostly in the winter and spring",
            "Warming is mostly in the summer and fall",
            "Summers have warmed, but winters have cooled slightly",
            "The Arctic's temperature has not significantly changed in recent decades",
            "Not sure",
        ],
        "labels": [
            "Warming winter/spring",
            "Warming summer/fall",
            "Summers warmed/winters cooled",
            "No change",
            "Not sure",
        ],
        "icorrect": 0,
    },
    # r"$\uparrow$summer/$\downarrow$winter",
    # "Arctic_change_2022": {
    #     "title": "Arctic climate change",
    #     "text": "Which best describes climate change in the Arctic?",
    #     "options": [
    #         "Warming is mostly in March and April",
    #         "Warming is mostly in the summer",
    #         "Summers have warmed, but winters have cooled slightly",
    #         "The Arctic's temperature has not significantly changed in recent decades",
    #         "Not sure",
    #     ],
    #     "labels": [
    #         "Warming Mar/Apr",
    #         "Warming in summer",
    #         "Warming summer / Cooling winter",
    #         "No change",
    #         "Not sure",
    #     ],
    #     "icorrect": 1,
    # },
    "sum": {
        "title": "Python sum",
        "text": "In Python, how would you print the sum of 5 and 3?",
        "options": [
            "result = 5+3, print(result)",
            "print(5+3)",
            "print(5 += 3)",
            "Not sure",
        ],
        "labels": [
            'r=5+3, print("r")',
            "print(5+3)",
            "print(5 += 3)",
            "Not sure",
        ],
        "icorrect": 1,
    },
    "power": {
        "title": "Python power",
        "text": "In Python, how do you raise a value to a power?",
        "options": [
            "5**2",
            "5^2",
            "Not sure",
        ],
        "labels": [
            "5**2",
            "5^2",
            "Not sure",
        ],
        "icorrect": 0,
    },
}
