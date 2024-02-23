#4.
from datetime import datetime

# Input datetime1 from the user
datetime1_str = input("Enter the first datetime (YYYY-MM-DD HH:mm:ss): ")
datetime1 = datetime.strptime(datetime1_str, "%Y-%m-%d %H:%M:%S")

# Input datetime2 from the user
datetime2_str = input("Enter the second datetime (YYYY-MM-DD HH:mm:ss): ")
datetime2 = datetime.strptime(datetime2_str, "%Y-%m-%d %H:%M:%S")

# Calculate the difference in seconds
time_difference_seconds = (datetime2 - datetime1).total_seconds()

print("Time Difference in Seconds:", time_difference_seconds)