# calculating the net-worth based on just two figures
import testing

def net_worth_calculation(total_savings,total_debt):
    net_worth = total_savings - total_debt
    print(f"Your net-worth is {net_worth}")

net_worth_calculation(testing.user_savings_total, testing.user_debt_total)