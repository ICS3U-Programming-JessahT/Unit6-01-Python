#!/usr/bin/env python3
# Created By: Jessah
# Date: December 21, 2022
# the program will generate 10 random numbers
# and calculate the average of the 10 generated numbers

# import random numbers and constants
import random
import constants


def main():
    # declare variables
    list_of_int = []
    sum = 0
    counter = 0

    # use a counter to add random numbers to list
    for counter in range(constants.MAX_ARRAY_SIZE):
        rand_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        list_length = len(list_of_int)
        list_of_int.append(rand_num)
        sum = rand_num + sum
        counter = counter + 1
        # display the random number and list placement
        print("{} was added to {}".format(rand_num, list_length))

    # calculate average
    average = sum / 10

    #  display average of random numbers
    print("the average of the generated numbers is {}%".format(average))


if __name__ == "__main__":
    main()
