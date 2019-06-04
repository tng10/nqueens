import time
from genetic_algorithm import GeneticAlgorithm


def main():
    ga = GeneticAlgorithm()
    ga.start()


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('It has finished in', end - start, 'seconds')
