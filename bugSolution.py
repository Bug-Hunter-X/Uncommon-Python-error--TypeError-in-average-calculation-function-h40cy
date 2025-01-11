def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage (demonstrating the fix):
my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: The average is: 0

my_numbers = [10, 20, 30]
result = calculate_average(my_numbers)
print(f"The average is: {result}")  # Output: The average is: 20.0

my_numbers = [10, 20, 'a']
result = calculate_average(my_numbers) # Output: The average is: 20.0

my_numbers = ['a', 'b', 'c']
result = calculate_average(my_numbers) # Output: The average is: 0