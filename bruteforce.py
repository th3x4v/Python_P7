import itertools
from decorators import performance_decorator


@performance_decorator
def bruteforce(actions):
    """ Generate all possible combinations of stocks"""
    # Initialize variables
    max_profit = 0
    best_combination = []

    # Generate all possible combinations of stocks
    for r in range(1, len(actions) + 1):
        combinations = itertools.combinations(actions, r)

        # Iterate through each combination
        for combination in combinations:
            total_cost = sum((action['coût_par_action']) for action in combination)
            total_benefit = sum((action['coût_par_action']*action['bénéfice_après_2_ans']) for action in combination)
        

            # Check if the combination satisfies the constraints
            if total_cost <= 500 and total_benefit > max_profit:
                max_profit = total_benefit
                best_combination = combination
    # Display the best combination of purchased actions
    for action in best_combination:
        print(f"Purchased: {action['action']} (Cost: {action['coût_par_action']} euros, Benefit: {action['bénéfice_après_2_ans']})")

    print(f"\nTotal Cost: {sum((action['coût_par_action']) for action in best_combination)} euros")
    print(f"Total Benefit: {max_profit}")