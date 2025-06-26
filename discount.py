# Jaelee
# 02 Teach Activity: Calling Functions

# import datetime
from datetime import datetime
currentDate = datetime.now()
dayOfWeek = currentDate.weekday()

# user input
subtotal = float(input('Please enter the subtotal: '))

# calculation
discount = 0.9
taxRate = 0.06
discountAmt = 0
taxAmt = 0
discountSubtotal = 0
total = 0


if dayOfWeek in [1,2] and subtotal >= 50:
    discountAmt = subtotal * discount
    discountSubtotal = subtotal - discountAmt
    taxAmt = discountSubtotal * taxRate
    total = discountSubtotal + taxAmt
    print(f'Discount Amount: {discountAmt:.2f}')
else:
    taxAmt = subtotal * taxRate
    total = subtotal + taxAmt

# print
print(f'Sales Tax Amount: {taxAmt:.2f}')
print(f'Total: {total:.2f}')

