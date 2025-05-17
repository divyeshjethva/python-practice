even_numbers = []
odd_numbers = []

# User se 5 baar input lena
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Loop ke baad ek aur input lena
choice = input("Even ya Odd likhiye (even/odd): ").strip().lower()

# Output dena user ke choice ke hisaab se
if choice == 'even':
    print("Even numbers:", even_numbers)
elif choice == 'odd':
    print("Odd numbers:", odd_numbers)
else:
    print("Galat input diya gaya. Sirf 'even' ya 'odd' likhe.")
