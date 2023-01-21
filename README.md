<!-- Logos -->
![Emails are raining](/.attachments/emails.gif)

# Lambda alarm Introduction
AWS Lambda alarm that sends SNS custom email notifications every monday to alert IT users oncall shift change. The lambda is triggered by a cron job using aws eventbridge. Lambda executes custom python code that interacts with aws dynamodb to retrieve state and user data. Python code is executed and to interact with aws resources by using the aws sdk for python.

# DynamoDB Schema:
![DynamoDB Schema](/.attachments/Dynamo-schema.png)

# NOTE: THIS Project takes advantage of a pre-created sandbox vpc and will use data resources to pull necessary data.

# Directory Tree Structure:
```
│   .gitignore
│   LICENSE
│   README.md
│
├───.attachments
│       Dynamo-schema.png
│       emails.gif
│
├───code
│       alarm.py
│
├───infrastructure
│       backend.tf
│       data.tf
│       dynamodb.tf
│       eventbridge.tf
│       iam.tf
│       lambda.tf
│       locals.tf
│       outputs.tf
│       provider.tf
│       sg.tf
│       sns.tf
│       variables.tf
│
└───yaml
    │   code-ci.yaml
    │   infrastructure-ci.yaml
    │
    └───templates
            code-cd.yaml
            destroy-infrastructure.yaml
            infrastructure-cd.yaml
```
