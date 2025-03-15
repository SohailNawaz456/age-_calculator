from datetime import datetime

# Get the current year
current_year = 2025

# Ask the user for their birthdate
birth_date_str = input("Enter your birthdate (DD/MM/YYYY or DD-MM-YYYY or DD MM YYYY): ")

# Replace different separators with a standard one
birth_date_str = birth_date_str.replace("-", "/").replace(" ", "/")

try:
    # Convert input to a date object
    birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
    
    # Check if the birth year is in the future
    if birth_date.year > current_year:
        print("Error: You entered a future year! Please enter a valid birth year.")
    else:
        # Calculate age
        age = current_year - birth_date.year

        # Adjust age if the birthday hasn’t occurred yet this year
        if datetime(current_year, birth_date.month, birth_date.day) > datetime(current_year, 3, 13):
            age -= 1

        print(f"You are {age} years old. 🎉")

        # Calculate years left to 100
        years_to_100 = 100 - age
        if years_to_100 > 0:
            print(f"You have {years_to_100} years left until you turn 100. 🎂")
        else:
            print("Congratulations! You are 100 years old or older! 🎊")

except ValueError:
    print("Invalid date format! Please enter your birthdate correctly.")