# This file is meant to store all the configuration parameters for the project

# The values here are set almost randomly (up to now), feel free to change them!

import numpy as np

# Configuration parameters
ITERATIONS = 50
AUCTIONS = 10
N_USERS = 10
N_ADVERTISERS = 100    # number of companies that compete for slot auctions, including myself
NUMBER_OF_ARMS = 10    # needed for the UCB algorithm
PRICES = np.linspace(0, 1, NUMBER_OF_ARMS)    # actual arms of the ucb algorithm
BUDGET = 500
NUMBER_OF_SLOTS = 10

lambda_fun_param = lambda s: 1/(s+(0.3))       # probability of the ad being seen given the position s ->  0.5 for first position, 0.33 for second, 0.25 for third, etc...
LAMBDAS = np.array([lambda_fun_param(i) for i in range(1, NUMBER_OF_SLOTS+1)])    # array of lambda values (for each slot)

DAYS = 100 # number of rounds of the pricing algorithm