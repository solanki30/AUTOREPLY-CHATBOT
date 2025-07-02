import pyautogui
import pyperclip
import time
import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="APIKEY")

# Choose Gemini model
model = genai.GenerativeModel("gemini-2.5-flash") 

# STEP 1: Click on WhatsApp icon to activate window
pyautogui.click(1346,1053)  # Change coordinates as per your screen
time.sleep(1)

# STEP 2: Select the message to reply (drag from one point to another)
pyautogui.moveTo(693,198)
pyautogui.dragTo(1863,926, duration=1.0,button = "left")  # Smooth dra

# STEP 3: Copy selected message
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# STEP 4: (Optional) Click elsewhere to remove selection highlight
pyautogui.click(1828,908)

# STEP 5: Get copied message from clipboard
chat_history = pyperclip.paste()
print(chat_history)

prompt = f"""The following is a message from a WhatsApp chat. 
Respond like Solanki, who is a bit frustrated but always technical, logical, and reacts smartly.
The reply should sound human and casual.
Message: "{chat_history}"

Solanki's Reply:"""

# STEP 6: Generate reply using Gemini
response = model.generate_content(prompt)
reply = response.text.strip()
print("Reply from Gemini:\n", reply)
# STEP 7: Copy the bot reply to clipboard
pyperclip.copy(reply)

# STEP 8: Paste the reply in message box & send
pyautogui.click(796,976)  # Click on message box
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.3)
pyautogui.press('enter')  # Send the message