name = str(input("Enter your name: "))
age = int(input("Enter your age:" ))
height = float(input("Enter your height in meters: "))
fav_number = int(input("Enter your favorite number: "))
height_in_cm = int(height * 100)
card_title= "Your profile card"

print("==============================")
print(f"{card_title.upper():^30}")
print("==============================")
print(

f"{'Name:':}             {name:}\n"
f"{'Age:':}              {age:}\n"
f"{'Height:':}           {height:}m ({height_in_cm:}cm)\n"
f"{'Favourite Number:':} {fav_number:}\n"
"=============================="

)
