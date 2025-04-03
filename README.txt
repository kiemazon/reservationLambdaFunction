# example config/used for testing
# prerequisites:
#  - sns topic for publishing output/content from code
#  - iam role with permission to make api calls to get data & publish to sns topic

Lambda config = {
  General configuration:{
    Description: -
    Memory: 128MB
    Ephemeral storage: 512MB
    Timeout: 0min3sec
    SnapStart: None
  },
  Environment variables:{
    'topic_arn:arn': 'aws:sns:eu-west-1:012345678910:example-sns-topic-arn'
  },
  Triggers: 'EventBridge (CloudWatch Events): example-eventsbridge-rule-name'
  Permissions: '*'
}
