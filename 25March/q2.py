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

def main():
    income = int(input("Enter Income: "))

    expenditures = {}
    total_expenditure = 0
    while True:
        material = input("Enter Type of Material (or 'done' to finish): ")
        if material.lower() == "done":
            break

        expense = int(input(f"Enter Expenditure on {material}: "))
  
        expenditures[material] = expenditures.get(material, 0) + expense
        
        total_expenditure += expense

    total_savings = income - total_expenditure

    print(f"\nTotal Income: {income}")
    print(f"Total Savings: {total_savings}")
    print("\nExpenditures:")

    for material, expense in expenditures.items():
        print(f"{material}: {expense}")
if __name__ == "__main__":
 main()
