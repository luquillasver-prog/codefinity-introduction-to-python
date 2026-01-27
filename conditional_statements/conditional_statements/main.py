# Input variables
product_type = "Dairy"  
day_of_week = "Wednesday"

# Si es Frutas y Lunes
if product_type == "Fruits" and day_of_week == "Monday":
    print("10% discount on Fruits today!")

# Si es Vegetales y Martes
elif product_type == "Vegetables" and day_of_week == "Tuesday":
    print("15% discount on Vegetables today!")

# Si es Lácteos y Miércoles
elif product_type == "Dairy" and day_of_week == "Wednesday":
    print("20% discount on Dairy today!")

# Si es Other (cualquier día)
elif product_type == "Other":
    print("No discount available.")

# Todos los demás casos
else:
    print("No special discounts today.")