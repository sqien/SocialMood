mood_list = ["Barely holding on","Worse than usual", "Meh", "Pretty good", "Good", "Perfect"]


for elements, mood in enumerate(mood_list, start=1):
    print(f"{elements}: {mood}")
    pass

mood_input = int(input("What's your mood today, choose from the list: "))


while mood_input < 1 or mood_input > len(mood_list):
    print("You only have 6 options, buddy))")
    mood_input = int(input("What's your mood today, choose from the list: "))


print(f"You choose option: {mood_input}, which means your mood is: {mood_list[mood_input - 1]}")