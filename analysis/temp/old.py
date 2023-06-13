#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:15:13 2023

@author: prowe
"""

names = {
    "Q5": "Fastest-warming region",
    "Q7": "Reconstructing past temps",
    "Q8": "Last million years mostly",
    "Q6": "Length ice core record",
    "Q10": "ID plot of CO2 vs temp",
    "Q11": "ID plot of CO2 vs temp",
    "Q12": "ID plot of CO2 vs temp",
    "Q19": "Polar Amp. primary cause",
    "Q15": "Neg lin assoc",
    "Q13": "No/mod/perf lin. assoc",
    "Q4": "Ave relationship x vs y",
    "Q3": "Prediction outside range",
    "Q14": "Use of lin reg",
    "Q16": "Evidence of causation",
}

# OBSOLETE CODE
#
# def print_results(inds):
#     print(",                          test , control")
#     for key, name in names.items():
#         diff0 = round(aft[key] - bef[key])
#         cdiff0 = round(caft[key] - cbef[key])
#         odds = round(pvalue[key][0])
#         codds = round(cpvalue[key][0])
#         pval = pvalue[key][1]
#         cpval = cpvalue[key][1]
#         print(f"{name}")
#         print("  Before correct (%%), %8d, %5d" % (bef[key], cbef[key]))
#         print("  After correct (%%), %9d, %5d" % (aft[key], caft[key]))
#         print("  Improvement (%%), %11d, %5d" % (diff0, cdiff0))
#         print("  n, %23d, %5d" % (nstudents[key], cnstudents[key]))
#         print("  Odds ratio, %16d, %5d" % (odds, codds))
#         if pval < 0.01 and cpval < 0.01:
#             print(f"  P,                        <0.01, <0.01")
#         elif pval < 0.01 and cpval >= 0.01:
#             print(f"  P,                        <0.01, %5.2f" % (cpval))
#         elif pval >= 0.01 and cpval < 0.01:
#             print(f"  P,                        {round(pval,2)},  <0.01")
#         else:
#             print("  P, %28.2f, %5.2f" % (pval, cpval))


# bef = {}
# aft = {}
# cbef = {}
# caft = {}
# pvalue = {}
# cpvalue = {}
# nstud = {}
# cnstud = {}
# for name in names:
#     val = param.KNOW[name]
#     corr = val["options"][val["icorrect"]]
#     # Test/intervention group
#     bef_corr, bef_wrong = get_num_correct(interv[name + "_x"], corr)
#     aft_corr, aft_wrong = get_num_correct(interv[name + "_y"], corr)
#     print(
#         f"number students bef vs after {bef_corr + bef_wrong}, {aft_corr + aft_wrong}"
#     )
#     print()
#     nstud[name] = bef_corr + bef_wrong
#     bef[name] = 100 * bef_corr / (bef_corr + bef_wrong)
#     aft[name] = 100 * aft_corr / (aft_corr + aft_wrong)
#     # data = [[pcbef_wrong, pcaft_wrong], [pcbef_corr, pcaft_corr]]
#     data = [
#         [aft_corr, aft_wrong],
#         [bef_corr, bef_wrong],
#     ]
#     # print(f"{name}:")
#     # print(data)
#     pvalue[name] = stats.fisher_exact(data)

#     # Control/comparison group
#     bef_corr, bef_wrong = get_num_correct(comp[name + "_x"], corr)
#     aft_corr, aft_wrong = get_num_correct(comp[name + "_y"], corr)
#     print(
#         f"control: number students bef vs after {bef_corr + bef_wrong}, {aft_corr + aft_wrong}"
#     )
#     print()
#     cnstud[name] = bef_corr + bef_wrong
#     cbef[name] = 100 * bef_corr / (bef_corr + bef_wrong)
#     caft[name] = 100 * aft_corr / (aft_corr + aft_wrong)
#     # data = [[pcbef_wrong, pcaft_wrong], [pcbef_corr, pcaft_corr]]
#     data = [
#         [aft_corr, aft_wrong],
#         [bef_corr, bef_wrong],
#     ]
#     cpvalue[name] = stats.fisher_exact(data)

# print("                          test  control")
# for key, name in names.items():
#     diff0 = round(aft[key] - bef[key])
#     cdiff0 = round(caft[key] - cbef[key])
#     odds = round(pvalue[key][0])
#     codds = round(cpvalue[key][0])
#     pval = pvalue[key][1]
#     cpval = cpvalue[key][1]
#     print(f"{name}")
#     print("  Before correct (%%) %8d %5d" % (bef[key], cbef[key]))
#     print("  After correct (%%) %9d %5d" % (aft[key], caft[key]))
#     print("  Improvement (%%) %11d %5d" % (diff0, cdiff0))
#     print("  n %23d %5d" % (nstudents[key], cnstudents[key]))
#     print("  Odds ratio %16d %5d" % (odds, codds))
#     if pval < 0.01 and cpval < 0.01:
#         print(f"  P                        <0.01 <0.01")
#     elif pval < 0.01 and cpval >= 0.01:
#         print(f"  P                        <0.01 %5.2f" % (cpval))
#     elif pval >= 0.01 and cpval < 0.01:
#         print(f"  P                        {round(pval,2)}  <0.01")
#     else:
#         print("  P %28.2f %5.2f" % (pval, cpval))
#     # print(f"  P                  {round(pval,2)}  {round(cpval,2)}")
