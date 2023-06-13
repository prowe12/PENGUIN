#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:22:59 2019

@author: prowe
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import path_params


def add_percentages(vals, axnum):
    for i, v in enumerate(vals):
        if v < 0.01:
            axnum.text(i - 0.1, v + 2, str(round(v)) + "%", fontsize=8)
        elif v < 2:
            axnum.text(i - 0.2, v + 2, str(round(v, 1)) + "%", fontsize=8)
        elif v < 10:
            axnum.text(i - 0.1, v + 2, str(round(v)) + "%", fontsize=8)
        else:
            axnum.text(i - 0.2, v + 2, str(round(v)) + "%", fontsize=8)


def set_colors(bl):
    cmap = matplotlib.cm.get_cmap("Spectral")

    for i in range(len(bl)):
        k = 0.2 + 0.2 * i
        bl[i].set_color(cmap(k)[:3])

    if len(bl) == 6:
        bl[5].set_color("m")
    elif len(bl) > 6:
        raise ValueError("not prepared for this case, modify code")

    return bl


def set_labels(bl, labels):
    for i in range(len(bl)):
        bl[i].set_label(labels[i])


def get_vals(in_series, indices):
    in_series = 100 * in_series.value_counts(dropna=True, normalize=True)
    out_series = pd.Series(data=None, index=indices)
    for index in indices:
        if index in in_series.index:
            out_series[index] = in_series[index]
        else:
            out_series[index] = 0

    return out_series


def plot_before_after():
    # Labels
    comfort_labels = [
        "Very Uncomfortable",
        "Somewhat Uncomfortable",
        "Neutral",
        "Somewhat Comfortable",
        "Very Comfortable",
        "Don’t Know",
    ]

    importance = [
        "Not Important at All",
        "Slightly Important",
        "Moderately Important",
        "Very Important",
        "Extremely Important",
        "Don’t Know",
    ]

    importance_labels = [
        "Not at all",
        "Slghtly",
        "Moderately",
        "Very",
        "Extremely",
        "Don't know",
    ]

    rating_labels = ["Very Poor", "Poor", "Fair", "Good", "Excellent"]

    # # # # #   BEGIN    # # # # # #
    data_file = data_dir + datafile

    # Flags
    save_figs = True  # whether to save figures

    # Load in the data
    df = pd.read_excel(data_file, header=[0, 1], sheet_name=0)
    print("Column headings:")
    print(df.columns)

    # fmt: off
    # cols = [
    #     'StartDate', 'EndDate', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8',
    #     'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19',
    #     'Q20_1', 'Q20_2', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25_1', 'Q25_2', 'Q26_1',
    #     'Q26_2', 'Q27_1', 'Q27_2', 'Q28_1', 'Q28_2', 'Q28_3', 'Q28_4', 'Q28_5',
    #     'Q28_6', 'Q28_7', 'Q28_8', 'Q28_9', 'Q28_10', 'Q28_11', 'Q28_12',
    #     'Q28_13', 'Q28_14', 'Q28_15', 'Q28_15_TEXT', 'Q29', 'Q30', 'Q31', 'Q32',
    #     'Q33', 'Q34', 'Q35_1', 'Q35_2', 'Q35_4', 'Q35_5', 'Q35_6', 'Q36_1',
    #     'Q36_2', 'Q36_3', 'Q36_4', 'Q36_5', 'Q36_6', 'Q36_7', 'Q36_8', 'Q36_9',
    #     'Q36_10', 'Q36_9_TEXT', 'Q37', 'Q39', 'Q40',
    # ]
    # fmt: on

    # Question key
    # Q6: How comfortable are you with Python/Excel?
    # Q8: Before this module, how much exposure did you have to polar research
    # Q12: How important is polar research in the context of climate change?
    # Q13: Rank your knowledge of climate change
    # Q14: Rank your knowledge of the topic
    # Q15: Doing this module was a _____ way to learn about a topic in your course.
    # Q17: Overall, how would you rate the polar data module you just completed?

    # Data, e.g. df['Q6_6'].value_counts(dropna=True)

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

    # Replace with inputs

    # Add values from Excel sheet
    keystoremove = []
    for key, value in org.items():
        if key in befaft:
            print(key)
            for innerkey, innerval in befaft[key].items():
                org[key][innerkey] = innerval
            org[key]["bef"] = get_vals(df[value["qbef"]], value["ans"])
            org[key]["aft"] = get_vals(df[value["qaft"]], value["ans"])
        else:
            # Remove from org
            keystoremove.append(key)
    for key in keystoremove:
        org.pop(key)

    # # # # # # # # # #      Figures    # # # # # # # # # # # # # #
    figno = 0

    left = 0.12
    wid = 0.85
    bot1 = 0.3
    bot2 = 0.65
    height = 0.32
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

        if save_figs:
            plt.savefig(outdir + outfile + name + ".eps")


# Directories and files
maindir = path_params.DATA_DIR
outdir = maindir + "analysis/supplemental/"

# Fall 2021 Stats
data_dir = maindir + "results_2021_fall/"
datafile = "StatsPostSurvey.xlsx"
# datafile = "PENGUIN Statistics Knowledge Post-Survey Dataset.xlsx"
outfile = "stats_post_2021_fall_"
# The data
befaft = {
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
plot_before_after()

# Spring 2022 Stats
data_dir = maindir + "results_2022_spring/"
datafile = "StatsPostSurvey.xlsx"
# datafile = "Spring 2022 PENGUIN Statistics Knowledge Post-Survey Dataset.xlsx"
outfile = "stats_post_2022_spring_"
# The data
befaft = {
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
plot_before_after()

# Fall 2022 Stats
data_dir = maindir + "results_2022_fall/"
datafile = "StatsPostSurvey.xlsx"
# datafile = "Fall 2022 PENGUIN Statistics Knowledge Post-Survey Dataset.xlsx"
outfile = "stats_post_2022_fall_"
# The data
befaft = {
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
plot_before_after()

# Fall 2021 modeling
data_dir = maindir + "results_2021_fall/"
datafile = "PENGUIN Climate Modeling Post-Survey Dataset.xlsx"
outfile = "modeling_post_2021_fall_"
# The data
befaft = {
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
plot_before_after()

# single = {
#     "exposure": {
#         "qno": "Q21",
#         "ans": exposure_labels,
#         "labels": exposure_labels,
#         "title": "Exposure to polar research",
#     },
#     "overall": {
#         "qno": "Q29",
#         "ans": rating_labels,
#         "labels": rating_labels,
#         "title": "Overall module ranking",
#     },
#     "learnmore": {
#         "qno": "Q32",
#         "ans": yesno_labels,
#         "labels": yesno_labels,
#         "title": "Like to learn more about polar data?",
#     },
#     "stem": {
#         "qno": "Q33",
#         "ans": yesno_labels,
#         "labels": yesno_labels,
#         "title": "Are you a STEM major?",
#     },
#     "consideringstem": {
#         "qno": "Q34",
#         "ans": yesno_labels,
#         "labels": yesno_labels,
#         "title": "Are you considering a STEM major?",
#     },
# }

# exposure_labels = [
#     "None",
#     "A little",
#     "Some",
#     "A fair amount",
#     "A great deal",
#     "Don’t know",
# ]

#    yesno_labels = ["Yes", "No", "Maybe"]
