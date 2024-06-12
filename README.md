[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hidden_coding)

![image](https://github.com/flaming-chameleon/telegram-profile-images-with-name/assets/73156836/480d510b-a0e6-4b98-8d30-c540c7b09581)

# Telegram Image Scaraper from Twitter

This script scrapes follower information from specified Twitter profiles using Selenium and saves their profile images and usernames. 

## Requirements

- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver
- Requests

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install selenium requests
   ```

2. **Download ChromeDriver:**
   Ensure you have the ChromeDriver installed and its path is set correctly in the script (`CHROME_DRIVER_PATH`).
   [List of drivers here](https://googlechromelabs.github.io/chrome-for-testing/#stable)

4. **Configure Chrome for remote debugging:**
   Start Chrome with the remote debugging port:
   ```bash
   google-chrome --remote-debugging-port=9222
   ```

5. **Run the script:**
   ```bash
   python script.py
   ```

## Script Details

- The script navigates to the follower pages of specified Twitter profiles.
- It scrolls through the follower list and captures the username and profile image of each follower.
- The images are saved locally in the `images` directory.
- The collected data (username and image filename) is saved in `data.json`.

  
[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hidden_coding)
