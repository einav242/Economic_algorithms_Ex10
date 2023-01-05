# This is a sample Python script.
from typing import List
import statistics
import itertools


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


def fair_to_groups(total_budget: float, citizen_votes: List[List], result: List):
    temp = [i for i in range(len(citizen_votes))]
    comb = []
    for i in range(0, len(temp) + 1):  # to get all lengths: 0 to 3
        for subset in itertools.combinations(temp, i):
            if subset:
                comb.append(list(subset))
    comb.remove(comb[len(comb) - 1])

    for i in range(len(comb)):
        b = False
        for j in range(len(comb[i])):
            s = 0
            check = len(comb[i]) * (total_budget / len(citizen_votes))
            for item in range(len(citizen_votes[comb[i][j]])):
                if citizen_votes[comb[i][j]][item] != 0:
                    s += result[item]
            if s >= check:
                b = True
        if not b:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(compute_budget(30, [[6, 6, 6, 6, 0, 0, 6, 0, 0, 0], [0, 0, 6, 0, 6, 6, 6, 0, 6, 0],
                              [6, 6, 0, 0, 0, 6, 6, 0, 0, 6]]))
    print(compute_budget(10, [[6, 3, 1], [5, 5, 0], [3, 2, 5]]))
    print(compute_budget(100, [[100, 0, 0], [0, 0, 100]]))

    # test
    lst = [[5, 5, 10], [12, 3, 5], [1, 14, 5], [10, 10, 0], [19, 1, 0], [14, 5, 1], [1, 12, 7], [1, 12, 7], [11, 6, 3],
           [1, 17, 2]]
    print(fair_to_groups(20, lst, compute_budget(20, lst)))
    lst = [[18, 2, 0], [7, 13, 0], [14, 6, 0], [15, 0, 5], [18, 1, 1], [14, 4, 2], [11, 2, 7], [11, 3, 6], [1, 16, 3],
           [1, 7, 12]]
    print(fair_to_groups(20, lst, compute_budget(20, lst)))
    lst = [[15, 5, 0], [12, 3, 5], [11, 4, 5], [9, 10, 1], [8, 11, 1], [8, 12, 0], [2, 2, 16], [1, 13, 6], [2, 16, 2],
           [8, 2, 10]]
    print(fair_to_groups(20, lst, compute_budget(20, lst)))
    lst = [[3, 8, 11], [14, 6, 0], [15, 4, 1], [15, 3, 2], [9, 11, 0], [4, 15, 1], [11, 2, 7], [10, 3, 7], [4, 6, 10],
           [10, 10, 0]]
    print(fair_to_groups(20, lst, compute_budget(20, lst)))
