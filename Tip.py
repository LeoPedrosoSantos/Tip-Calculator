print("***Tip Calculator***\n")

Bill = float(input("What is the total bill?\n"))

Percentage = float(input("What percentage tip would you like to give? 5 or 10?\n"))

PercentageP = float(Percentage / 100)

Calculator = Bill * PercentageP

Calculator2 = Calculator + Bill

People = float(input("How many people gonna split the bill?\n"))

Result = Calculator2 / People

print(f"Each person should pay {round(Result,2)}")

print(input("\nClick ENTER to close the window"))