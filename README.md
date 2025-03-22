# 🧠 Typing Speed Bot

A blazing-fast Python bot that types automatically on [10FastFingers](https://10fastfingers.com/typing-test/english) using Selenium.  
Give it a target WPM (Words Per Minute), and it’ll type for you as fast as possible — no human delay added!

---

## 🚀 Features

- ✅ Automates the typing test at 10FastFingers
- ✅ Accepts custom WPM input via command line
- ✅ Uses Selenium + BeautifulSoup for automation and scraping
- ✅ Requires **no manual ChromeDriver installation** (thanks to `webdriver-manager`)
- ✅ Clean and modular code structure

---

## 📸 Demo

<img src="https://user-images.githubusercontent.com/your-gif-or-screenshot-url" width="600" alt="demo of bot typing on 10fastfingers" />

---

## ⚙️ Requirements

- Python 3.7+
- Google Chrome (installed)
- Required packages (see below)

---

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/typing-speed-bot.git
cd typing-speed-bot
```
2. **Install the dependencies**:
```
pip install -r requirements.txt
```

3. **Usage**:
Run the bot with your desired speed:
```
python typing_bot.py --wpm 60
```
➡️ The bot will open Chrome, wait for the test to load, then type words as fast as possible until it reaches the target character count (based on WPM × 5).

4. **📁 Project Structure**:
```
typing-speed-bot/
├── typing_bot.py         # Main script
├── requirements.txt      # Required dependencies
├── README.md             # This file
```
5. **Requirements.txt Contents**:
```
selenium>=4.0.0
webdriver-manager>=3.0.0
beautifulsoup4>=4.9.0
```
6. **Contributing**:   


Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.


