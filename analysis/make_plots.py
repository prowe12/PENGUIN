#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:28:45 2023

@author: prowe
"""

# Modules
import matplotlib.pyplot as plt
import numpy as np

# My modules
from plot_resources import add_percentages, set_colors_corr, set_labels
from analysis_resources import get_vals, get_vals_in, getstats

# import stats_params as param
# import clim_modeling_params as cm_param


def plot_demo(dfm, demo, figno: int, savefigs: bool, outdir: str):
    """
    Plot the demographic questions in a 4x4 grid for four survey questions
    @param dfm  The pandas dataframe
    @param names
    @param figno  The figure number
    """

    names = demo.keys()

    left = [0.08, 0.08, 0.58, 0.58, 0.08]
    bot = [0.74, 0.44, 0.74, 0.44, 0.1]
    bot += bot
    height = 0.23
    wid = [0.4, 0.4, 0.4, 0.4, 0.9]
    letter = ["a) ", "b) ", "c) ", "d) ", "e) "]

    if len(names) <= 2:
        raise ValueError("Option not here yet")
    else:
        plt.figure(figsize=(8, 8), num=figno, clear=True)
        axs = [plt.subplot(3, 2, i + 1) for i in range(len(names))]
        for i in range(len(names)):
            axs[i].set_position([left[i], bot[i], wid[i], height])

    ytext = 108
    ymax = 120

    i = -1
    for name in names:
        i += 1
        val = demo[name]
        if val["title"] == "Race/Ethnicity":
            resp = get_vals_in(dfm[name], val["options"])
        else:
            resp = get_vals(dfm[name], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        title = letter[i] + val["title"]
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])

        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        set_labels(bar1, val["labels"])
        axs[i].set_xticks(xtic, val["labels"], rotation=45)

    if savefigs:
        plt.savefig(f"{outdir}/stats_demo.png")
        plt.savefig(f"{outdir}/stats_demo.eps")


def plot_4by4_bef_aft(dfm, param, names: list[str], figno: int):
    """
    Plot the results before and after in a 4x4 grid for four survey questions
    @param dfm  The pandas dataframe
    @param param  The survey parameters
    @param names
    @param figno  The figure number
    """
    bot = [0.81, 0.63, 0.33, 0.15]
    bot += bot
    height = 0.17
    letter = ["a) ", "b) ", "c) ", "d) ", "e) ", "f) ", "g) ", "h) "]

    if len(names) <= 2:
        leftall = 0.17
        wid = 0.8
        plt.figure(figsize=(4, 8), num=figno, clear=True)
        axs = [plt.subplot(4, 1, i + 1) for i in range(4)]
        for i in range(4):
            axs[i].set_position([leftall, bot[i], wid, height])
    else:
        left1 = 0.08
        left2 = 0.58
        left = [left1, left1, left1, left1, left2, left2, left2, left2]
        wid = 0.4
        plt.figure(figsize=(8, 8), num=figno, clear=True)
        axs = [plt.subplot(4, 2, i + 1) for i in range(8)]
        for i in range(8):
            axs[i].set_position([left[i], bot[i], wid, height])

    ytext = 108
    ymax = 120

    i = -1
    for name in names:
        val = param.KNOW[name]
        i += 1
        resp = get_vals(dfm[name + "_x"], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        title = letter[i] + val["title"] + "; before"
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        set_colors_corr(bar1, val["icorrect"])
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        # set_labels(bar1, val["labels"])
        # axs[i].set_xticks(xtic, val["labels"], rotation=45)

        i += 1
        resp = get_vals(dfm[name + "_y"], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        set_colors_corr(bar1, val["icorrect"])

        title = letter[i] + val["title"] + "; after"
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        set_labels(bar1, val["labels"])
        axs[i].set_xticks(xtic, val["labels"], rotation=45)


def plot_4by4_bef_aft_cm(dfm, cm_param, names: list[str], figno: int):
    """
    Plot the results before and after in a 4x4 grid for four survey questions
    for the climate modeling (cm) course
    @param dfm  The pandas dataframe
    @param cm_param  The climate modeling survey parameters
    @param names
    @param figno  The figure number
    """
    bot = [0.81, 0.63, 0.33, 0.15]
    bot += bot
    height = 0.17
    letter = ["a) ", "b) ", "c) ", "d) ", "e) ", "f) ", "g) ", "h) "]

    if len(names) <= 1:
        leftall = 0.1
        wid = 0.9
        plt.figure(figsize=(4, 8), num=figno, clear=True)
        axs = [plt.subplot(4, 1, i + 1) for i in range(2)]
        for i in range(2):
            axs[i].set_position([leftall, bot[i], wid, height])
    elif len(names) <= 2:
        bot = [0.81, 0.63, 0.31, 0.13]
        bot += bot
        leftall = 0.17
        wid = 0.8
        plt.figure(figsize=(4, 8), num=figno, clear=True)
        axs = [plt.subplot(4, 1, i + 1) for i in range(4)]
        for i in range(4):
            axs[i].set_position([leftall, bot[i], wid, height])
    else:
        left1 = 0.08
        left2 = 0.58
        left = [left1, left1, left1, left1, left2, left2, left2, left2]
        wid = 0.4
        plt.figure(figsize=(8, 8), num=figno, clear=True)
        axs = [plt.subplot(4, 2, i + 1) for i in range(8)]
        for i in range(8):
            axs[i].set_position([left[i], bot[i], wid, height])

    ytext = 108
    ymax = 120

    i = -1
    for name in names:
        val = cm_param.KNOW[name]
        i += 1
        resp = get_vals(dfm[name + "_x"], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        title = letter[i] + val["title"] + "; before"
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        set_colors_corr(bar1, val["icorrect"])
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        # set_labels(bar1, val["labels"])
        # axs[i].set_xticks(xtic, val["labels"], rotation=45)

        i += 1
        resp = get_vals(dfm[name + "_y"], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        set_colors_corr(bar1, val["icorrect"])

        title = letter[i] + val["title"] + "; after"
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        set_labels(bar1, val["labels"])
        axs[i].set_xticks(xtic, val["labels"], rotation=45)


def plot_test_v_control(interv, comp, param, names: list[str], figno: int):
    """
    Make plots comparing test group and control group
    @param interv  pandas dataframe for test (intervention) group
    @param comp  pandas dataframe for control (comparison) group
    @param param  The survey parameters
    @param names
    @param  figno  desired number for figure
    """
    left1 = 0.08
    left2 = 0.58
    bot1 = 0.8
    bot2 = 0.62
    bot3 = 0.32
    bot4 = 0.14
    left = [left1, left1, left2, left2, left1, left1, left2, left2]
    bot = [bot1, bot2, bot1, bot2, bot3, bot4, bot3, bot4]
    wid = 0.4
    height = 0.17
    letter = ["a) ", "b) ", "c) ", "d) ", "e) ", "f) ", "g) ", "h) "]

    plt.figure(figsize=(8, 8), num=figno, clear=True)
    axs = [plt.subplot(4, 2, i + 1) for i in range(8)]
    for i in range(8):
        axs[i].set_position([left[i], bot[i], wid, height])

    ytext = 108
    ymax = 120

    i = -1
    for name in names:
        val = param.KNOW[name]
        i += 1
        resp = get_vals(interv[name + "_x"], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        title = letter[i] + val["title"] + "; before"
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        set_colors_corr(bar1, val["icorrect"])
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        # set_labels(bar1, val["labels"])
        # axs[i].set_xticks(xtic, val["labels"], rotation=45)
        if i == 0:
            axs[i].set_title("Test")

        i += 1
        resp = get_vals(interv[name + "_y"], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        set_colors_corr(bar1, val["icorrect"])

        title = letter[i] + val["title"] + "; after"
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        set_labels(bar1, val["labels"])
        axs[i].set_xticks(xtic, val["labels"], rotation=45)

        i += 1
        resp = get_vals(comp[name + "_x"], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        title = letter[i] + val["title"] + "; before"
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        set_colors_corr(bar1, val["icorrect"])
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        # set_labels(bar1, val["labels"])
        # axs[i].set_xticks(xtic, val["labels"], rotation=45)
        if i == 2:
            axs[i].set_title("Control")

        i += 1
        resp = get_vals(comp[name + "_y"], val["options"])
        xtic = np.arange(len(resp))
        bar1 = axs[i].bar(xtic, resp)
        axs[i].set_ylabel("Students (%)")
        axs[i].set_xticks([], (""))
        set_colors_corr(bar1, val["icorrect"])

        title = letter[i] + val["title"] + "; after"
        axs[i].text(-0.5, ytext, title)
        axs[i].set_ylim([0, ymax])
        add_percentages(resp, axs[i])
        set_labels(bar1, val["labels"])
        axs[i].set_xticks(xtic, val["labels"], rotation=45)


def print_stats_cm(interv, cm_param):
    """
    Print out stats for test group and control group for the climate modeling
    module
    @param interv  pandas dataframe for test (intervention) group
    @param cm_param  The survey parameters
    """
    print("\n\n, Correct,, Change, n, Odds, P")
    print("Question, Before (%),After (%), (%), , Ratio, ")
    for key, name in cm_param.KNOW.items():
        corr = cm_param.KNOW[key]["options"][cm_param.KNOW[key]["icorrect"]]
        befpc, aftpc, chg, nstud, odds, pval = getstats(interv, key, corr)
        print(f"{key}, {befpc}, {aftpc}, {chg}, {nstud}, {odds}, {pval}")


def print_stats(
    interv, comp, polarqs: dict[str:str], statsqs: dict[str:str], know: dict
):
    """
    Print out stats for test group and control group
    @param interv  pandas dataframe for test (intervention) group
    @param comp  pandas dataframe for control (comparison) group
    @param param  Parameters describing the survey
    polarqs = param.POLARQS
    statsqs = param.STATSQS
    """

    # POLAR TEST GROUP
    print("\n\n, Correct,, Change, n, Odds, P")
    print("Question, Before (%),After (%), (%), , Ratio, ")
    for key, name in polarqs.items():
        corr = know[key]["options"][know[key]["icorrect"]]
        befpc, aftpc, chg, nstud, odds, pval = getstats(interv, key, corr)
        print(f"{name}, {befpc}, {aftpc}, {chg}, {nstud}, {odds}, {pval}")

    # POLAR CONTROL GROUP
    print("\n\n, Correct,, Change, n, Odds, P")
    print("Question, Before (%),After (%), (%), , Ratio, ")
    for key, name in polarqs.items():
        corr = know[key]["options"][know[key]["icorrect"]]
        befpc, aftpc, chg, nstud, odds, pval = getstats(comp, key, corr)
        print(f"{name}, {befpc}, {aftpc}, {chg}, {nstud}, {odds}, {pval}")

    # STATS TEST GROUP
    print("\n\n, Correct,, Change, n, Odds, P")
    print("Question, Before (%),After (%), (%), , Ratio, ")
    for key, name in statsqs.items():
        corr = know[key]["options"][know[key]["icorrect"]]
        befpc, aftpc, chg, nstud, odds, pval = getstats(interv, key, corr)
        print(f"{name}, {befpc}, {aftpc}, {chg}, {nstud}, {odds}, {pval}")

    # STATS CONTROL GROUP
    print("\n\n, Correct,, Change, n, Odds, P")
    print("Question, Before (%),After (%), (%), , Ratio, ")
    for key, name in statsqs.items():
        corr = know[key]["options"][know[key]["icorrect"]]
        befpc, aftpc, chg, nstud, odds, pval = getstats(comp, key, corr)
        print(f"{name}, {befpc}, {aftpc}, {chg}, {nstud}, {odds}, {pval}")


def make_all_plots(
    interv,
    comp,
    param,
    names: list[str],
    savefigs: bool = False,
    outdir: str = "",
):
    """
    Make all plots, including comparing test and control and for test only
    @param interv  pandas dataframe for test (intervention) group
    @param comp  pandas dataframe for control (comparison) group
    @param savefigs  Whether to save the figures
    @param outdir  Directory to save the figures to
    """

    for i in range(int(len(names) / 2)):
        plot_test_v_control(interv, comp, param, names[2 * i : 2 * (i + 1)], i)
        plt.savefig(f"{outdir}/stats_knowledge_comp{i}.png")

    plt.close("all")
    for i in range(1, 5):
        plot_4by4_bef_aft(interv, param, names[4 * (i - 1) : 4 * i], i)
        if savefigs:
            plt.savefig(f"{outdir}/stats_knowledge{i}.png")
            plt.savefig(f"{outdir}/stats_knowledge{i}.eps")


def make_demo_plots(interv, savefigs: bool = False, outdir: str = ""):
    """
    Make plots of demographics
    @param interv  pandas dataframe for test (intervention) group
    @param savefigs  Whether to save the figures
    @param outdir  Directory to save the figures to
    """

    demo_names = ["Q3", "Q4", "Q5", "Q6"]
    plot_demo(interv, demo_names, 1)
    if savefigs:
        plt.savefig(f"{outdir}/stats_demo.png")
        plt.savefig(f"{outdir}/stats_demo.eps")


def make_all_plots_cm(interv, param, savefigs: bool = False, outdir: str = ""):
    """
    Make all plots, including comparing test and control and for test only
    @param interv  pandas dataframe for test (intervention) group
    @param comp  pandas dataframe for control (comparison) group
    @param savefigs  Whether to save the figures
    @param outdir  Directory to save the figures to
    """
    names = list(param.KNOW.keys())

    plt.close("all")
    for i in range(1, 5):
        plot_4by4_bef_aft_cm(interv, param, names[4 * (i - 1) : 4 * i], i)
        if savefigs:
            plt.savefig(f"{outdir}/climate_model_knowledge{i}.png")
            plt.savefig(f"{outdir}/climate_model_knowledge_knowledge{i}.eps")


# def plot_test_v_control_bycourse(
#     intervs, comps, param, names: list[str], figno: int
# ):
#     """
#     Make plots comparing test group and control group
#     @param interv  pandas dataframe for test (intervention) group
#     @param comp  pandas dataframe for control (comparison) group
#     @param param  The survey parameters
#     @param names
#     @param  figno  desired number for figure
#     """
#     left1 = 0.08
#     left2 = 0.58
#     bot1 = 0.8
#     bot2 = 0.62
#     bot3 = 0.32
#     bot4 = 0.14
#     left = [left1, left1, left2, left2, left1, left1, left2, left2]
#     bot = [bot1, bot2, bot1, bot2, bot3, bot4, bot3, bot4]
#     wid = 0.4
#     height = 0.17
#     letter = ["a) ", "b) ", "c) ", "d) ", "e) ", "f) ", "g) ", "h) "]

#     plt.figure(figsize=(8, 8), num=figno, clear=True)
#     axs = [plt.subplot(4, 2, i + 1) for i in range(8)]
#     for i in range(8):
#         axs[i].set_position([left[i], bot[i], wid, height])

#     ytext = 108
#     ymax = 120

#     #     import pandas as pd

#     # speed = [0.1, 17.5, 40, 48, 52, 69, 88]
#     # lifespan = [2, 8, 70, 1.5, 25, 12, 28]
#     # height = [1, 5, 20, 3, 30, 6, 10]
#     # index = ['snail', 'pig', 'elephant',
#     #          'rabbit', 'giraffe', 'coyote', 'horse']
#     # df = pd.DataFrame({'speed': speed,
#     #                    'lifespan': lifespan,
#     #                    'height': height}, index=index)
#     # ax = df.plot.bar(rot=0)

#     #     df2 = resp.to_frame()
#     #     bar1 = df2.plot.bar()

#     i = -1
#     for name in names:
#         val = param.KNOW[name]
#         i += 1
#         resp = get_vals(interv[name + "_x"], val["options"])
#         xtic = np.arange(len(resp))
#         bar1 = axs[i].bar(xtic, resp)

#         title = letter[i] + val["title"] + "; before"
#         axs[i].text(-0.5, ytext, title)
#         axs[i].set_ylabel("Students (%)")
#         axs[i].set_xticks([], (""))
#         set_colors_corr(bar1, val["icorrect"])
#         axs[i].set_ylim([0, ymax])
#         add_percentages(resp, axs[i])
#         # set_labels(bar1, val["labels"])
#         # axs[i].set_xticks(xtic, val["labels"], rotation=45)
#         if i == 0:
#             axs[i].set_title("Test")

#         i += 1
#         resp = get_vals(interv[name + "_y"], val["options"])

#         # Determine bar widths
#         width_cluster = 0.7
#         n_classes = 3
#         n_series = n_classes + 1
#         width_bar = width_cluster / n_series

#         for n in range(n_series):
#             x_positions = xtic + (width_bar * n) - width_cluster / 2
#             axs[i].bar(x_positions, resp, width_bar, align="edge")

#         xtic = np.arange(len(resp))
#         bar1 = axs[i].bar(xtic, resp)
#         axs[i].set_ylabel("Students (%)")
#         axs[i].set_xticks([], (""))
#         set_colors_corr(bar1, val["icorrect"])

#         title = letter[i] + val["title"] + "; after"
#         axs[i].text(-0.5, ytext, title)
#         axs[i].set_ylim([0, ymax])
#         add_percentages(resp, axs[i])
#         set_labels(bar1, val["labels"])
#         axs[i].set_xticks(xtic, val["labels"], rotation=45)

#         i += 1
#         resp = get_vals(comp[name + "_x"], val["options"])
#         xtic = np.arange(len(resp))
#         bar1 = axs[i].bar(xtic, resp)
#         title = letter[i] + val["title"] + "; before"
#         axs[i].text(-0.5, ytext, title)
#         axs[i].set_ylabel("Students (%)")
#         axs[i].set_xticks([], (""))
#         set_colors_corr(bar1, val["icorrect"])
#         axs[i].set_ylim([0, ymax])
#         add_percentages(resp, axs[i])
#         # set_labels(bar1, val["labels"])
#         # axs[i].set_xticks(xtic, val["labels"], rotation=45)
#         if i == 2:
#             axs[i].set_title("Control")

#         i += 1
#         resp = get_vals(comp[name + "_y"], val["options"])
#         xtic = np.arange(len(resp))
#         bar1 = axs[i].bar(xtic, resp)
#         axs[i].set_ylabel("Students (%)")
#         axs[i].set_xticks([], (""))
#         set_colors_corr(bar1, val["icorrect"])

#         title = letter[i] + val["title"] + "; after"
#         axs[i].text(-0.5, ytext, title)
#         axs[i].set_ylim([0, ymax])
#         add_percentages(resp, axs[i])
#         set_labels(bar1, val["labels"])
#         axs[i].set_xticks(xtic, val["labels"], rotation=45)


# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(19680801)

# n_bins = 10
# x = np.random.randn(1000, 3)

# fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

# colors = ['red', 'tan', 'lime']
# ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
# ax0.legend(prop={'size': 10})
# ax0.set_title('bars with legend')

# ax1.hist(x, n_bins, density=True, histtype='bar', stacked=True)
# ax1.set_title('stacked bar')

# ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
# ax2.set_title('stack step (unfilled)')

# # Make a multiple-histogram of data-sets with different length.
# x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
# ax3.hist(x_multi, n_bins, histtype='bar')
# ax3.set_title('different sample sizes')

# fig.tight_layout()
# plt.show()
