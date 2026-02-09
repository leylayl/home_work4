import json
import os
from datetime import datetime

class AnimalAndHug:
    def __init__(self):
        # Configuration: File name for our professional JSON database
        self.file_name = "animal_hug_data.json"
        self.data = self.load_database()

    def load_database(self):
        """ LOADING: This function reads the JSON file or creates a new one. """
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except:
                return self.get_empty_structure()
        return self.get_empty_structure()

    def get_empty_structure(self):
        """ DEFAULT: If no file exists, we start with this structure. """
        return {"residents": [], "happy_tails": [], "donations": 0}

    def save_database(self):
        """ SAVING: Writes current database state into the JSON file. """
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def add_pet(self, name, species, is_urgent):
        """ REGISTRATION: Adds a pet with a specific portrait and reason. """
        urgent_reason = "N/A"
        if is_urgent:
            # New feature: Asking for the reason of urgency
            urgent_reason = input("⚠️  Why is it urgent? (Reason): ")

        # Generating ASCII portrait based on species for the JSON file
        if "dog" in species.lower():
            icon = "🐶"
            portrait = "  __   _  \n (o o) /  \n  (V)    " 
        elif "cat" in species.lower():
            icon = "🐱"
            portrait = "  ^ ^     \n (o o)    \n  (W)     " 
        else:
            icon = "🐾"
            portrait = "  / \     \n ( @ )    \n  \ /     "

        # Creating a detailed dictionary (Object) for our database
        new_pet = {
            "name": name,
            "species": species,
            "portrait": portrait, # This "image" will be stored in your JSON
            "status": {
                "is_urgent": is_urgent,
                "reason": urgent_reason,
                "vibe": "Waiting for Love 💖",
                "health": "Verified ✅"
            },
            "technical_info": {
                "icon": icon,
                "entry_date": datetime.now().strftime("%d %b %Y | %H:%M"),
                "id": f"HUG-{datetime.now().strftime('%S%f')[:5]}"
            }
        }
        self.data["residents"].append(new_pet)
        self.save_database()
        print(f"\n✨ {icon} {name} is registered! Portrait saved to JSON.")

    def give_a_hug(self, name):
        """ ADOPTION: Transfers a pet from 'residents' to 'happy_tails'. """
        for pet in self.data["residents"]:
            if pet["name"].lower() == name.lower():
                pet["status"]["vibe"] = "Adopted & Happy! 🏠"
                self.data["happy_tails"].append(pet)
                self.data["residents"].remove(pet)
                self.save_database()
                print(f"\n🎊 HOORAY! {name} found a forever home! 🎊")
                print("🥳 💕 🏠 💕 🥳")
                return
        print(f"\n🧐 Error: Pet '{name}' not found.")

    def show_dashboard(self):
        """ UI: Displays the shelter dashboard in the console. """
        print("\n" + "⭐ " * 15)
        print("   🐾  ANIMAL & HUG SYSTEM  🐾   ")
        print("⭐ " * 15)
        
        print(f"\n🏠 RESIDENTS IN SHELTER ({len(self.data['residents'])}):")
        if not self.data["residents"]:
            print("   (The shelter is empty...)")
        for p in self.data["residents"]:
            sos = f"🚨 [SOS: {p['status']['reason']}]" if p["status"]["is_urgent"] else "💎 [OK]"
            print(f"   • {sos} {p['technical_info']['icon']} {p['name']} (ID: {p['technical_info']['id']})")

        print(f"\n💖 HAPPY HEARTS: {len(self.data['happy_tails'])} pets adopted!")
        print(f"💰 FUND: ${self.data['donations']}")
        print("-" * 30)

# --- PROGRAM ENTRY POINT ---
if __name__ == "__main__":
    # ASCII Header: Visual intro for the jury
    print(r"""
       __🐱__            __🐶__
      (  o o )          (  u u )
    ==(  =^= )==      ==(  -v- )==
       '---'             '---'
    A N I M A L   &   H U G
    """)
    
    app = AnimalAndHug()
    while True:
        app.show_dashboard()
        print("\n[1] Add Pet | [2] Adopt | [3] Donate | [4] Exit")
        choice = input("Select action >>> ")
        
        if choice == "1":
            n = input("Pet Name: "); s = input("Species: ")
            u = input("Is it urgent? (y/n): ").lower() == 'y'
            app.add_pet(n, s, u)
        elif choice == "2":
            app.give_a_hug(input("Who is being adopted?: "))
        elif choice == "3":
            try:
                amt = int(input("Donation amount ($): "))
                app.data["donations"] += amt
                app.save_database()
                print("🙏 Thank you for the hug!")
            except:
                print("❌ Please enter a number!")
        elif choice == "4":
            print("Saving data... See you! 🐾💕")
            break
            