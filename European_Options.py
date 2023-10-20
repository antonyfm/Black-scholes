# -*- coding: utf-8 -*-
"""
@author: Antony F. M.
European Call Put Options Pricing
"""
from math import log, sqrt, exp
from scipy.stats import norm

def black_scholes_call(S0, K, t, rf, SD):
    d1 = (log(S0/K) + (rf + SD**2/2)*t)/(SD*sqrt(t))
    d2 = (log(S0/K) + (rf - SD**2/2)*t)/(SD*sqrt(t))
    
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    
    Call_price = S0 * Nd1 - K * exp(-1 * rf * t) * Nd2
    print("Call price: ", Call_price)
    return 0 

#Continuous dividend yield
def black_scholes_dividend_call(S0, K, t, rf, q, SD):
    d1 = (log(S0/K) + (rf -q + SD**2/2)*t)/(SD*sqrt(t))
    d2 = (log(S0/K) + (rf -q - SD**2/2)*t)/(SD*sqrt(t))
    
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    
    Call_dividend_price = S0 * exp(-1 * q * t) * Nd1 - K * exp(-1 * rf * t) * Nd2
    print("Call price with continuous dividend yield", Call_dividend_price)
    return 0 

def black_scholes_put(S0, K, t, rf, SD):
    d1 = (log(S0/K) + (rf + SD**2/2)*t)/(SD*sqrt(t))
    d2 = (log(S0/K) + (rf - SD**2/2)*t)/(SD*sqrt(t))
    
    Nd1 = norm.cdf(-d1)
    Nd2 = norm.cdf(-d2)
    
    Put_price = K * exp(-1 * rf * t) * Nd2 - S0 * Nd1
    print("Put price: ", Put_price)
    return 0 

#Continuous dividend yield
def black_scholes_dividend_put(S0, K, t, rf, q, SD):
    d1 = (log(S0/K) + (rf -q + SD**2/2)*t)/(SD*sqrt(t))
    d2 = (log(S0/K) + (rf -q - SD**2/2)*t)/(SD*sqrt(t))
    
    Nd1 = norm.cdf(-d1)
    Nd2 = norm.cdf(-d2)
    
    Put_dividend_price = K * exp(-1 * rf * t) * Nd2 - S0 * exp(-1 * q * t) * Nd1
    print("Put price with continuous dividend yield", Put_dividend_price)
    return 0 

black_scholes_call(23.15, 1.22, 10, 0.0525, 0.5)
black_scholes_put(23.15, 1.22, 10, 0.0525, 0.5)
black_scholes_dividend_call(23.15, 1.22, 10, 0.0525, 0.015, 0.5)
black_scholes_dividend_put(23.15, 1.22, 10, 0.0525, 0.015, 0.5)