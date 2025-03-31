import pywhatkit

phone = input('Enter the phone number: ')
message = input('Enter your message: ')

pywhatkit.sendwhatmsg_instantly(phone, message, 20, True, 20)

print("Message sent successfully!")
