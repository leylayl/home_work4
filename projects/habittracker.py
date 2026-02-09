import json
import os
from datetime import datetime

class LeylaUltimateTracker:
    def __init__(self, user_name, age):
        self.user_name = user_name
        self.age = age
        self.file_name = "leyla_habits_data.json"
        
        self.habits = {
            "Morning Hydration": "💧",        
            "Post-School Recovery": "🛌",     
            "Night Owl Study": "🦉",          
            "Volunteer Service": "🤝",        
            "Creative Procrastination": "⏳", 
            "Journaling Thoughts": "📔",      
            "Capturing Memories": "📸",       
            "Making Handmade Gifts": "🎨",    
            "Humor as Stress Relief": "🤡",    
            "Name Mixing Paradox": "🔄",      
            "Frequent Name Usage": "🗣️",       
            "Sending Emojis During Chatting": "💖" 
        }
        self.progress = self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except:
                return {}
        return {}

    def save_data(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.progress, file, indent=4, ensure_ascii=False)
        print(f"\n[SYSTEM] Data synced to {self.file_name} ✨")

    def get_status(self, percentage):
        if percentage < 30: return "Rest & Recharge 🧊"
        if percentage < 70: return "Active Flow ⚡"
        return "Leyla Level: Unstoppable 👑"

    def show_interface(self):
        date_today = datetime.now().strftime("%A, %d %B %Y")
        
        print("\n" + "🌸 " * 15)
        print(f" PROJECT: THE REAL LEYLA TRACKER")
        print(f" DEVELOPER: {self.user_name} | AGE: {self.age}")
        print(f" DATE: {date_today}")
        print("🌸 " * 15)

        if date_today not in self.progress:
            self.progress[date_today] = {habit: False for habit in self.habits}

        done_count = 0
        for habit, sticker in self.habits.items():
            is_done = self.progress[date_today][habit]
            status_symbol = "❤️" if is_done else "🤍"
            if is_done: done_count += 1
            print(f" {status_symbol} {sticker} {habit.ljust(30)}")

        total = len(self.habits)
        percent = int((done_count / total) * 100)
        
        print("-" * 50)
        print(f" DAILY PROGRESS: {percent}%")
        print(f" CURRENT VIBE: {self.get_status(percent)}")
        print("-" * 50)

    def mark_habit(self):
       
        print("\nWhich habit did you complete? (Enter name or 'save'):")
        action = input(">>> ")

        if action in self.habits:
            today = datetime.now().strftime("%A, %d %B %Y")
            self.progress[today][action] = True
            
            if action == "Sending Emojis During Chatting":
                print("✨ ✨ ✨ Love and Emojis everywhere! ✨ ✨ ✨")
                
            print(f"Done! {action} recorded.") 
            return True
        elif action.lower() == 'save':
            self.save_data()
            return False
        else:
            print("Error: Habit not found. Check the text above!")
            return True

if __name__ == "__main__":
    app = LeylaUltimateTracker(user_name="Leyla", age=16)
    
    active = True
    while active:
        app.show_interface()
        active = app.mark_habit()
        
