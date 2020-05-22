from flask_restplus import Api, Resource, fields # Necessary imports
from flask import Flask, request
from emailer import emailSender
from smser import smsSender
###############################
#DEV: Carlos Ornelas
#Description:
#API Server constructor 
###############################
 # Special Flask Constructor. __name__ is a special case variable which receieves __main__ 
 # once the script is executed
app = Flask(__name__)
#API info
api = Api(app, version='0.1.0', description='SmartPharm Notification API Platform')
# "Name" of API
name_space = api.namespace('api')

#Create a Json model of the emailer class
emailModel = api.model('Email',  {'emailAddress': fields.String(readonly = True),
                                  'dispensee': fields.String(readonly=True), 
                                  'receiveName': fields.String(readonly = True)    }  )

smsModel = api.model('SMS',{'to': fields.String(readonly = True),
                            'body': fields.String(readonly = True)})

dispenseModel = api.model('Dispense', {'inputFromDevice': fields.String(readonly = True)})

          
@name_space.route("/getinfo")
class GetInfo(Resource):

    def get(self):
        try:
            return {"Status": "Connection Successful"}
            
        except KeyError as e:
            name_space.abort(500, e.__doc__, status="Could Not Save Information", statusCode="500")
        except Exception as e:
            name_space.abort(400, e.__doc__, status="Could Not Save Information", statusCode="400")

# This is the notification center of the API
# The Flask API is expecting the JSON model 
# Individually check for each JSON variable
# Return email sent for debugging purpose
@name_space.route('/notification')
class sendEmail(Resource):

    @api.expect(emailModel, validate = True )
    def post(self):
        emailAddress = request.json['emailAddress']
        dispensee    = request.json['dispensee']
        receiveName  = request.json['receiveName']
        sender = emailSender().sendEmail(emailAddress, dispensee, receiveName)
        return {'Status':'Email Sent'}


@name_space.route('/sms')

class sendSMS(Resource):
    @api.expect(smsModel, validate = True)
    def post(self):
        to      = request.json['to']
        body    = request.json['body']
        sendSMS = smsSender().sendSMS(to, body)
        return{'Status': "SMS SENT"}

# tie it all up
if __name__ == '__main__':
    app.run()