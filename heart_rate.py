# Jaelee Hutchinson
# 01 Checkpoint: Review Python

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# user input
age = int(input("Please enter your age: "))

# calculate range
rate_high = int((220 - age) * 0.85)
rate_low = int((220 - age) * 0.65)

# print
print('When you exercise to strengthen your heart, you should')
print(f'keep your heart rate between {rate_low} and {rate_high} beats per minute.')
