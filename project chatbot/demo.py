import pyautogui
import time
import pyperclip

# Small delay to give user time to switch windows
time.sleep(2)

# Step 1: Click the icon
pyautogui.click(x=1402, y=1042)
time.sleep(1)

# Step 2: Select area by dragging from (696, 217) to (1879, 937)
pyautogui.moveTo(696, 217)
pyautogui.dragTo(1879, 937, duration=0.5, button='left')
time.sleep(0.5)

# Step 3: Press Ctrl+C to copy
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get content from clipboard
copied_text = pyperclip.paste()
print("Copied Text:")
print(copied_text)
