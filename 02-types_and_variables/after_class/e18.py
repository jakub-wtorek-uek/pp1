# 18. In interactive mode, calculate and display your height in feet and inches.
# Sample result: I am 170cm tall, i.e. 5 feet and 7 inches.

CM_IN_FOOT = 30.48
INCH_IN_CM = 0.393700787

height = 170
height_copy = height

foot_count = 0

while height_copy > CM_IN_FOOT:
    foot_count += 1
    height_copy -= CM_IN_FOOT

reminder_in_inch = int(round(height_copy * INCH_IN_CM, 0))

print(
    f"I am {height}cm tall, i.e. {foot_count} feet and {reminder_in_inch} inches.")
