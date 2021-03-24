print("Welcome to tip calculator.\n")
bill = input("What was the total bill?$\n")
tip = input("What parcent tip would you like to give? 10,12,or 15,20\n")
num_ppl = input("How many people to split the bill?\n")

total_bill = float(bill) * (1+float(tip)/100)

result = float(total_bill) / int(num_ppl)
final_result = round(result,2)
final_result ="{:.2f}".format(final_result)
message = f"Each person should pay {final_result}"

print(message)
