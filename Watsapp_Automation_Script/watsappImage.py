# import pywhatkit

# phone = input('Enter the phone number (with country code): ')
# image_path = r"C:\Selenium_Testing\screenshot.png"
# caption = input("Enter the caption for the image: ")

# pywhatkit.sendwhats_image(phone, image_path, caption, 20, True, 10)

# print("Image sent successfully!")

import pywhatkit

phone = input('Enter the phone number with countrycode ')
image_path = r"C:\Selenium_Testing\screenshot.png"

# No caption, using empty string
pywhatkit.sendwhats_image(phone, image_path, "This is pranesh comics tv", 20, True, 20)

print("Image sent successfully!")
