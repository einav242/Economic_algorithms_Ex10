# This is a sample Python script.
from typing import List
import statistics


def binary_search(c: float, choice: List[List]):
    low = 0
    high = 1

    n = len(choice[0])
    while True:
        middle = (high + low) / 2
        ans = []
        for i in range(len(choice)):
            temp_list = choice[i].copy()
            for j in range(1, n):
                temp_list.append(c * min(1, middle * j))
            ans.append(statistics.median(temp_list))
        if sum(ans) == c:
            return [round(item) for item in ans]
        elif sum(ans) > c:
            high = middle
        elif sum(ans) < c:
            low = middle


def compute_budget(total_budget: float, citizen_votes: List[List]) -> List[float]:
    choice = []
    num_of_citizen = len(citizen_votes)
    num_of_option = len(citizen_votes[0])
    for i in range(num_of_option):
        temp_list = []
        for j in range(num_of_citizen):
            temp_list.append(citizen_votes[j][i])
        choice.append(temp_list)
    return binary_search(total_budget, choice)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(compute_budget(30, [[6, 6, 6, 6, 0, 0, 6, 0, 0], [0, 0, 6, 6, 6, 6, 0, 6, 0], [6, 6, 0, 0, 6, 6, 0, 0, 6]]))
    print(compute_budget(10, [[6, 3, 1], [5, 5, 0], [3, 2, 5]]))
    print(compute_budget(100, [[100, 0, 0], [0, 0, 100]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
