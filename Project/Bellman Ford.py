"""
This is the final project for CS5008. We build an algorithm to check for currency arbitrage.
We alter bellman ford algorithm for this
Code Author: Ifteda Ahmed-Syed
"""

import sys
import numpy as np
import pandas as pd
from itertools import combinations


broker_1 = [
    [1, 0.813157, 0.949083],
    [1.229775, 1, 1.167158],
    [1.053649, 0.856782, 1]
]
broker_2 = [
    [1, 0.813599, 0.950421],
    [1.229106, 1, 1.168168],
    [1.052165, 0.856041, 1]
]
broker_3 = [
    [1, 0.816405, 0.952551],
    [1.224882, 1, 1.166762],
    [1.049812, 0.857072, 1]
]

input_markets = ['USD', 'GBP', 'EUR']
brokers = {"Broker 1": broker_1, "Broker 2": broker_2, "Broker 3": broker_3}


def choose_best_rates(broker_rates, markets):
    if len(broker_rates) == 0:
        print("No rates given.")
        return

    rates = list(broker_rates.values())[0]
    comb = list(combinations(markets, 2))
    comb += [(item[1], item[0]) for item in comb]
    edges = dict.fromkeys(comb, list(broker_rates.keys())[0])

    for broker in list(broker_rates.keys())[1:]:
        for row in range(len(broker_rates[broker])):
            for col in range(len(broker_rates[broker][row])):
                broker_rate = broker_rates[broker][row][col]
                if broker_rate > rates[row][col]:
                    rates[row][col] = broker_rate
                    edge = (markets[row], markets[col])
                    edges[edge] = broker

    return pd.DataFrame(rates, index=markets, columns=markets), edges


def algorithm(rates, markets, source):
    rates, edges = choose_best_rates(rates, markets)

    log_rates = rates.applymap(lambda x: -np.log(x))

    distance = dict.fromkeys(rates.index, sys.maxsize)
    distance[source] = rates.index.get_loc(source)

    predecessor = dict.fromkeys(rates.index, -1)

    max_profit = 0
    reverse_optimal_path = []
    reverse_optimal_edges = []

    for i in range(len(markets) - 1):
        for start, row in log_rates.iterrows():
            for end, weight in row.iteritems():
                potential_weight = distance[start] + weight
                if potential_weight < distance[end]:
                    distance[end] = potential_weight
                    predecessor[end] = start

    for start, row in log_rates.iterrows():
        for end, weight in row.iteritems():
            potential_weight = distance[start] + weight
            if potential_weight < distance[end]:  # negative cycle detected
                reverse_negative_cycle = [source, end, start]
                reverse_negative_weights = [rates.loc[end][source], rates.loc[start][end]]
                while predecessor[start] not in reverse_negative_cycle:
                    reverse_negative_weights.append(rates.loc[predecessor[start]][reverse_negative_cycle[-1]])
                    reverse_negative_cycle.append(predecessor[start])
                    start = predecessor[start]
                if predecessor[start] is source:
                    reverse_negative_weights.append(rates.loc[predecessor[start]][reverse_negative_cycle[-1]])
                    reverse_negative_cycle.append(predecessor[start])
                    profit = np.prod(reverse_negative_weights) - 1
                    if profit > max_profit:
                        max_profit = profit
                        reverse_optimal_path = reverse_negative_cycle
                        reverse_optimal_edges = reverse_negative_weights

    if max_profit <= 0:
        print("No arbitrage opportunities for given rates and source will lead to profit.")
    else:
        path = " -> ".join(market for market in reverse_optimal_path[::-1])
        edge_path = " -> ".join(str(market) for market in reverse_optimal_edges[::-1])
        start = reverse_optimal_path[-1]
        broker_list = []
        for end in reverse_optimal_path[-2::-1]:
            broker_list.append(edges[(start, end)])
            start = end
        broker_path = " -> ".join(str(broker) for broker in broker_list)

        print("---------- OPTIMAL PATH ----------")
        print("path: " + path + "\n")
        print("rates:\n" + edge_path + "\n")
        print("broker for each transaction:\n" + broker_path + "\n")
        print("profit margin: " + '{:.14%}'.format(max_profit))


algorithm(brokers, input_markets, "EUR")
