#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:09:31 2019

@author: paragonhao
"""
# reference on fitting poisson distribution: https://stackoverflow.com/questions/25828184/fitting-to-poisson-histogram/25828558
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.special import factorial
from scipy.optimize import minimize
import math
import statsmodels.api as sm

# load in data and configure settings
raw_data = pd.read_csv("interview_task.csv")
pd.set_option('display.max_columns', 500)


def cal_mid_price(bid_price, bid_qty, ask_price, ask_qty):

    bid_ask_qty = bid_qty + ask_qty
    return bid_price * (ask_qty/bid_ask_qty) + ask_price * (bid_qty/bid_ask_qty)



def cal_delta(priceA, priceB):
    return priceA - priceB

def find_spread(bid, ask):
    return ask - bid


# get volume weighted mid price
raw_data['vw_ref_price'] = raw_data[['bid_price','bid_qty','ask_price','ask_qty']].apply(lambda x: cal_mid_price(x.bid_price, x.bid_qty, x.ask_price, x.ask_qty), axis = 1)

lbpercentile = 5
ubpercentile = 95

# get gamma beta 
raw_data['delta_bid'] = raw_data[['vw_ref_price','bid_price']].apply(lambda x: cal_delta(x.vw_ref_price, x.bid_price), axis = 1)
raw_data['delta_ask'] = raw_data[['vw_ref_price','ask_price']].apply(lambda x: cal_delta(x.ask_price, x.vw_ref_price), axis = 1)

# get percentile values
lower_bid = np.percentile(raw_data['delta_bid'], lbpercentile)
upper_bid = np.percentile(raw_data['delta_bid'], ubpercentile)

raw_data.loc[raw_data['delta_bid'] < lower_bid, 'delta_bid'] = lower_bid
raw_data.loc[raw_data['delta_bid'] > upper_bid, 'delta_bid'] = upper_bid


lower_ask = np.percentile(raw_data['delta_ask'], lbpercentile)
upper_ask = np.percentile(raw_data['delta_ask'], ubpercentile)

raw_data.loc[raw_data['delta_ask'] < lower_ask, 'delta_ask'] = lower_ask
raw_data.loc[raw_data['delta_ask'] > upper_ask, 'delta_ask'] = upper_ask

# qty 
bid_qty_lower = np.percentile(raw_data['bid_qty'], lbpercentile)
bid_qty_upper = np.percentile(raw_data['bid_qty'], ubpercentile)

raw_data.loc[raw_data['bid_qty'] < bid_qty_lower, 'bid_qty'] = bid_qty_lower
raw_data.loc[raw_data['bid_qty'] > bid_qty_upper, 'bid_qty'] = bid_qty_upper

ask_qty_lower = np.percentile(raw_data['ask_qty'], lbpercentile)
ask_qty_upper = np.percentile(raw_data['ask_qty'], ubpercentile)

raw_data.loc[raw_data['ask_qty'] < ask_qty_lower, 'ask_qty'] = ask_qty_lower
raw_data.loc[raw_data['ask_qty'] > ask_qty_upper, 'ask_qty'] = ask_qty_upper



# get lambda values
raw_data['lnLambda_bid'] = raw_data[['bid_qty']].apply(lambda x: 1/math.log(x.bid_qty), axis = 1)
raw_data['lnLambda_ask'] = raw_data[['ask_qty']].apply(lambda x: 1/math.log(x.ask_qty), axis = 1)

# append the two columns together 
Y = raw_data['lnLambda_bid'].append(raw_data['lnLambda_ask']).reset_index(drop=True)
X = raw_data['delta_bid'].append(raw_data['delta_ask']).reset_index(drop=True)
X = sm.add_constant(X)


model = sm.OLS(Y, X).fit() ## sm.OLS(output, input)
# in sample prediction
predictions = model.predict(X)
model.summary()




# plot 
plt.style.use('ggplot')
plt.xlabel('Qty')
plt.ylabel('Frequency')
plt.title('Bid-ask qty Histogram')
plt.hist(raw_data['bid_qty'], bins=100)
plt.hist(raw_data['ask_qty'], bins=100)

raw_data['spread'] = raw_data[['bid_price','ask_price']].apply(lambda x: find_spread(x.bid_price, x.ask_price), axis = 1)
plt.hist(raw_data['spread'], bins=100)


plt.style.use('ggplot')
plt.xlabel('delta')
plt.ylabel('lnLambda bid')
Y = raw_data['lnLambda_bid'].append(raw_data['lnLambda_ask']).reset_index(drop=True)
X = raw_data['delta_bid'].append(raw_data['delta_ask']).reset_index(drop=True)
plt.scatter(X, Y)
plt.show()




# out of sample testin
X_train = X[1:200000]
Y_train = Y[1:200000]

model_out_of_sample = sm.OLS(Y_train , X_train).fit() ## sm.OLS(output, input)
# in sample prediction
predictions_out_of_sample = model_out_of_sample.predict(X[200000:len(X)])
model_out_of_sample.summary()

sse = np.sum(np.square(np.asarray(predictions_out_of_sample) - np.mean(np.asarray(X[200000:len(X)][0]))))
sst = np.sum(np.square(np.asarray(predictions_out_of_sample) - np.asarray(X[200000:len(X)][0]))) 
r_squared = 1 - (sse/sst)
r_adj = 1 - (1-r_squared) * (200000 - 1) /(200000 - 2 - 1)




