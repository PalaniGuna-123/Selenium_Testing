with open("C:/Selenium_Testing/Python_OOPS/requirements.txt", "r") as file:
    content=file.read()
    print(content)
with open("C:/Selenium_Testing/Python_OOPS/requirements.txt", "w") as file:
    content=file.write("Hello Python , I love Python")

with open("C:/Selenium_Testing/Python_OOPS/requirements.txt", "a") as file:
    content=file.write("/n hello world")