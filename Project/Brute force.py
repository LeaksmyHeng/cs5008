"""
This is the final project for CS5008. We build an algorithm to check for currency arbitrage.
We used brute force algorithm for this.
Code Author: Leaksmy Heng
"""

currency_arbitrage = {'USD': {'EUR': 0.951054, 'GBP': 0.81691, 'CAD': 1.344334},
                      'EUR': {'GBP': 0.858838, 'USD': 1.05138, 'CAD': 1.413512},
                      'GBP': {'USD': 1.224123, 'CAD': 1.645841, 'EUR': 1.164376},
                      'CAD': {'USD': 0.743863, 'GBP': 0.607501, 'EUR': 0.707458}
                      }

currency_arbitrage2 = {
    'USD_b1': {'EUR_b1': 0.813157, 'GBP_b1': 0.949083, 'EUR_b2': 0.950421, 'GBP_b2': 0.813599, 'EUR_b3': 0.952551,
               'GBP_b3': 0.816405},
    'EUR_b1': {'USD_b1': 1.053649, 'GBP_b1': 0.856782, 'GBP_b2': 0.856041, 'USD_b2': 0.1052165, 'GBP_b3': 0.857072,
               'USD_b3': 1.049812},
    'GBP_b1': {'USD_b1': 1.229775, 'EUR_b1': 1.167158, 'USD_b2': 1.229106, 'EUR_b2': 1.168168, 'USD_b3': 1.224882,
               'EUR_b3': 1.166762},
    'USD_b2': {'EUR_b2': 0.813599, 'GBP_b2': 0.950421, 'EUR_b3': 0.952551, 'GBP_b3': 0.816405, 'EUR_b1': 0.813157,
               'GBP_b1': 0.949083},
    'EUR_b2': {'USD_b2': 1.052165, 'GBP_b2': 0.856041, 'USD_b1': 1.053649, 'GBP_b1': 0.856782, 'USD_b3': 1.049812,
               'GBP_b3': 0.857072},
    'GBP_b2': {'USD_b2': 1.229775, 'EUR_b2': 1.167158, 'USD_b3': 1.224882, 'EUR_b3': 0.952551, 'USD_b1': 1.229775,
               'EUR_b1': 1.167158},
    'USD_b3': {'EUR_b3': 0.952551, 'GBP_b3': 0.816405, 'EUR_b2': 0.950421, 'GBP_b2': 0.813599, 'EUR_b1': 0.813157,
               'GBP_b1': 0.949083},
    'EUR_b3': {'USD_b3': 1.049812, 'GBP_b3': 0.857072, 'USD_b1': 1.053649, 'GBP_b1': 0.856782, 'GBP_b2': 0.856041,
               'USD_b2': 0.1052165},
    'GBP_b3': {'USD_b3': 1.224882, 'EUR_b3': 1.166762, 'USD_b1': 1.229775, 'EUR_b1': 1.167158, 'USD_b2': 1.229106,
               'EUR_b2': 1.168168},
}


def turn_dict_dict_to_dict_list(currency_arbitrage_graph):
    new_dict = {}
    for node in currency_arbitrage_graph:
        new_dict[node] = list(currency_arbitrage_graph[node].keys())
    return new_dict


def listed_all_cycle(graph: dict, node: str, tracking_node: list) -> list:
    graph = turn_dict_dict_to_dict_list(graph)
    node_checker = [(node, [])]
    cycle_path = []

    while node_checker:
        # checking for the last node and latest_path
        main_node, latest_path = node_checker.pop()
        if latest_path:
            # if the last element of the latest_path is the same as the tracking_node
            # -> cycle is detected hence append that latest_path to cycle_path
            if main_node in tracking_node:
                cycle_path.append(latest_path)
                yield latest_path

        # if there are no cycle detected, use the main node to check in depth (dfs structure)
        for child_node in graph[main_node]:
            if child_node not in latest_path:
                node_checker.append((child_node, latest_path + [child_node]))

    return cycle_path


def arbitrage_currency(graph, currency_head, list_head):
    all_transaction = {'path': [], 'cur_val': [], 'value': []}
    counter = 0
    ori_cycle_path = listed_all_cycle(graph, currency_head, list_head)

    # loop through the cycle path and calculate the value
    for cycle_path in ori_cycle_path:
        all_transaction['path'].append(cycle_path)
        all_transaction['cur_val'].append([])
        prev_node = currency_head
        result = 1

        for node_in_cycle in cycle_path:
            all_transaction['cur_val'][counter].append(str(graph[prev_node][node_in_cycle]))
            result = result * graph[prev_node][node_in_cycle]
            prev_node = node_in_cycle

        counter += 1

        all_transaction['value'].append(result)

    max_value = max(all_transaction['value'])
    # check if there are arbitrage opportunities exist
    if max_value > 1:
        find_max_value_position = all_transaction['value'].index(max_value)
        profit_margin = (all_transaction["value"][find_max_value_position] - 1) * 100
        # this means there is only 1 broker
        if len(list_head) == 1:
            # printing the path
            print('------------- Optimal Path ------------------')
            print('path: ' + currency_head, '->', ' -> '.join(all_transaction['path'][find_max_value_position]))
            print('rates: ' + ' -> '.join(all_transaction['cur_val'][find_max_value_position]))
            print(f'profit margin: {profit_margin}%\n')

        else:
            # printing the path
            print('------------- Optimal Path ------------------')
            transaction_path = []
            transaction_broker = []
            for transaction in all_transaction['path'][find_max_value_position]:
                split_transaction = transaction.split('_')
                transaction_path.append(split_transaction[0])
                transaction_broker.append(split_transaction[1])
            print('path: ' + currency_head.split('_')[0], '->', ' -> '.join(transaction_path))
            print('\nrates: ' + ' -> '.join(all_transaction['cur_val'][find_max_value_position]))
            print('\nbroker for each transaction:\n' + ' -> '.join(transaction_broker))
            print(f'\nprofit margin: {profit_margin}%')

        return all_transaction['path'][find_max_value_position], all_transaction['cur_val'][find_max_value_position], \
               all_transaction['value'][find_max_value_position]

    return 'No arbitrage opportunities is detected'


if __name__ == '__main__':
    arbitrage_currency(currency_arbitrage, 'USD', ['USD'])
    arbitrage_currency(currency_arbitrage2, 'EUR_b1', ['EUR_b1', 'EUR_b2', 'EUR_b3'])
