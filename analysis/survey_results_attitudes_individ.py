#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:43:38 2023

@author: prowe
"""

import matplotlib.pyplot as plt
import numpy as np

from analysis_resources import get_vals
from plot_resources import set_colors, add_percentages, set_labels
from clean import load, remove_symbols


def plot_before_after(befaft: dict, datafile: str, outfilepfx: str):
    """
    Make plots that compare before and after
    @params befaft  Information about the pandas array
    @params datafile  The full path to the input data file
    @params outfilepfx  Directory + filename prefix for saving the figure
    """
    # Labels
    comfort_labels = [
        "Very Uncomfortable",
        "Somewhat Uncomfortable",
        "Neutral",
        "Somewhat Comfortable",
        "Very Comfortable",
        "Dont Know",
    ]

    importance = [
        "Not Important at All",
        "Slightly Important",
        "Moderately Important",
        "Very Important",
        "Extremely Important",
        "Dont Know",
    ]

    importance_labels = [
        "Not at all",
        "Slghtly",
        "Moderately",
        "Very",
        "Extremely",
        "Dont know",
    ]

    rating_labels = ["Very Poor", "Poor", "Fair", "Good", "Excellent"]

    # Flags: TODO read in
    save_figs = True  # whether to save figures

    # The data
    org = {
        "cs": {
            "qbef": "Q20_1",
            "qaft": "Q20_2",
            "ans": comfort_labels,
            "labels": comfort_labels,
            "title": "Comfort with Rstudio",
        },
        "polarimport": {
            "qbef": "Q25_1",
            "qaft": "Q25_2",
            "ans": importance,
            "labels": importance_labels,
            "title": "Importance of Polar regions",
        },
        "climateknowledge": {
            "qbef": "Q26_1",
            "qaft": "Q26_2",
            "ans": rating_labels,
            "labels": rating_labels,
            "title": "Climate Knowledge",
        },
        "icecoreknowledge": {
            "qbef": "Q27_1",
            "qaft": "Q27_2",
            "ans": rating_labels,
            "labels": rating_labels,
            "title": "Ice Core Knowledge",
        },
    }

    # # # # #   BEGIN    # # # # # #
    # Load and clean the data
    dfm = load(datafile)
    remove_symbols(dfm)  # Done in place

    # Replace with inputs and
    # Add values from Excel sheet
    keystoremove = []
    for key, value in org.items():
        if key in befaft:
            for innerkey, innerval in befaft[key].items():
                org[key][innerkey] = innerval
            value["bef"] = get_vals(dfm[value["qbef"]], value["ans"])
            value["aft"] = get_vals(dfm[value["qaft"]], value["ans"])
        else:
            # Remove from org
            keystoremove.append(key)
    for key in keystoremove:
        org.pop(key)

    if "title" in befaft:
        title = befaft["title"]
    else:
        title = ""

    # # # # # # # # # #      Figures    # # # # # # # # # # # # # #
    figno = 0

    left = 0.12
    wid = 0.85
    bot1 = 0.28
    bot2 = 0.63
    height = 0.3
    legend_left = 2.3
    ytext = 62  # np.ceil(np.max([python_before, python_after]))*.93
    ymax = 80  # np.round(1.2*ytext/10)*10

    for name, vals in org.items():
        figno += 1
        labels = vals["labels"]
        before = vals["bef"]
        after = vals["aft"]

        plt.figure(figsize=(5, 5), num=figno, clear=True)
        ax1 = plt.subplot(211)
        ax2 = plt.subplot(212)  # , sharex=ax1)
        ax1.set_position([left, bot2, wid, height])
        ax2.set_position([left, bot1, wid, height])

        bar1 = ax1.bar(np.arange(len(before)), before)
        ax1.set_ylabel("Respondents (%)")
        ax1.set_xticks([], (""))
        set_colors(bar1)
        ax1.text(-0.5, ytext, "a) " + vals["title"] + " \n    Before")
        ax1.set_ylim([0, ymax])
        ax1.set_title(title)
        add_percentages(before, ax1)

        xtick = np.arange(len(after))
        bar2 = ax2.bar(xtick, after)
        ax2.set_ylabel("Respondents (%)")
        set_colors(bar2)
        ax2.text(-0.5, ytext, "b) " + vals["title"] + " \n    After")
        ax2.set_xticks([], (""))
        ax2.set_ylim([0, ymax])
        add_percentages(after, ax2)
        set_labels(bar2, labels)
        plt.legend(bbox_to_anchor=(legend_left, 0.5), loc="right")
        ax2.set_xticks(
            xtick, labels, rotation=45, ha="right", rotation_mode="anchor"
        )

        if save_figs:
            plt.savefig(outfilepfx + name + ".eps")
