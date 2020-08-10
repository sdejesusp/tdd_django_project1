from selenium import webdriver

# browser = webdriver.Firefox()
browser = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr")
browser.get('http://localhost:8000')

assert 'Django' in browser.title

