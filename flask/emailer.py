import smtplib, ssl
import os
###############################
#DEV: Carlos Ornelas
#Description:
# Email class based around SMTP 
# Tester file can be removed
# Used for debugging purposes 
###############################
class emailSender:

    def sendEmail(self,emailAddress,dispensee,recieveName):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com" 
        sender_email = "smartpharmtech@gmail.com"  # Enter your address
        password = os.environ['SMTP_PW']       
        subject = "Hi there, {}".format(recieveName)
        body = "Pills have been dispensed for user {}".format(dispensee)
        message = "Subject:{}\n\n{}".format(subject,body)
 
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server: # Default constructor
            server.login(sender_email, password) # login to email
            server.sendmail(sender_email, emailAddress, message) # Send Message

        return 'email sent'
tester = emailSender().sendEmail('testEmail@gmail.com','Mike', "Carlos")
print(tester)
