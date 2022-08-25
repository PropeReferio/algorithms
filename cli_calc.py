from dataclasses import dataclass, field
import pytest
import argparse


# Prompt: Write a command-line calculator that prompts the user to enter an
# operation (addition or multiplication), two values and then prints the
# output of the operation applied to the values

# concerns? testing?


@dataclass
class Arithmetic:
    num_1: int
    num_2: int
    operation: str
    possible_operations = ('a', 'm', 's')

    def cli_calc(self):
        operation = None
        if operation not in self.possible_operations:
            raise Exception(f'Please choose from the following operations: {self.possible_operations}')
        if operation == 'a':
            print(self.num_1 + self.num_2)
        elif operation == 'm':
            print(self.num_1 * self.num_2)
        elif operation == 's':
            print(self.num_1 - self.num_2)

    def _add(self):
        return self.num_1 + self.num_2

    # def set_two_integers(self):
    #     nums = []
    #     while len(nums) != 2:
    #         values = input('What values do you want to run the '
    #                         'operation on? 2 Integers only, separated by space. ')
    #         try:
    #             nums = list(map(lambda x: int(x), values.split(' ')))
    #         except Exception as e:
    #             raise Exception('There was a problem parsing your values. '
    #                             'Please enter them like this: 6 5')
    #     self.num_1, self.num_2 = nums[0], nums[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--operation', '-o', required=True)
    parser.add_argument('--first-num', '-f', required=True)
    parser.add_argument('--second-num', '-s', required=True)

    args = parser.parse_args()
    operation = args.operation
    first_num = args.first_num
    second_num = args.second_num

    calc = Arithmetic(first_num, second_num)
    calc.cli_calc()


main()
