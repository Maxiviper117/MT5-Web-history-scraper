
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")


# Set the URL of the login page
# url = "https://trade.mql5.com/trade?version=5"
url = "https://www.facebook.com"
#
# Create a webdriver for Chrome and open the URL
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://trade.mql5.com/trade?version=5")
def connect():
	driver.implicitly_wait(time_to_wait=20)

	while True:
		pass

connect()


# # Wait for the page to finish loading
# driver.implicitly_wait(20)  # Wait for up to 10 seconds

# # Parse the HTML code of the page
# soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup)

# # Find the list of available servers
# server_list = soup.find("select", {"id": "SERVER"})
# print(server_list)

# # Extract the server names from the list
# # servers = [option.get("value") for option in server_list.find_all("option")]

# # Select the desired server
# server = "server_name"
# # if server in servers:
# #     form_data = {"LOGIN": "myusername", "PASSWORD": "mypassword", "SERVER": server}

# # Close the webdriver
# driver.quit()
