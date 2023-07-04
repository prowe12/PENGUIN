#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:43:38 2023

@author: prowe
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# My modules
from analysis.plot_resources import add_percentages, set_colors, set_labels
from analysis.analysis_resources import get_vals

# def add_percentages(vals, axnum):
#     for i, v in enumerate(vals):
#         if v < 0.01:
#             axnum.text(i - 0.1, v + 2, str(round(v)) + "%", fontsize=8)
#         elif v < 2:
#             axnum.text(i - 0.2, v + 2, str(round(v, 1)) + "%", fontsize=8)
#         elif v < 10:
#             axnum.text(i - 0.1, v + 2, str(round(v)) + "%", fontsize=8)
#         else:
#             axnum.text(i - 0.2, v + 2, str(round(v)) + "%", fontsize=8)


# def set_colors(bl):
#     cmap = matplotlib.cm.get_cmap("Spectral")

#     for i in range(len(bl)):
#         k = 0.2 + 0.2 * i
#         bl[i].set_color(cmap(k)[:3])

#     if len(bl) == 6:
#         bl[5].set_color("m")
#     elif len(bl) > 6:
#         raise ValueError("not prepared for this case, modify code")

#     return bl


# def set_labels(bl, labels):
#     for i in range(len(bl)):
#         bl[i].set_label(labels[i])


# def get_vals(in_series, indices):
#     in_series = 100 * in_series.value_counts(dropna=True, normalize=True)
#     out_series = pd.Series(data=None, index=indices)
#     for index in indices:
#         if index in in_series.index:
#             out_series[index] = in_series[index]
#         else:
#             out_series[index] = 0

#     return out_series


def combine_results(data: list[dict]):
    """
    Make plots that compare before and after
    @params befaft  Information about the pandas array
    @params datafile  The full path to the input data file
    @params outfilepfx  Directory + filename prefix for saving the figure
    """
    # Answers
    importance = [
        "Dont Know",
        "Not Important at All",
        "Slightly Important",
        "Moderately Important",
        "Very Important",
        "Extremely Important",
    ]

    comfort = [
        "Dont Know",
        "Very Uncomfortable",
        "Somewhat Uncomfortable",
        "Neutral",
        "Somewhat Comfortable",
        "Very Comfortable",
    ]

    # Labels: for labeling all plots
    # comfort_labels = [
    #     "Don't Know",
    #     "V. Uncomfort.",
    #     "S. Uncomfort.",
    #     "Neutral",
    #     "S. Comfort.",
    #     "V. Comfort.",
    # ]
    # Labels: for labeling after panels only
    comfort_labels = [
        "Don't Know",
        "V. Uncomfortable",
        "S. Uncomfortable",
        "Neutral",
        "S. Comfortable",
        "V. Comfortable",
    ]

    importance_labels = [
        "Don't know",
        "Not at all",
        "Slghtly",
        "Moderately",
        "Very",
        "Extremely",
    ]

    rating_labels = ["Very Poor", "Poor", "Fair", "Good", "Excellent"]
    yesno_labels = ["No", "Maybe", "Yes"]

    # Generic data organization
    org = {
        "climateknowledge": {
            "respbef": [],
            "respaft": [],
            "ans": rating_labels,
            "labels": rating_labels,
            "title": "Climate Knowledge",
            "rot": 0,
        },
        "cs": {
            "respbef": [],
            "respaft": [],
            "ans": comfort,
            "labels": comfort_labels,
            "title": "Comfort with Rstudio",
            "rot": 45,
        },
        "polarimport": {
            "respbef": [],
            "respaft": [],
            "ans": importance,
            "labels": importance_labels,
            "title": "Polar importance",
            "rot": 45,
        },
        "subjectknowledge": {
            "respbef": [],
            "respaft": [],
            "ans": rating_labels,
            "labels": rating_labels,
            "title": "Ice Core Knowledge",
            "rot": 0,
        },
        "ranking": {
            "respaft": [],
            "ans": rating_labels,
            "labels": rating_labels,
            "title": "Module ranking",
            "rot": 0,
        },
        "learnmore": {
            "respaft": [],
            "ans": yesno_labels,
            "labels": yesno_labels,
            "title": "Learn more polar research?",
            "rot": 0,
        },
    }

    # Loop over files and load and combine the data
    for dat in data:
        df = pd.read_excel(dat["datafile"], header=[0, 1], sheet_name=0)

        from analysis.clean import remove_symbols

        remove_symbols(df)  # Done in place

        # Replace with inputs and
        # Add values from Excel sheet
        keystoremove = []
        for key, value in org.items():
            if key in dat and "respbef" in org[key]:
                rbefprev = org[key]["respbef"]
                if type(rbefprev) == list:
                    org[key]["respbef"] = df[dat[key]["qbef"]]
                else:
                    rbef = df[dat[key]["qbef"]]
                    org[key]["respbef"] = pd.concat(
                        [rbefprev, rbef], ignore_index=True, sort=False
                    )

            if key in dat and "respaft" in org[key]:
                raftprev = org[key]["respaft"]
                if type(raftprev) == list:
                    org[key]["respaft"] = df[dat[key]["qaft"]]
                else:
                    raft = df[dat[key]["qaft"]]
                    org[key]["respaft"] = pd.concat(
                        [raftprev, raft], ignore_index=True, sort=False
                    )
            elif key not in dat:
                # Remove from org
                keystoremove.append(key)
        for key in keystoremove:
            org.pop(key)

    for key, value in org.items():
        # TODO
        print(key)
        if "respbef" in value:
            org[key]["bef"] = get_vals(
                value["respbef"].squeeze(), value["ans"]
            )
        if "respaft" in value:
            org[key]["aft"] = get_vals(
                value["respaft"].squeeze(), value["ans"]
            )

    return org


def makefig(org: dict, outprefix: str = "", savefigs: bool = False):

    panels = [
        "climateknowledge",
        "polarimport",
        "subjectknowledge",
        "cs",
    ]
    # "ranking",
    # "learnmore",
    types = {"bef": "before", "aft": "after"}

    # # # # # # # # # #      Figures    # # # # # # # # # # # # # #
    left1 = 0.08
    left2 = 0.58
    # For labeling all panels
    # bot1 = 0.83
    # bot2 = 0.62
    # bot3 = 0.38
    # bot4 = 0.11
    # plt.figure(figsize=(8, 8), num=1, clear=True)
    # For labeling after panels only
    bot1 = 0.81
    bot2 = 0.62
    bot3 = 0.37
    bot4 = 0.18
    plt.figure(figsize=(8, 6), num=1, clear=True)

    left = [left1, left1, left1, left1, left2, left2, left2, left2]
    bot = [bot1, bot2, bot3, bot4, bot1, bot2, bot3, bot4]
    wid = 0.4
    height = 0.18
    letter = ["a) ", "b) ", "c) ", "d) ", "e) ", "f) ", "g) ", "h) "]
    ax = [plt.subplot(4, 2, i + 1) for i in range(8)]
    for i in range(8):
        ax[i].set_position([left[i], bot[i], wid, height])

    ytext = 70
    ymax = 80

    i = -1
    for panel in panels:
        if panel not in org:
            raise ValueError("Variable missing")
        labels = org[panel]["labels"]

        typs = [x for x in types.items() if x[0] in org[panel]]
        for typ in typs:
            i += 1
            resp = org[panel][typ[0]]
            xtic = np.arange(len(resp))
            bar1 = ax[i].bar(xtic, resp)
            ax[i].set_ylabel("Students (%)")
            ax[i].set_xticks([], (""))
            set_colors(bar1)
            title = letter[i] + org[panel]["title"] + " " + typ[1]
            ax[i].text(-0.5, ytext, title)
            ax[i].set_ylim([0, ymax])
            add_percentages(resp, ax[i])
            set_labels(bar1, labels)
            if typ[1] == "after":
                ax[i].set_xticks(
                    xtic,
                    labels,
                    rotation=org[panel]["rot"],
                )
            # rotation_mode="anchor",
            # ha="right",

        # xtick = np.arange(len(after))
        # bar2 = ax[i + 1].bar(xtick, after)
        # ax[i + 1].set_ylabel("Respondents (%)")
        # set_colors(bar2)
        # ax[i + 1].text(
        #     -0.5, ytext, "b) " + org[panel]["title"] + " \n    After"
        # )
        # ax[i + 1].set_xticks([], (""))
        # ax[i + 1].set_ylim([0, ymax])
        # add_percentages(after, ax[i + 1])
        # set_labels(bar2, labels)
        # plt.legend(bbox_to_anchor=(legend_left, 0.5), loc="right")
        # ax[i + 1].set_xticks(
        #     xtick, labels, rotation=45, ha="right", rotation_mode="anchor"
        # )

    if savefigs:
        plt.savefig(outprefix + ".eps")

    # Plots with after only
    panels = ["ranking", "learnmore"]
    types = {"bef": "", "aft": ""}

    # # # # # # # # # #      Figures    # # # # # # # # # # # # # #
    left1 = 0.08
    left2 = 0.58
    bot1 = 0.83
    bot2 = 0.62
    bot3 = 0.38
    bot4 = 0.11
    left = [left1, left1, left1, left1, left2, left2, left2, left2]
    bot = [bot1, bot2, bot3, bot4, bot1, bot2, bot3, bot4]
    wid = 0.4
    height = 0.16
    letter = ["a) ", "b) ", "c) ", "d) ", "e) ", "f) ", "g) ", "h) "]
    plt.figure(figsize=(8, 8), num=2, clear=True)
    ax = [plt.subplot(4, 2, i + 1) for i in range(8)]
    for i in range(8):
        ax[i].set_position([left[i], bot[i], wid, height])

    ytext = 70
    ymax = 80

    i = -1
    for panel in panels:
        if panel not in org:
            raise ValueError("Variable missing")
        labels = org[panel]["labels"]

        typs = [x for x in types.items() if x[0] in org[panel]]
        for typ in typs:
            i += 1
            resp = org[panel][typ[0]]
            xtic = np.arange(len(resp))
            bar1 = ax[i].bar(xtic, resp)
            ax[i].set_ylabel("Students (%)")
            ax[i].set_xticks([], (""))
            set_colors(bar1)
            title = letter[i] + org[panel]["title"] + " " + typ[1]
            ax[i].text(-0.5, ytext, title)
            ax[i].set_ylim([0, ymax])
            add_percentages(resp, ax[i])
            set_labels(bar1, labels)
            ax[i].set_xticks(
                xtic,
                labels,
                rotation=org[panel]["rot"],
            )

    if savefigs:
        plt.savefig(outprefix + "b.eps")


def makefigs(org: dict, outprefix: str = "", savefigs: bool = False):

    # # # # # # # # # #      Figures    # # # # # # # # # # # # # #
    figno = 0

    left = 0.12
    wid = 0.85
    bot1 = 0.28
    bot2 = 0.63
    height = 0.3
    # legend_height = 1.87
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

        if savefigs:
            plt.savefig(outprefix + name + ".eps")
