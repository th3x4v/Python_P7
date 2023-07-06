from decorators import performance_decorator


@performance_decorator
def Sorted_method(actions):
    """Sort the actions by descending order of benefit"""
    sorted_actions = sorted(actions, key=lambda x: x['bénéfice_après_2_ans'], reverse=True)
    # Initialize variables
    budget_remaining = 500
    actions_purchased = []

    # Iterate through the sorted actions
    for action in sorted_actions:
        if action['coût_par_action'] <= budget_remaining:
            actions_purchased.append(action)
            budget_remaining -= action['coût_par_action']

    # Display the purchased actions
    total_purchase = 0
    total_benefit = 0
    for action in actions_purchased:
        benefit = action['coût_par_action']*action['bénéfice_après_2_ans']/100
        total_purchase = total_purchase + action['coût_par_action']
        total_benefit = total_benefit + benefit
        print(f"Purchased: {action['action']} (Cost: {action['coût_par_action']} euros, Benefit: {action['bénéfice_après_2_ans']})")

    print(total_benefit)
    print(total_purchase)
    return total_benefit,actions_purchased, total_purchase

@performance_decorator
def Knapsack_method(actions):
    """Knapsack Problem with Dynamic Memory Allocation"""
    #sorted(actions, key=lambda x: x['bénéfice_après_2_ans'], reverse=True)
    # Initialize variables
    max_cost = 50000
    actions_purchased = []
    
    # Create a 2D array to store the maximum benefit for each budget and number of actions
    dp = [[0] * (max_cost + 1) for _ in range(len(actions) + 1)]
    
    # Iterate through the sorted actions
    for i in range(1, len(actions) + 1):
        for j in range(1, max_cost + 1):
            action = actions[i - 1]
            if action['coût_par_action'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - action['coût_par_action']] + action['bénéfice_après_2_ans'])
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Find the actions to purchase
    j = max_cost
    for i in range(len(actions), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            action = actions[i - 1]
            actions_purchased.append(action)
            j -= action['coût_par_action']
    
    # Display the purchased actions
    total_purchase = 0
    total_benefit = 0
    for action in actions_purchased:
        benefit = action['bénéfice_après_2_ans']
        total_purchase += action['coût_par_action']
        total_benefit += action['bénéfice_après_2_ans']
        print(f"Purchased: {action['action']} (Cost: {action['coût_par_action']/100} euros, Benefit: {benefit})")
    
    print(total_benefit)
    print(total_purchase/100)
    return total_benefit,actions_purchased, total_purchase

@performance_decorator
def Simple_knapsack_method(actions):
    max_cost=50000
    n = len(actions)
    dp = [[0] * (max_cost + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = actions[i - 1]['coût_par_action']
        benefit = actions[i - 1]['bénéfice_après_2_ans']
        for j in range(1, max_cost + 1):
            if cost <= j:
                dp[i][j] = max(benefit + dp[i - 1][j - cost], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    max_benefit = dp[n][max_cost]

    actions_purchased = []
    j = max_cost
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            actions_purchased.append(actions[i - 1])
            j -= actions[i - 1]['coût_par_action']

    # Display the purchased actions
    total_purchase = 0
    total_benefit = 0
    for action in actions_purchased:
        benefit = action['bénéfice_après_2_ans']
        total_purchase += action['coût_par_action']
        total_benefit += action['bénéfice_après_2_ans']
        print(f"Purchased: {action['action']} (Cost: {action['coût_par_action']/100} euros, Benefit: {benefit})")
    
    print(total_benefit)
    print(total_purchase/100)
    return total_benefit,actions_purchased,total_purchase
