dict_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15}
dict_not_dec = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def from_dec(number, system):
    number = int(number)
    answer = ''
    while number > 0:
        answer += dict_not_dec[number % system]
        number //= system
    return answer[::-1]


def to_dec(number, system):
    number = str(number)[::-1]
    count = -1
    answer = 0
    while len(number) > 0:
        count += 1
        answer += dict_dec[number[0]] * system ** count
        number = number[::-1][:len(number) - 1][::-1]
    return answer


def main():
    number = input("Number: ")
    request = input("to decimal/from decimal/to any: ")
    if request == "to decimal":
        system = int(input("System: "))
        print("Your {0} from {1} system to decimal is {2}".format(number, system, to_dec(number, system)))
    elif request == "from decimal":
        system = int(input("System: "))
        print("Your {0} from decimal system to {1} system is {2}".format(number, system,
                                                                         from_dec(number, system)))
    elif request == "to any":
        old_system = int(input("old system: "))
        new_system = int(input("new system: "))
        print("Your {0} from old system {1} to new system {2} is {3}"
              .format(number, old_system, new_system, from_dec(to_dec(number, old_system), new_system)))
    answer = input("Would you like calculate again? (yes/no): ")
    if answer == "yes":
        main()
    elif answer == "no":
        print("Have a nice day!")


main()
