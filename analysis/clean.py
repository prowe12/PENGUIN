#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:12:34 2023

@author: prowe
"""
# Built-in modules
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'


def load(fname: str):
    """
    Load excel-type file fname and return pandas dataframe
    @param fname  The excel-type filename
    @returns pandas dataframe
    """
    return pd.read_excel(fname, header=[0], skiprows=[1])


def getcols(dfi, col: list[str]):
    """
    Return pandas dataframe for the specified column
    @param dfi  The dataframe
    @param col  The column header
    @returns  Pandas dataframe
    """
    return dfi[col]


def rename(dfo, old_n_new_names):
    """
    Rename specified columns to specified names
    @param  dfo  The dataframe
    @param old_n_new_names  A dictionary w old names as keys, new as values
    """
    dfo.rename(columns=old_n_new_names, inplace=True)


def filter_out_minors(dfo, age: str):
    """
    Keep only results for students over 18
    @param dfo  The dataframe
    @param age  Column with Yes/No for over 18
    @returns  The filtered dataframe
    """
    return dfo[dfo[age] == "Yes"]


def sort_by_id(dfi, sid: list[str]):
    """
    Sort respondes by student id
    @param dfi  The dataframe
    @param sid  The column with the student id
    @returns  The sorted dataframe
    """
    return dfi.sort_values(sid)


def clean_ids(dfo, sid0: str):
    """
    Return dataframe with only the rows where the ids are not nan,
    after converting ids from float to int
    and convert the student id and days to ints
    @params dfo  Dataframe of survey results
    @params sid0  Column header for student id
    @returns Pandas dataframe
    """
    dfo = dfo.dropna(subset=sid0)
    dfo[sid0] = dfo[sid0].astype(int)
    return dfo


def student_ids_unique(dfo, sid: str):
    """
    Make sure the student id uniquely identifies each student
    @param dfo  The dataframe
    @param sid  The columns with the identifiers
    """
    if dfo[sid[0]].dtype != "O":
        dfsid = dfo[sid[0]].astype(str)
    else:
        dfsid = dfo[sid[0]]

    for sid0 in sid[1:]:
        if dfo[sid0].dtype != "0":
            dfsid += dfo[sid0].astype(str)
        else:
            dfsid += dfo[sid0]

    if not dfsid.is_unique:
        print(dfsid)
        raise ValueError("All partial IDs are not unique!")


def remove_symbols(dfo):
    """
    Remove undesired symbols from all responses (in place)
    @params dfo  The input dataframe
    """
    # Remove all symbols but the following
    dfo.replace(r"[^\w\s\-\.\,\/\(\)]|_", "", regex=True, inplace=True)
    # Remove bad characters
    dfo.replace(r"[â€œ]", "", regex=True, inplace=True)
    dfo.replace(r"â", "", regex=True, inplace=True)
    dfo.replace(r"â€", "", regex=True, inplace=True)
    # Remove period in "Not sure." because sometimes its there ,sometimes not
    dfo.replace(r"Not sure.", "Not sure", regex=True, inplace=True)


def clean_single(fname: str, col: list[str], age: str, names: dict):
    """
    Return dataframe from a survey file after cleaning
    @param  fname  File to load in
    @param col  Columns to keep
    @param age  Header for column giving whether over 18
    @param  names  Identifying questions (for matching pre and post)
    @returns pandas dataframe
    """
    dfo = load(fname)
    dfo = getcols(dfo, col)
    rename(dfo, names)
    dfo = filter_out_minors(dfo, age)
    dfo = clean_ids(dfo, "sid")
    dfo = sort_by_id(dfo, "sid")
    student_ids_unique(dfo, ["sid", "month", "day"])
    remove_symbols(dfo)  # Done in place
    return dfo


def clean_single_cm(fname: str, age: str, names: dict):
    """
    Return dataframe from a survey file after cleaning
    @param  fname  File to load in
    @param col  Columns to keep
    @param age  Header for column giving whether over 18
    @param  names  Identifying questions (for matching pre and post)
    @returns pandas dataframe
    """
    cols = [age] + list(names.keys())
    dfo = load(fname)
    dfo = getcols(dfo, cols)
    rename(dfo, names)
    dfo = filter_out_minors(dfo, age)
    dfo = clean_ids(dfo, "sid")
    dfo = sort_by_id(dfo, "sid")
    student_ids_unique(dfo, ["sid", "month", "day"])
    remove_symbols(dfo)  # Done in place
    return dfo


def clean_climate_modeling(prm):
    """
    Return a dataframe containing selected columns from cleaned and matched
    pre and post survey files
    @param prm  Parameters for the survey, specified in a param file (class)
    @returns pandas dataframe
    """

    # Columns to use: Age column (18 or over?), knowledge questions, and
    # identifying questions (to match pre/post tests)
    # col_pre = [prm.AGE] + list(group["pre"].values())
    # col_post = [prm.AGE] + list(group["pre"].values())

    # Load and clean
    res = []
    for group in prm.DATA:

        # Get the pre and post
        print(group["pre_file"])
        pre = clean_single_cm(group["pre_file"], prm.AGE, group["pre"])
        print(group["post_file"])
        post = clean_single_cm(group["post_file"], prm.AGE, group["post"])

        # Merge pre and post and append to list of results
        res.append(
            pd.merge(pre, post, on=["sid", "month", "day"], how="inner")
        )

    # Merge into one big dataframe and return
    return pd.concat(res)


def clean(files, age, know, qpre, qpost):
    """
    Return a dataframe containing selected columns from cleaned and matched
    pre and post survey files
    @param prm  Parameters for the survey, specified in a param file (class)
    @returns pandas dataframe

    # Columns to use: Age column (18 or over?), knowledge questions, and
    # identifying questions (to match pre/post tests)
    col_pre = [prm.AGE] + list(prm.KNOW.keys()) + list(prm.QPRE.keys())
    col_post = [prm.AGE] + list(prm.KNOW.keys()) + list(prm.QPOST.keys())
    files = prm.FILES
    """

    # Columns to use: Age column (18 or over?), knowledge questions, and
    # identifying questions (to match pre/post tests)
    col_pre = [age] + list(know.keys()) + list(qpre.keys())
    col_post = [age] + list(know.keys()) + list(qpost.keys())

    # Load and clean
    res = []
    for fname in files:
        print(fname["pre_file"])
        # Get the pre and post
        pre = clean_single(fname["pre_file"], col_pre, age, qpre)
        post = clean_single(fname["post_file"], col_post, age, qpost)
        # Merge pre and post and append to list of results
        res.append(
            pd.merge(pre, post, on=["sid", "month", "day"], how="inner")
        )

    # Merge into one big dataframe and return
    return pd.concat(res)


# pre0, post0 = get_matching(pre0, post0, prm.SID_PRE[0], prm.SID_POST[0])
# pres.append(pre0)
# posts.append(post0)
# pre = pd.concat(pres)
# post = pd.concat(posts)

# # Sort (again)
# pre = sort_by_id(pre, prm.SID_PRE)
# post = sort_by_id(post, prm.SID_POST)


# def get_matching(pre, post, ipre_id, ipost_id):
#     """
#     Get the pre and post where they match
#     """
#     ikeep = []
#     for i, sid in enumerate(pre[ipre_id]):
#         if sid in post[ipost_id]:
#             ikeep.append(i)
#         print(f"{presid}, {postsid}")
#     return pre, post
