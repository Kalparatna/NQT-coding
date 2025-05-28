'''
Write a program that continuously takes user input for the following details:

1. Income (amount earned).
2. Type of Material (category of expenditure).
3. Expenditure on that Material (amount spent).
The input process continues until the user enters "done".
After the input process is complete, the program should:
. Display the total income.
. Calculate and display the total savings (i.e., Income - Total Expenditure).
· List all expenditures (showing where the money was spent and how much).

INPUT:
Income: 5000
Type of Material: Food
Expenditure: 100

Type of Material: Mobile
Expenditure: 200

Type of Material: Electricity
Expenditure: 500

Then the user enters "done" 

EXPETCETD OUTPUT:

Total Income: 5000
Total Savings: 4200
Expenditures :
Food: 100
Mobile: 200
Electricity: 500

'''


income = int(input())
total_income = income
expenses = {}
total_exp = 0
while True:
    Type_of_material = input()
    if Type_of_material.lower() =='done':
        break
    else:
        exp =int(input())
        expenses[Type_of_material] = expenses.get(Type_of_material, 0) + exp
        total_exp += exp
    

total_savings = total_income - total_exp

print("Total Income", income)
print("Total Savings", total_savings)

for Type_of_material, exp in expenses.items():
    print(Type_of_material, ":", exp)
