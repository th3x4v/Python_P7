import csv
from decorators import performance_decorator
from bruteforce import bruteforce
from optimised import Sorted_method
from optimised import Knapsack_method
from optimised import Simple_knapsack_method


def load_csv(file):
    """Load the actions from the CSV file"""
    actions = []
    actions_knapsack = []
    with open(file + '.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if float(row[1]) > 0 : 
                action = {
                    'action': row[0],
                    'coût_par_action': int(float(row[1]) * 100),
                    'bénéfice_après_2_ans': int(round(float(row[1]) * (float(row[2]) / 100), 2))
                }
                actions_knapsack.append(action)
                action = {
                        'action': row[0],
                        'coût_par_action': float(row[1]),
                        'bénéfice_après_2_ans': float(row[2])
                        }
                actions.append(action)

    return actions, actions_knapsack


def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Action", "Cost", "Benefit", "Total benefit", "Total cost"])
        writer.writerow(["", "", "", data[0]],"")
        writer.writerow(["", "", "", "", data[2]])
        for action in data[1]:
            writer.writerow([action['action'], action['coût_par_action'], action['bénéfice_après_2_ans']])

#optimised(load_csv("actions"))
#bruteforce(load_csv("actions"))
data1 = load_csv("dataset1_Python+P7")
data2 = load_csv("dataset2_Python+P7")
result =Sorted_method(data1[0])
write_to_csv("sorted", result)
#Sorted_method(data2[0])
#Simple_knapsack_method(data2[1])
#Simple_knapsack_method(data1[1])
#Knapsack_method(data1[1])
#Knapsack_method(data2[1])

