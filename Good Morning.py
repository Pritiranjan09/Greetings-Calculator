from datetime import datetime
import pytz

# Select time zone (India)
timezone = pytz.timezone("Asia/Kolkata")

# Get current time in that time zone
current_time = datetime.now(timezone)

# Extract hour (0–23)
hour = current_time.hour

# Decide greeting
if hour >= 5 and hour < 12:
    print("Good Morning 🌅")
elif hour >= 12 and hour < 17:
    print("Good Afternoon ☀️")
else:
    print("Good Night 🌙")
