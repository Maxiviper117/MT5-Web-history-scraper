import requests

login = 88394128
password = "wRQpXRG!Y583fz$"
server = "Ava-Real 1-MT5"

# Set the URL of the login page and the form data (e.g., username and password)
url = "https://trade.mql5.com/trade"
form_data = {"LOGIN": "myusername", "PASSWORD": "mypassword", "SERVER": "server_name"}

# Send a POST request to the login page with the form data
response = requests.post(url, data=form_data)

# If the login is successful, the server will send back a cookie that you can use to authenticate subsequent requests
if response.status_code == 200:
    print("Login successful")
    # Extract the cookie from the response and store it for future requests
    cookie = response.cookies
else:
    print("Login failed")