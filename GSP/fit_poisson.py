#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:46:35 2019

@author: paragonhao
"""

# take quantile of 1.5% to 98.5%
lower = np.percentile(raw_data["bid_qty"], 1.5)
upper = np.percentile(raw_data["bid_qty"], 98.5)

bid_qty = raw_data[(raw_data.bid_qty > lower) & (raw_data.bid_qty < upper)]['bid_qty']



def poisson(k, lamb):
    """poisson pdf, parameter lamb is the fit parameter"""
    return (lamb**k/factorial(k)) * np.exp(-lamb)


def negLogLikelihood(params, data):
    """ the negative log-Likelohood-Function"""
    lnl = - np.sum(np.log(poisson(data, params[0])))
    return lnl

# minimize the negative log-Likelihood
result = minimize(negLogLikelihood,  # function to minimize
                  x0=np.ones(1),     # start value
                  args=(bid_qty,),      # additional arguments for function
                  method='Powell',   # minimization method, see docs
                  )
