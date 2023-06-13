#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:04:10 2023

@author: prowe
"""

import numpy as np
import pandas as pd
from scipy import stats


def get_pc_correct(in_series, corr: str):
    """
    Get percentage correct
    @param in_series
    @param corr
    """
    percentages = 100 * in_series.value_counts(dropna=True, normalize=True)
    # QC: make sure correct is in the set of answers
    if corr not in percentages.keys():
        raise ValueError("No student gave the correct response")
    return percentages[corr]


def get_num_correct(in_series, corr: str):
    """
    Get number correct and number incorrect for a given survey question
    @param in_series  Survey responses for a question(pandas core series)
    @param corr  The exact correct answer
    """
    valcounts = in_series.value_counts(dropna=True)
    tot = sum(valcounts.values)
    # QC: make sure correct is in the set of answers
    #     actually, allow the possibility that no student got the
    #     correct answer (this can happen, esp on the pre-test)
    if corr not in valcounts.keys():
        # raise ValueError("No student gave the correct response")
        # sum([count for name, count in valcounts.items()])
        ncorr = 0
    else:
        ncorr = int(valcounts[corr])
    return ncorr, tot - ncorr


def get_fisher(bef_corr: int, bef_wrong: int, aft_corr: int, aft_wrong: int):
    """
    Perform Fisher's test to get odds ratio and pvalue
    @param bef_corr  Number correct before
    @param bef_wrong  Number incorrect before
    @param aft_corr  Number correct after
    @param aft_wrong  Number incorrect after
    Notes
    Fisher's test Table format
    We want to test whether people did better after the module/class
    __________________________________________________
              |     Correct   |      Incorrect        |
      After   |   aft_corr   a|  tot - pcaft[name] b  |
     Before   |   bef_corr   c|  tot - pcbef[name] d  |
    --------------------------------------------------
       a,c => positive (correct)  b,d => negative (incorrect)

    Positives represent pairs that are the same in both variables (diagonal)
    and negatives represent the pairs that aren’t the same in both variables.
    (off-diagonals)
    The odds ratio tells us how many times more positive cases can happen than
    negative cases.
    odds ratio = 1 => no effect
    odds ratio > 1 => higher chance of effect
    odds ratio < 1 => lower odds
    """
    data = [
        [aft_corr, aft_wrong],
        [bef_corr, bef_wrong],
    ]
    fish = stats.fisher_exact(data)

    # The odds ratio can be infinite, in which case we canot use round
    if not np.isfinite(fish[0]):
        odds = fish[0]
    elif fish[0] >= 10:
        odds = round(fish[0])
    elif fish[0] >= 1:
        odds = round(fish[0], 1)
    else:
        odds = round(fish[0], 1)

    if fish[1] < 0.01:
        pval = "<0.01"
    elif fish[1] < 0.2:
        pval = f"{fish[1]:0.2f}"  # str("%0.2f" % (fish[1]))
    else:
        pval = f"{fish[1]:1.1f}"  # str("%1.1f" % (fish[1]))

    return odds, pval


def get_bef_aft(dfm, name, correct_ans):
    """
    Return the number of correct and incorrect answers before and after, for
    the question given by name
    @param dfm  pandas dataframe
    @param name  The question name (e.g. 'Q5')
    @param corr  The exact text of the correct answer (e.g. 'Polar regions')
    """
    # Get the dataframe for the given question before and after for the group
    ibef = name + "_x"
    iaft = name + "_y"
    fdf = dfm[[ibef, iaft]]

    # Filter out rows where question was not answered before or after
    # (e.g. filter out rows with one or more nan)
    fdf = fdf[fdf[[ibef, iaft]].notnull().all(1)]

    # Get the number correct and wrong before and after
    bef_corr, bef_wrong = get_num_correct(fdf[name + "_x"], correct_ans)
    aft_corr, aft_wrong = get_num_correct(fdf[name + "_y"], correct_ans)

    # Make sure the filtering worked
    if bef_corr + bef_wrong != aft_corr + aft_wrong:
        raise ValueError("Oops!  Different number before than after")

    return bef_corr, bef_wrong, aft_corr, aft_wrong


def getstats(dfm, name: str, corr: str):
    """
    Get statistics: percent correct before and after; difference (change);
    number of students; and odds ratio and pvalue from Fisher's exact test
    @param dfm  pandas dataframe
    @param name  The question name (e.g. 'Q5')
    @param corr  The exact text of the correct answer (e.g. 'Polar regions')
    """
    # val = param.KNOW[name]
    # corr = val["options"][val["icorrect"]]

    # Get the number correct and wrong before and after where both exist
    bef_corr, bef_wrong, aft_corr, aft_wrong = get_bef_aft(dfm, name, corr)

    # Perform Fisher's test
    odds, pval = get_fisher(bef_corr, bef_wrong, aft_corr, aft_wrong)

    # Get remaining outputs
    nstudents = bef_corr + bef_wrong
    # change = round(aft_corr - bef_corr)
    change = round((aft_corr - bef_corr) / nstudents * 100)
    before_pc = round(100 * bef_corr / (bef_corr + bef_wrong))
    after_pc = round(100 * aft_corr / (aft_corr + aft_wrong))

    return before_pc, after_pc, change, nstudents, odds, pval


def get_vals(in_series, ans_choices: list[str]):
    """
    Return cleaned responses for a given survey question
    @param in_series  Survey responses for a question(pandas core series)
    @param ans_choices  Allowed responses
    @returns  The cleaned responses (pandas series)
    """
    percentages = 100 * in_series.value_counts(dropna=True, normalize=True)
    # QC: make sure expected and actual answers match
    if not np.all([x in ans_choices for x in percentages.keys()]):
        ind = [x in ans_choices for x in percentages.keys()]
        # ind = [x == False for x in ind]
        print("\n\nAnswer choices:")
        print(ans_choices)
        print("\nStudent answer that is not in answer choices:")
        print(np.array(percentages.keys())[ind])
        print("\n\n")
        raise ValueError("A student answer was not an expected response!")
    out_series = pd.Series([], dtype=pd.StringDtype())
    # data=None, index=ans_choices)
    for index in ans_choices:
        if index in percentages.index:
            out_series[index] = percentages[index]
        else:
            out_series[index] = 0

    return out_series


def set_before_and_after_to_numeric(in_bef, in_aft, rank_labels):
    """
    Set the before and after to a number
    """
    out_bef = np.nan * np.ones(in_bef.size)
    out_aft = np.nan * np.ones(in_bef.size)
    count = 0
    for bef, aft in zip(in_bef, in_aft):
        if (bef in rank_labels) and (aft in rank_labels):
            # add one because should start from 1 not 0
            out_bef[count] = rank_labels.index(bef) + 1
            out_aft[count] = rank_labels.index(aft) + 1
            count += 1

    out_bef = out_bef[:count]
    out_aft = out_aft[:count]

    return out_bef, out_aft


# def print_mann_whitney_u(survey_item_label, in1, in2, rank_labels):
#     """
#     Print Mann Whitney results
#     """
#     x, y = set_before_and_after_to_numeric(in1, in2, rank_labels)
#     n1 = len(x)
#     n2 = len(y)
#     U, p = stats.mannwhitneyu(x, y, alternative="two-sided")
#     print("\n" + survey_item_label)
#     print("median, median, n1, n2, U, p")
#     print(np.median(x), np.median(y), n1, n2, U, p)
