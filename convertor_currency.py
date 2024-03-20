bgn = 0
euro = 0
pound = 0
total = []


def show_currency():
    print("***    Select the foreign currency    ***")
    print("1. EURO")
    print("2. POUND")
    print("3. OTHER")


def selected_currency(self, choice):
    self.choice = choice
    print("Please make your choice and enter the number of the selected currency!")
    choice = int(input())
    if choice == 1:
        return "euro"
    elif choice == 2:
        return "pound"
    elif choice == 3:
        return "other"


def pound_to_bgn(line_input, exchange_rate):
    rate_pound_to_bgn = exchange_rate
    return float(line_input) * float(rate_pound_to_bgn)


def bgn_to_pound(line_input, exchange_rate):
    rate_bgn_to_pound = exchange_rate
    return float(line_input) * float(rate_bgn_to_pound)


def change_bgn_to_euro(line_input, exchange_rate):
    rate_bgn_to_euro = exchange_rate
    return float(line_input) * float(rate_bgn_to_euro)


def change_euro_to_bgn(line_input, exchange_rate):
    rate_euro_to_bgn = exchange_rate
    return float(line_input) * float(rate_euro_to_bgn)


def budget_increase():
    pass

budget = int(input('Please, enter the Budget: '))
total.append(budget)
line_input = input("Please confirm with enter to continue!")
while True:
    if __name__ == '__main__':
        show_currency()
    payment_currency = str(input('Please enter the number of the selected currency: '))

    if line_input == "stop":
        break
    else:
        if payment_currency == "1":
            line_input = input('Please, enter value: ')
            exchange_rate = input(f'Please, insert the exchange rate,\n if You need to use different currency from 1.95583.\n It bis important to use a dot! : ')
            current_sum = float(line_input)
            res = change_bgn_to_euro(current_sum, 1.95583)
            euro += float(line_input)
            bgn += res

        elif payment_currency == '2':
            line_input = input('Please, enter value: ')
            exchange_rate = input(f'Please, insert the exchange rate, \nif You need to use different currency from 1.95583.\nIt is important to use a dot! : ')
            current_sum = float(line_input)
            res = pound_to_bgn(current_sum,exchange_rate)
            print(f"The amount used in BGN is:{res:.2f}")
            pound += float(line_input)
            bgn += res
        elif payment_currency == "3":
            line_input = input('Please, enter value: ')
            exchange_rate = input('Please, insert the exchange rate, '
                                  'if You need to use different currency from 1.95583. '
                                  'It bis important to use a dot! : ')
            current_sum = float(line_input)
            res = bgn_to_pound (current_sum, exchange_rate)
            print(f"The amount used in BGN is:{res:.2f}")
            bgn += res

    if 0 < budget - bgn < budget * 10 / 100:
        remainder = budget - bgn
        print(f"WARNING!\n Only {remainder} BGN left")
        opportunities = input("If you want to continue spending, press Y, otherwise press N: ")
        if opportunities.upper() == "Y":
            add_budget = int(input("You need to supplement the budget. Please enter an amount!: "))
            total.append(add_budget)
            budget += add_budget
        else:
            break

    if budget - bgn < 0:
        remainder = abs(budget - bgn)
        print(f"WARNING!\nYou have exceeded the budget with {remainder:.2f} BGN")
        opportunities = input("If you want to continue spending, press Y, otherwise press N: ")
        if opportunities.upper() == "Y":
            add_budget = int(input("You need to supplement the budget. Please enter an amount!: "))
            total.append(add_budget)
            budget += add_budget
        else:
            break

    line_input = input('Please, press "enter" or type "stop" if you want to finish the count!')


print(f"Paid euro: {euro:.2f}")
print(f"Paid pound: {pound:.2f}")
print(f"Paid bgn: {bgn:.2f}")
total_bgn = sum(total)
available = total_bgn - bgn
print(f"Remains available : {available:.2f} BGN")
