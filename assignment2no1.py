from datetime import datetime, timedelta

def main():
    # Read the number of days from the user
    days = int(input("Enter the number of days from now: "))

    # Get the current date
    current_date = datetime.now()

    # Calculate the date after the given number of days
    future_date = current_date + timedelta(days=days)

    # Format the future date as desired
    formatted_date = future_date.strftime("%A, %B %d, %Y")

    # Print the formatted future date
    print("The date", days, "days from now will be:", formatted_date)

if __name__ == "__main__":
    main()
