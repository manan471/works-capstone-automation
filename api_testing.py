import requests

# Define the API endpoint
for i in range(1000):
    url = "http://worksapp.propsure.rocks/leads"
    response = requests.get(url)
    print(response)

    print("API request successful")
else:
    print("API request Not successful")


# Check the response status code
# if response.status_code == 200:
#     print("API request successful")
#     data = response.json()  # Parse response JSON data
#     # Perform assertions or verifications on the API response data
# else:
#     print(f"API request fa   iled with status code: {response.status_code}")
# import time
#
# import requests
#
# # API endpoint URL
# url = "http://worksapp.propsure.rocks/customers/store"
#
#
# # JSON data to send in the POST request
# data = {
#     "first_name": "test",
#     "last_name": "test",
#     "phone": "+92 342-3242342"
# }
#
#
# try:
#     response = requests.post(url, json=data)
#     print("POST request successful")
# except:
#     time.sleep(2)

