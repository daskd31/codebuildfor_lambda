import json
import os

def lambda_handler(event, context):
    
    if event.get('detail',None) != None:
        stateMachineArn = event.get('detail',{}).get('stateMachineArn',{})
        stateMachineArn = stateMachineArn.rsplit(':')[-1]
    else:
        stateMachineArn = "No ARN provided"
        
    if event.get('detail',None) != None:
        statusDetails = event.get('detail',{}).get('status',{})
    else:
        statusDetails = "No status provided "
        
    msgSubject = stateMachineArn + " - status " + statusDetails
    
    jsonFormat = json.dumps(event,indent = 6)
    
   
    return {
        'statusCode': 200,
        'body': jsonFormat,
         'headers': {
            'Content-Type': 'text/json',
        }
    }
