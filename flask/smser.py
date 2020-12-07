from twilio.rest import Client
import os
###############################
#DEV: Carlos Ornelas
#Description:
#SMS class based around the Twilio Library
#Used Twilio Cookbook to build this file
#Tester file @ bottom for debugging purposes
#Can be removed if needed
###############################
class smsSender:
    def sendSMS(self, to, body ):

        # Your Account Sid and Auth Token from twilio.com/console
        # CAUTION: Create ENVIROMENT VARIABLES for account SID and AuthToken
        account_sid = os.environ['SID_TWILIO']
        auth_token =  os.environ['AUTH_TWILIO']
        client = Client(account_sid, auth_token)

        client.messages \
                .create(
                    body=body,
                    from_='Twilio Number here',
                    to=to
                )
        return "SMS SENT"
        


tester = smsSender().sendSMS('number here', "Pills have been dispensed for Carlos")
print(tester)
