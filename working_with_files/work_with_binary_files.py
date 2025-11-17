import requests

url = 'https://landlord.ua/wp-content/uploads/2025/01/fe2a5835d6d62a84d64cc357061c8186a244a1a8-734x483.jpeg'

response = requests.get(url=url)
# print(response.content)

with open('spring.jpeg', mode="wb") as file:
    content = response.content
    file.write(content)
    file.write(content)
    file.write(b' hello from Vasyl')



with open('spring.jpeg', mode="rb") as file:
    file_content = file.read()
    print(file_content)
