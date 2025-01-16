def build_list():
    list1 = []
    flag = True

    while flag:
        user_input = input("Enter a number (Done to exit out): ")
        if user_input == "Done":
            flag = False
        else:
            try:
                list1.append(int(user_input))
            except ValueError:
                print("Please enter a number.")

    return list1


def sort_list(unsortedList):
    unsortedList.sort()
    return unsortedList


if __name__ == "__main__":
    list1 = build_list()
    print(list1)
    sorted_list = sort_list(list1)
    print(sorted_list)