if __name__ == "__main__":
    # # task 1
    # while True:
    #     try:
    #         x = int(input("type 1st number"))
    #         y = int(input("type 2st number"))
    #         print(f"{x}**{y}={x**y}")
    #         break
    #     except ValueError:
    #         print("type int number")

    # task 2

    # count = 0
    #
    # for digit in range(10):
    #     for other_digit in range(10):
    #         if digit != other_digit:
    #             for _ in range(3):
    #                 count += 1
    #
    # print(count)
    # def count_numbers_with_unique_digits(start, end):
    #     total_count = end - start + 1
    #
    #     same_digit_count = 0
    #     for digit in range(1, 10):
    #         same_digit_count += 1
    #
    #     two_same_digits_count = 0
    #     for digit1 in range(1, 10):
    #         for digit2 in range(10):
    #             if digit1 != digit2:
    #                 two_same_digits_count += 1
    #
    #     unique_digits_count = total_count - (same_digit_count + two_same_digits_count)
    #
    #     return unique_digits_count
    #
    #
    # start_range = 100
    # end_range = 9999
    # result = count_numbers_with_unique_digits(start_range, end_range)
    # print(result)
    print("Type an integer number:")
    while True:
        try:
            number = int(input())
            break
        except ValueError:
            print("Type an integer number!")

    number_arr = []
    number_str = str(number)
    for i in number_str:
        number_arr.append(i)

    number_arr_filtered = [digit for digit in number_arr if digit != "3" and digit != "6"]
    print(number_arr_filtered)




