dis = int(input("how many kilometers you drive per weeK? "))
dev = int(input("how many hours you use electronic devices per day? "))
plastic = int(input("how many plastic items you use per day? "))

carbon_score = (dis * 0.21) + (dev * 0.05 * 7) + (plastic * 0.1 * 7)

if carbon_score < 20:
    print(f"Your carbon score is {carbon_score}. Excellent! Your carbon footprint is low. ")
elif carbon_score <= 20 and carbon_score > 50:
    print(f"Your carbon score is {carbon_score}. Moderate. consider improving some habits. ")
else:
    print(f"Your carbon score is {carbon_score}. High carbon footprint. Let's make more eco-friendly chocies. ")
    