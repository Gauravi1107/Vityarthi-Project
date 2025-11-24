Social Companion – A Python-Based Emotional Support Chatbot
Project Overview

SOCIAL COMPANION is a simple and interactive chatbot designed to support users emotionally by chatting with them, tracking moods , giving music and affirmations suggestions based on the mood, and analysing behaviour patterns.
This project has made use of basic python functions and file handling to store user logs, generate responses and provide basic personal suggestions based on the user mood.

It is a beginner friendly chatbot and can be easily extended into an advanced AI companion app.
Features
1. Chat Mode:
   
In this mode the user is able to chat with the bot.

The bot will respond based on the keywords in the messages sent by the user(like happy, greetings, sadness etc.)

A friendly fallback message will be  given if the bot doesn’t understand.

2. Mood & Stress Logging:
   
Users can enter their mood in the log which will be saved in the text file automatically.

The user can enter multiple log entires at once

3. Smart Suggestions
   
Based on the users current mood the bot will suggest:

🎵 Music playlists

🌼 Positive affirmations

☕ Small break suggestions

4. Behaviour Summary:
   
Analyses recent mood logs.

Detects user's mood patterns(e.g., frequent sadness, stress, hapiness, stable mood etc.)

Gives supportive feedback.

5. User-friendly Menu Navigation:
   
After completing every task the user is directed back to the main menu.

Contains simple input -based controls.

Technologies / Tools Used:

.Python 3.13

.File Handling

.Random Module 

.Conditional Logic & Loops


 Steps to Install & Run the Project:
 
1. Install Python

2. Download/Copy the Project Files

Save the full code as: companion.py

Make sure there is an empty file named:

companion.txt
(This will store your mood logs.)

3. Run the Program

4. Follow On-Screen Menu

You’ll see:

1. Chat with me
2. Log your mood
3. Get suggestions
4. View behaviour summary
5. Exit

Choose any number to begin.

Instructions for Testing

Here’s how you can properly test each feature:

✔ Chat Mode

Choose option 1.
Try typing:

"hello"

"I feel sad"

"I am stressed"

"how are you?"

"Tell me something"

Bot should reply appropriately.

Type bye to exit.

✔ Logging Mood

Choose option 2.

Type mood logs like:

"sad"

"happy"

"stress"

Enter yes to add more logs.

Enter no to return to menu.

The logs will automatically be saved in the companion.txt

✔ Suggestions

Choose 3.

Type any mood:

happy

sad

stressed

normal

Bot should display:

music recommendations

affirmations

break suggestions

✔ Behaviour Summary

Choose 4.

Based on mood history, the bot will show:

"You have been feeling low..."

"You have been stressed..."

or "Your mood has been stable…"


