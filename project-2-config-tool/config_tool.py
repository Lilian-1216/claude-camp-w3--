import json

with open("config.json", "r") as f:
    config = json.load(f)

print("Current settings:")
for key, value in config.items():
    print(f"  {key}: {value}")

key_to_change = input("\nWhich setting would you like to change? (theme/language/font_size): ")

if key_to_change not in config:
    print("❌ Not a valid setting.") 

elif key_to_change == "font_size":
    while True:
        user_input = input("New font_size (8-32, or 'q' to quit): ")
        
        if user_input == "q":
            print("Cancelled.")
            break    
    
        try:
            new_value = int(user_input)
            if 8 <= new_value <= 32:
                config["font_size"] = new_value
                print(f"✅ Changed to {new_value}")
                break    
            else:
                print("❌ Must be between 8 and 32, try again.")
        except ValueError:
            print("❌ Must be a number, try again.")
else:
    
    new_value = input(f"New {key_to_change}: ")
    config[key_to_change] = new_value
    print(f"✅ {key_to_change} has been changed to {new_value}")

with open("config.json", "w") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print("✅ Settings saved successfully!")

