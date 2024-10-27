def calculate_attendance(total_classes, attended_classes):
    if total_classes == 0:
        return 0  # Avoid division by zero
    attendance_percentage = (attended_classes / total_classes) * 100
    return attendance_percentage

# Input from the user
total_classes = int(input("Enter the total number of classes held: "))
attended_classes = int(input("Enter the number of classes attended: "))

# Calculate attendance
attendance_percentage = calculate_attendance(total_classes, attended_classes)

# Display results
print(f"Your attendance percentage is: {attendance_percentage:.2f}%")

# Check if eligible based on a minimum requirement
minimum_percentage = 75  # Example threshold
if attendance_percentage >= minimum_percentage:
    print("You meet the minimum attendance requirement.")
else:
    print("You do not meet the minimum attendance requirement.")
