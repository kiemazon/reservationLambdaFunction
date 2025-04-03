import boto3
import os
import json
ce_client = boto3.client('ce')
sns_client = boto3.client('sns')
class mainClass:
    def __init__(self, i):
        self.i = i
    def apiCall(self):
        return ce_client.get_reservation_purchase_recommendation(Service=self.i)
    def snsPublish(self):
        try:
            response = self.apiCall()
            accountID = boto3.client('sts').get_caller_identity().get('Account')
            sns_client.publish(TopicArn=os.environ.get('topic_arn'),Message=f'AWS Service: {self.i},\nRecommendations:{str(response.get("Recommendations"))}',Subject='[{str(accountID)}]Savings for {self.i}')
        except Exception as e:
            print(e.response['Error']['Message'])

def lambda_handler(event, context):
    y = ['Amazon Elastic Compute Cloud - Compute','Amazon Relational Database Service','Amazon Redshift','Amazon ElastiCache','Amazon Elasticsearch Service','Amazon OpenSearch Service','Amazon MemoryDB Service','Amazon DynamoDB Service']
    for i in y:
        mc = mainClass(i)
        mc.apiCall()
        mc.snsPublish()
    return {"StatusCode": 200}
