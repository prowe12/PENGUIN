#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:53:21 2023

@author: prowe
"""

import matplotlib


def add_percentages(vals, axnum):
    """
    Append the plot with the percentage
    @param vals  The percentages (pandas core series)
    @param axnum  The axes to append (axes subplot)
    """
    for i, val in enumerate(vals):
        if val < 0.01:
            axnum.text(i - 0.1, val + 2, str(round(val)) + "%", fontsize=8)
        elif val < 2:
            axnum.text(i - 0.2, val + 2, str(round(val, 1)) + "%", fontsize=8)
        elif val < 10:
            axnum.text(i - 0.1, val + 2, str(round(val)) + "%", fontsize=8)
        else:
            axnum.text(i - 0.2, val + 2, str(round(val)) + "%", fontsize=8)


def set_colors(bars):
    """
    Set histogram colors to spectral
    @param bars  The matplotlib bar container
    """
    cmap = matplotlib.cm.get_cmap("Spectral")

    for i, bar_i in enumerate(bars):
        k = 0.2 + 0.2 * i
        bar_i.set_color(cmap(k)[:3])

    if len(bars) == 6:
        bars[5].set_color("m")
    elif len(bars) > 6:
        raise ValueError("not prepared for this case, modify code")

    return bars


def set_colors_corr(bars, icorr: int):
    """
    Set histogram colors to gray, except the histogram corresponding to the
    correct answer; set the correct answer histogram to blue
    @param bl  The matplotlib bar container
    @param icorr  The index to the histogram for the correct answer
    """

    for bar_i in bars:
        bar_i.set_color("gray")

    bars[icorr].set_color("blue")

    return bars


def set_labels(bars, labels: list[str]):
    """
    Set labels on histogram plot
    @param bl  The matplotlib bar container
    @param labels  The labels, 1 for each histogram bar
    """
    for bar_i, label in zip(bars, labels):
        bar_i.set_label(label)
