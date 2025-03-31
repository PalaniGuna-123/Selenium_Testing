import pywhatkit
group_id = "GiLIGO5AMCP8RJEwNotimo"
message = "Hello squad, have you all filled out the company selection form?"

pywhatkit.sendwhatmsg_to_group_instantly(group_id, message, 15, True, 5)

print("Message sent successfully!")

# Python Code to Schedule a WhatsApp Group Message
# import pywhatkit

# group_id = "GiLIGO5AMCP8RJEwNotimo"
# message = "Hello squad, have you all filled out the company selection form?"

# pywhatkit.sendwhatmsg_to_group(group_id, message, 22, 30)

# print("Message scheduled successfully!")
# explanation
# pywhatkit.sendwhatmsg_to_group(group_id, message, hours, minutes, wait_time=15, tab_close=True, close_time=10)


