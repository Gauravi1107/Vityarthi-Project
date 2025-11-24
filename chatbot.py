import random
def history():
    try:
        file=open("companion.txt","r")
        data=file.read().strip().split()
        return data[-5:]
    except:
        return[]
    
def save_mood(mood):
    file=open("companion.txt","a")
    file.write(mood+",")

def response(message):
    import random
    msg = message.lower()
    if any(word in msg for word in ["hello", "hi", "hey", "heyy", "heyyy"]):
        return random.choice(["Heyy! How are you feeling today? 😊","Hi! What's going on?","Hey! Tell me what's on your mind!"])
    if "your name" in msg:
        return "i'm your social companion ! Your supportive buddy.😊"
    if "who are you" in msg:
        return "I'm your companion bot, here to talk and support you"
    if 'how are you' in msg:
        return random.choice(["I'm doing great. How about you?", "I' good! What about you"])
    if any(word in msg for word in ['food', 'eat','hungry']):
        return random.choice(["Ooh! food!!, What are you going to eat", "Food mood!! What's your favourite dish?"]
                             )
    if any(word in msg for word in ['Thank you',"thanks","thank" ]):
        return random.choice([  "Anything for you! 💖",  "You're welcome!","Always here to help 😊"])

    if any(word in msg for word in ["stress", "stressed", "pressure", "anxiety", "overthinking", "panic"]):
        return random.choice([
            "Relax… breathe… I’m right here. What’s causing the stress?",
            "It must be tough. Want to tell me what’s worrying you?",
            "You're under pressure, I get it. Let’s figure it out together."
        ])
    if any(word in msg for word in ["sad", "down", "hurt", "crying", "depressed", "upset", "lonely"]):
        return random.choice([
            "I’m really sorry you’re feeling like this. Want to talk about what happened?",
            "You’re not alone… I’m here for you 🫂",
            "That sounds painful… but I’m right here with you."
        ])

    if any(word in msg for word in ["tired", "exhausted", "drained", "sleepy", "no energy"]):
        return random.choice([
            "You sound really tired… Maybe take a small break?",
            "Your body needs rest. You should slow down a bit ❤️",
            "You’ve done enough for today. Rest if you can."
        ])
    if any(word in msg for word in ["weather", "hot", "cold", "rain"]):
        return random.choice([
            "Weather affects mood so much! How is it there?",
            "Is it raining? That sounds cozy ☔",
            "Hot or cold—what do you prefer?"])

    if any(word in msg for word in ["happy", "excited", "great", "amazing", "awesome", "good day"]):
        return random.choice([
            "YAYY! I love this energy 🥳 What made you so happy?",
            "That’s amazing! Tell me everything!",
            "I’m so glad you're feeling great! Keep shining 🌟"
        ])
    if msg in ["no", "nope", "nothing", "leave me", "stop"]:
        return random.choice([
            "Okay… I understand. But I’m here whenever you want to talk.",
            "Alright… I’ll be here for you.",
            "Take your time. I won’t push you."
        ])
    if msg in ["yes", "yeah", "yep", "sure"]:
        return random.choice([
            "Okay! Tell me more 😊",
            "Alright! What’s on your mind?",
            "Great! I'm listening."
        ])
    if any(word in msg for word in ["completed work", "task done", "finished my work","finished my task", "completed my work" ]):
        return random.choice([
            "Great! Congratulations on achieving your goal", 
            'YAYY!! great work', 
            "You worked hard🙌", 
            "I'm Proud of you"])
    
    if any(word in msg for word in ["fine", "okay", "ok", "alright", "normal"]):
        return random.choice([
            "That's good to hear! What made your day better?",
            "Nice! Anything interesting happening?",
            "Great! Want to chat about something?"
        ])

    if msg.endswith("?"):
        return random.choice([
            "Hmm… interesting question. What do YOU think?",
            "Let me think about that… tell me more.",
            "Why do you ask that?"
        ])
    fallback = [
        "Hmm… I get you. Tell me more.",
        "I’m listening… go on.",
        "That sounds important. Explain more!",
        "Okay… how does that make you feel?",
        "I understand. Want to talk deeper about it?"
    ]
    return random.choice(fallback)

def music(mood):
    if mood=="sad":
        return ["Upbeat Pop Mix", "Feel- Good Dance Playlist","Soft Pian comfort"]
    elif mood=="happy":
        return ["Upbeat Pop Mix","Feel-Good Dance Playlist","Morning Motivation Songs"]
    elif mood=="stress":
        return ["Deep Focus Playlist","Rain Sounds + Piano","Relaxing Ambient Study Mix"]
    else:
        return ["Chill Vibes Playlist","Evening Relax Mix","Smooth Beats for Daily Mood"]

def affirmation(mood):
    if mood=="stress" or mood=="sad":
        return "You are stronger than you think. Keep going!!"  
    if mood=="happy":
        return "GREAT!!, I'm Pround of you"
    
def behaviour(history):
    if not history:
        return "No Data yet"
    sad_count=history.count("sad")
    stress_count=history.count("stress")
    happy_count=history.count("happy")

    if sad_count>=3:
        return "You have been feeling low lately. Maybe take some time for yourself today."
    elif stress_count>=3:
        return "You have been stressed lately. Do you want to share with me?"
    elif happy_count>=3:
        return "You are in great mood recently.Keep up the good work. I'm Proud of you😊"
    else:
        return "Your mood have been stable mostly. Keep taking care of yourself🙌."

def main_menu():
    print("💖Welcome to your SOCIAL COMPANION")
    
    print("What would you like me to do?")
    print("\n1. Chat with me.")
    print("2. Log your mood + stress.")
    print("3. Give suggestions(music,breaks, affirmations).")
    print("4. View behaviour summary")
    print("5. Exit.\n")
history=history()
while True:
    main_menu()
    choice= input("Enter your choice: ")
    if choice=="1":
        print("\nCHat mode started! Type 'bye' to exit")
        while True:
             msg=input("You: ").lower()
             if msg in ['bye', 'exit', 'quit']:
                 print("Companion: Bye! Take Care💖")
                 print("\n Returning to main menu")
                 break
             reply=response(msg)
             print("Companion: ",reply)
    elif choice=="2":
        while True:
            log=input("\n Enter your log: ")
            history.append(log)
            save_mood(log)
            more=input("Do you want to add more logs? (YES/NO): ").strip().lower()
            if more!="yes":
                print("Returning to main menu \n")
                break
    elif choice=="3":
        mood = input("How is your mood right now? (happy/sad/stressed/normal): ").lower()
        print("\nMusic Recommendation:", music(mood))
        print("Affirmation:", affirmation(mood))
        playlists = music(mood) 
        print("\n🎵 Recommended Playlists:")
        for p in playlists:
            print("•", p)
            print("\nBreak Suggestion: Take a 5-minute walk or drink water.")
    elif choice=="4":
        print("\n Yourbehaviour pattern: ")
        print(behaviour(history))
    elif choice=="5":
        print("\n BYEE!! Take care. I am always here if you need me😊")
        break
    else:
        print("INCORRECT OPTION")
