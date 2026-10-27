# HerbNutri - Herbal and Nutrition Management System

def display_menu():
    print("\n================================")
    print("   HERBNUTRI MANAGEMENT SYSTEM")
    print("================================")
    print("1. Herbal Information")
    print("2. Nutrition Information")
    print("3. Healthy Food Suggestions")
    print("4. Daily Health Tips")
    print("5. About Project")
    print("6. Exit")


def herbal_information():
    print("\n--- HERBAL INFORMATION ---")
    print("1. Tulsi - Traditionally used in herbal remedies")
    print("2. Neem - Commonly used in traditional skincare")
    print("3. Aloe Vera - Used in skincare products")
    print("4. Turmeric - Commonly used as a food spice")
    print("5. Ginger - Used in food and traditional remedies")


def nutrition_information():
    print("\n--- NUTRITION INFORMATION ---")
    print("1. Carbohydrates - Provide energy")
    print("2. Proteins - Help growth and tissue repair")
    print("3. Vitamins - Support normal body functions")
    print("4. Minerals - Support bones and body functions")
    print("5. Fats - Provide energy and support cell functions")
    print("6. Water - Helps maintain hydration")


def healthy_food():
    print("\n--- HEALTHY FOOD SUGGESTIONS ---")
    print("1. Fruits - Apple, Banana, Orange")
    print("2. Vegetables - Spinach, Carrot, Broccoli")
    print("3. Protein Foods - Dal, Beans, Milk")
    print("4. Whole Grains - Rice, Oats, Roti")
    print("5. Nuts - Almonds, Walnuts")


def health_tips():
    print("\n--- DAILY HEALTH TIPS ---")
    print("1. Eat a balanced diet.")
    print("2. Drink enough water.")
    print("3. Include fruits and vegetables.")
    print("4. Maintain regular sleep.")
    print("5. Stay physically active.")
    print("6. Maintain personal hygiene.")


def about_project():
    print("\n--- ABOUT HERBNUTRI ---")
    print("Project Name: Herbal and Nutrition Management System")
    print("Developed Using: Python")
    print("Purpose: To spread awareness about herbs and nutrition.")
    print("This project provides basic health and food information.")


# Main Program
while True:
    display_menu()

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        herbal_information()

    elif choice == "2":
        nutrition_information()

    elif choice == "3":
        healthy_food()

    elif choice == "4":
        health_tips()

    elif choice == "5":
        about_project()

    elif choice == "6":
        print("\nThank you for using HerbNutri!")
        print("Stay Healthy, Stay Happy!")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 6.")
