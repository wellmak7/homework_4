from sys import argv

script_name, hours, earn, prem = argv

earnings = (int(hours) * int(earn)) + int(prem)

print("Заработная плата сотрудника: ", earnings)
