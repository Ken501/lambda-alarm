# lambda-alarm
AWS Lambda alarm that sends SNS custom email notifications every monday to alert users shift change. The lambda is triggered by a cron job using aws alarms. Lambda executes custom python code that interacts with aws dynamodb to retrieve state and user data.
