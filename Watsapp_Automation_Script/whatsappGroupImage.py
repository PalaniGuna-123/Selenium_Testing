import pywhatkit
group_id = "GiLIGO5AMCP8RJEwNotimo"
image_path = r"C:\Selenium_Testing\screenshot.png"
pywhatkit.sendwhats_image(group_id, image_path, "", 15, True, 10)

print("Image sent successfully!")
