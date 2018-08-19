age = 77

if age < 4:
    # print("Your admission cost is $.0.")
    prince = 0
elif age < 18:
    # print("Your admission cost is $5.")
    prince = 5
elif age < 65:
    prince = 10
elif age >= 65:
    # print("Your admission cost is $10.")
    prince = 5

print("Your admission cost is $" + str(prince) + ".")