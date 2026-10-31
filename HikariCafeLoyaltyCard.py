"""Manage cafe loyalty stamps and takeout prices."""


class HikariCafe:
    """Represent Hikari Cafe loyalty card system."""

    cafe_name = "Hikari Cafe"
    stamps_needed = 5

    def __init__(self, name):
        """Initialize customer information and loyalty stamps."""
        self.name = name
        self.stamps = 0
        print(f"Welcome to {HikariCafe.cafe_name}, {self.name}!")

    def buy_coffee(self):
        """Add a stamp and reward free coffee after five stamps."""
        self.stamps += 1

        if self.stamps == HikariCafe.stamps_needed:
            print("Congratulations! You earned a free coffee!")
            self.stamps = 0
            print("Your loyalty card has been reset.")
        else:
            remaining = HikariCafe.stamps_needed - self.stamps
            print(f"Stamp collected: {self.stamps}/{HikariCafe.stamps_needed}")
            print(f"{remaining} more stamps until your free coffee.")

    @staticmethod
    def takeout_price(price):
        """Calculate takeout price including 8% consumption tax."""
        return round(price * 1.08)


# Get customer information
name = input("Enter customer name: ")

# Create customer object
customer = HikariCafe(name)

# Buy coffee
while True:
    choice = input("\nDo you want to buy coffee? (yes/no): ").lower()

    if choice == "no":
        break
    elif choice == "yes":
        customer.buy_coffee()
    else:
        print("Please enter yes or no.")

# Calculate takeout price
price = float(input("\nEnter takeout coffee price: "))

final_price = HikariCafe.takeout_price(price)

print(f"Takeout price including 8% tax: ¥{final_price}")