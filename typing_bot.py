import sys
import argparse
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



TEN_FAST_FINGERS_URL = "https://10fastfingers.com/typing-test/english"
CHARACTERS_PER_WORD = 5

def get_desired_character_count() -> int:
    """Parse command-line arguments and return the total character count."""
    parser = argparse.ArgumentParser(description="10FastFingers typing bot.")
    parser.add_argument("--wpm", type=int, help="Desired words per minute", required=True)
    args = parser.parse_args()
    return args.wpm * CHARACTERS_PER_WORD


def setup_browser() -> webdriver.Chrome:
    """Initialize and return the Chrome browser instance."""
    print("Launching browser...")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(TEN_FAST_FINGERS_URL)
    print("Waiting for page to load (Cloudflare)...")
    sleep(10)
    return browser

def get_word_list(browser) -> list:
    """Scrape the word list from the 10FastFingers page."""
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    try:
        words = soup.find('div', {'id': 'wordlist'}).text.split('|')
        print(f"[INFO] Retrieved {len(words)} words.")
        return words
    except AttributeError:
        print("[ERROR] Could not retrieve word list. Exiting.")
        browser.quit()
        sys.exit(1)


def type_words(browser, words, charactercount) -> None:
    input_field = browser.find_element(By.ID, "inputfield")
    print("Starting to type...")
    for word in words:
        if charactercount <= 0:
            break
        for char in word:
            input_field.send_keys(char)
        input_field.send_keys(Keys.SPACE)
        charactercount -= len(word) + 1
    print("Typing complete.")


def main():
    charactercount = get_desired_character_count()
    browser = setup_browser()
    words = get_word_list(browser)
    type_words(browser, words, charactercount)

if __name__ == "__main__":
    main()