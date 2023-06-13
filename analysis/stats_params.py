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

# Directories and files
FILES = [
    {
        "pre_file": MAINDIR + "results_2021_fall/StatsPreSurvey.xlsx",
        "post_file": MAINDIR + "results_2021_fall/StatsPostSurvey.xlsx",
    },
    {
        "pre_file": MAINDIR + "results_2022_spring/StatsPreSurvey.xlsx",
        "post_file": MAINDIR + "results_2022_spring/StatsPostSurvey.xlsx",
    },
    {
        "pre_file": MAINDIR + "results_2022_fall/StatsPreSurvey.xlsx",
        "post_file": MAINDIR + "results_2022_fall/StatsPostSurvey.xlsx",
    },
]

COMPFILES = [
    {
        "pre_file": MAINDIR + "results_2021_fall/StatsCompPreSurvey.xlsx",
        "post_file": MAINDIR + "results_2021_fall/StatsCompPostSurvey.xlsx",
    },
]
# TODO: replace this above
#         "post_file": MAINDIR + "results_2021_fall/StatsCompPostSurvey.xlsx",


QPRE = {"Q20": "sid", "Q21": "month", "Q22": "day"}
QPOST = {"Q38": "sid", "Q39": "month", "Q40": "day"}

QPRE_COMP = {"Q20": "sid", "Q21": "month", "Q22": "day"}
QPOST_COMP = {"Q20": "sid", "Q21": "month", "Q22": "day"}

AGE = "Q1"

KNOW = {
    "Q3": {
        "title": "Prediction outside the range",
        "text": "1. Suppose we use a linear regression equation to estimate "
        + "the relationship between a response variable and an explanatory "
        + "variable, and that we also determine that the samples of these "
        + "two variables have a high correlation. We then use the regression "
        + "equation to predict the value of the response variable when the "
        + "explanatory variable is well outside the range of the values we "
        + "observed for it. This is an example of:",
        "options": [
            "Interpolation, and it is a reliable prediction.",
            "Interpolation, and it is not a reliable prediction.",
            "Extrapolation, and it is a reliable prediction.",
            "Extrapolation, and it is not a reliable prediction.",
            "Not sure",
        ],
        "labels": [
            "interp/reliable",
            "interp/unrel.",
            "extrap/reliable",
            "extrap/unrel.",
            "not sure",
        ],
        "icorrect": 3,
    },
    "Q4": {
        "title": "Ave relationship between x and y",
        "text": "Which statistical method would be appropriate for assessing "
        + "the average relationship between the value of a response variable "
        + "and the value of a numerical explanatory variable?",
        "options": [
            "Two sample t-test",
            "Chi-squared test of association",
            "Simple linear regression",
            "Matched pair t-test",
            "Not sure",
        ],
        "labels": [
            "Two sample t-test",
            "Chi-squared test",
            "Linear regression",
            "Match pair t-test",
            "Not sure",
        ],
        "icorrect": 2,
    },
    "Q5": {
        "title": "Fastest-warming region",
        "text": "3. Over the last 100 years, which region has warmed the "
        + "fastest due to climate change?",
        "options": [
            "Polar regions",
            "Mid-latitudes",
            "Tropical / equatorial",
            "Not sure",
        ],
        "labels": [
            "Polar regions",
            "Mid-latitudes",
            "Tropical",
            "Not sure",
        ],
        "icorrect": 0,
    },
    "Q6": {
        "title": "Length ice core record (years)",
        "text": "4. The longest time range for which climate scientists have "
        + "obtained useful information from ice cores is on the order of",
        "options": [
            "Hundreds of years.",
            "Thousands of years.",
            "About a million years.",
            "Hundreds of millions of years.",
            "Not sure",
        ],
        "labels": [
            "hundreds",
            "thousands",
            "about a million",
            "100s of millions",
            "Not sure",
        ],
        "icorrect": 2,
    },
    "Q7": {
        "title": "Reconstructing past temperatures",
        "text": "In reconstructing the temperature record of past climates, "
        + "scientists mainly use the following feature of the ice core...",
        "options": [
            "The temperature of the ice as a function of depth.",
            "The isotopic composition of the ice.",
            "Tiny air pockets in the ice.",
            "Not sure",
        ],
        "labels": [
            "Temperature",
            "Isotopic Comp.",
            "Air pockets",
            "Not sure",
        ],
        "icorrect": 1,
    },
    "Q8": {
        "title": "Last million years was mostly...",
        "text": "Over the last few million years, Earth’s transitions to/from "
        + "'ice age' conditions were such that",
        "options": [
            "Most time was spent in ice ages, with occasional short warm "
            + "periods like the present.",
            "Most time was spent in warm periods like the present, "
            + "occasionally dipping into brief ice ages.",
            "About equal time was spent in warm periods as in ice ages.",
            "Not sure",
        ],
        "labels": [
            "Ice ages",
            "Warm periods",
            "Both",
            "Not sure",
        ],
        "icorrect": 0,
    },
    "Q10": {
        "title": "ID plot of Ice core record",
        "text": "The label a (blue circles) corresponds to:",
        "options": [
            "Modern Polar (Arctic research station at Utqiagvik)",
            "Modern Global",
            "Ice Core Record",
        ],
        "labels": [
            "Modern Polar",
            "Modern Global",
            "Ice Core Rec.",
        ],
        "icorrect": 2,
    },
    "Q11": {
        "title": "ID plot of modern polar",
        "text": "The label b (green triangles) corresponds to:",
        "options": [
            "Modern Polar (Arctic research station at Utqiagvik)",
            "Modern Global",
            "Ice Core Record",
        ],
        "labels": [
            "Modern Polar",
            "Modern Global",
            "Ice Core Rec.",
        ],
        "icorrect": 0,
    },
    "Q12": {
        "title": "ID plot of modern global",
        "text": "The label c (orange x's) corresponds to:",
        "options": [
            "Modern Polar (Arctic research station at Utqiagvik)",
            "Modern Global",
            "Ice Core Record",
        ],
        "labels": [
            "Modern Polar",
            "Modern Global",
            "Ice Core Rec.",
        ],
        "icorrect": 1,
    },
    "Q13": {
        "title": "No, moderate, perfect linear assoc.",
        "text": "The sample correlation, r, is a measure of strength of "
        + "linear association. Which values of r would represent (in order): "
        + "no linear association, moderate linear association, and perfect "
        + "linear assocation?",
        "options": ["0, 0.8, 1", "1, 0.8, 0", "-1, 0.8, 1", "Not sure"],
        "labels": ["0, 0.8, 1", "1, 0.8, 0", "-1, 0.8, 1", "Not sure"],
        "icorrect": 0,
    },
    "Q14": {
        "title": "Use of linear regression",
        "text": "For an explanatory and response variable showing a strong "
        + "linear association in their observed values, which of the "
        + "following is an appropriate use of a simple linear regression "
        + "model?",
        "options": [
            "Interpolation",
            "Extrapolation",
            "Interpolation and extrapolation",
            "Neither interpolation nor extrapolation",
            "Not sure",
        ],
        "labels": [
            "Interp",
            "Extrap",
            "Both",
            "Neither",
            "Not sure",
        ],
        "icorrect": 0,
    },
    "Q15": {
        "title": "Negative linear association",
        "text": "Choose the scatterplot that is best described as having a "
        + "moderately strong, negative, linear association between the two "
        + "variables",
        "options": [
            "IM1GGZAho7mJAA2zk",
            "IM6PD6XHpBMhIvSWa",
            "IMd0d8cb3PVxp1K50",
            "IMcOwiJHQQ0iCRLbU",
            "Not sure",
        ],
        "labels": ["a", "b", "c", "d", "Not sure"],
        "icorrect": 0,
    },
    "Q16": {
        "title": "Evidence of causation",
        "text": "Which of the following gives strong evidence of causation?",
        "options": [
            "A strong correlation between two variables.",
            "A strong positive correlation between two variables.",
            "A physical model of causation that predicts beforehand what is "
            + "later observed.",
            "None of the above.",
            "Not sure",
        ],
        "labels": ["Strong", "Strong +", "Model", "None", "Not sure"],
        "icorrect": 2,
    },
    "Q19": {
        "title": "Main cause of polar amplification",
        "text": "Which is currently believed to be the strongest contributor "
        + "to polar amplification?",
        "options": [
            "Colder polar air retains more CO2, causing an enhanced "
            + "greenhouse effect over polar regions.",
            "Polar regions receive more sunlight during the summers and less "
            + "during the winters. These extremes amplify climate change "
            + "compared to the global average.",
            "As warming melts sea ice, sunlight is no longer reflected but "
            + "instead heats the ocean.",
            "In our current phase of the orbital cycles, the sun is slightly "
            + "closer to the Arctic during summer, amplifying warming.",
            "Thawing permafrost releases methane, a strong greenhouse gas.",
            "Not sure",
        ],
        "labels": [
            "Polar greenhouse",
            "Polar sunlight",
            "Sea ice melt",
            "Orbital Cycle",
            "Permafrost thaw",
            "Not sure",
        ],
        "icorrect": 2,
    },
}

DEMO = {
    "Q33": {
        "title": "STEM major?",
        "text": "Are you a science, technology, engineering or math major?",
        "options": [
            "Yes",
            "No",
            "Maybe",
        ],
        "labels": [
            "Yes",
            "No",
            "Maybe",
        ],
    },
    "Q34": {
        "title": "Considering STEM?",
        "text": "Are you considering a science, technology, engineering, or math major?",
        "options": [
            "Yes",
            "No",
            "Maybe",
        ],
        "labels": [
            "Yes",
            "No",
            "Maybe",
        ],
    },
    "Q35": {
        "title": "Gender Identity",
        "text": "What is your gender identity? (Check all that apply)",
        "options": [
            "Woman",
            "Man",
            "Other",
        ],
        "labels": [
            "Woman",
            "Man",
            "Other",
        ],
    },
    "Q36": {
        "title": "Race/Ethnicity",
        "text": "What is your race/ethnicity? (Check all that apply)",
        "options": [
            "White",
            "American Indian or Alaska Native",
            "Asian",
            "Filipino/a",
            "Pacific Islander",
            "Multiple Ethnicities",
            "African American/Black",
            "Hispanic/Latino/a",
            "Prefer not to say",
        ],
        "labels": [
            "White",
            "American Indian or Alaska Native",
            "Asian",
            "Filipino/a",
            "Pacific Islander",
            "Multiple Ethnicities",
            "African American/Black",
            "Hispanic/Latino/a",
            "Prefer not to say",
        ],
    },
}

POLARQS = {
    "Q5": "Fastest-warming region",
    "Q7": "Reconstructing past temps",
    "Q8": "Last million years mostly",
    "Q6": "Length ice core record",
    "Q10": "ID plot of CO2 vs temp",
    "Q11": "ID plot of CO2 vs temp",
    "Q12": "ID plot of CO2 vs temp",
    "Q19": "Polar Amp. primary cause",
}

STATSQS = {
    "Q15": "Neg lin assoc",
    "Q13": "No/mod/perf lin. assoc",
    "Q4": "Ave relationship x vs y",
    "Q3": "Prediction outside range",
    "Q14": "Use of lin reg",
    "Q16": "Evidence of causation",
}


#    "Q9": {
#        "text": "The graph below shows how temperature has changed with CO2 at an Arctic research station, in the modern era globally, as well as in the ice core record. The linear relationship between temperature and CO2 is seen to vary, but the correlation is positive for all three. Choose the best descriptions for the scatterplots labelled a, b, and c.",

# Q17. What is polar amplification? ________________________________________________________________________ ________________________________________________________________________ ________________________________________________________________________ ________________________________________________________________________ ______________________________________________________________________
# Q18. Describe a positive feedback loop involving climate in polar regions. ________________________________________________________________________ ________________________________________________________________________ ________________________________________________________________________ ________________________________________________________________________ ________________________________________________________________________

# Please enter your student ID below. Your ID will be used confidentially by an external evaluator to match pre and post surveys, after which it will be deleted from your survey results so that they will be anonymous. No faculty or staff at your university will have access to this information in connection with your survey results.
# 15. What is your student ID? _______________________________
