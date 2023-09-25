#!/usr/bin/env python
# coding: utf-8

# In[11]:


import twilio


# In[14]:


from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'ACef481fdf7a22a710747d0422f073fc01'
auth_token = '5b72992f3f215f2965a3cb8666ea331d'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define the recipient's phone number and the message you want to send
to_phone_number = '+916390438993'  # Replace with the recipient's actual phone number
message = 'Hello, this is a test SMS sent from Python!'

# Send the SMS
message = client.messages.create(
    to=to_phone_number,
    from_='+12564459747',  # Use your Twilio phone number here
    body=message)

# Print the SID (a unique identifier) of the sent message
print(f'SMS sent with SID: {message.sid}')


# In[ ]:




