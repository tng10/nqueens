import time
from statistics import mean

from genetic_algorithm import GeneticAlgorithm


def main():
    ga = GeneticAlgorithm()
    ga.start()
    return ga.has_goal()


if __name__ == '__main__':
    execution_time = []
    goals = []

    for i in range(10):
        start = time.time()
        result = main()
        end = time.time()
        execution_time.append(end - start)
        if result:
            goals.append(1)
        else:
            goals.append(0)

    print('Average time is', mean(execution_time), 'seconds')
    print('Goals reached are', mean(goals) * 100, '%')
