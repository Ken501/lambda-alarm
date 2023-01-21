<!-- Logos -->
![Emails are raining](/.attachments/emails.gif)

# Lambda alarm Introduction
AWS Lambda alarm that sends SNS custom email notifications every monday to alert IT users oncall shift change. The lambda is triggered by a cron job using aws eventbridge. Lambda executes custom python code that interacts with aws dynamodb to retrieve state and user data. Python code is executed to interact with aws resources by using the aws sdk for python.

# CI/CD
Yaml manifest configuration files are included which are compatible with the Microsoft Azure DevOps platform. The pipeline configuration runs a development pipeline that only triggers with branches that are not equal to main and a production branch that triggers when a merge occurs for terraform infrastructure release and a separate pipeline for code ci/cd.

<!-- Dir Summary -->
# Directory Guide
* .attachments
  * Contains images and other miscellaneous items for project
* code
    * python code
* Infrastructure
    * Stores Terraform configuration files
* yaml
    * Stores Microsoft Azure Devops Services CI/CD pipeline configuration files in yaml format

# DynamoDB Schema:
![DynamoDB Schema](/.attachments/Dynamo-schema.png)

# NOTE: This project takes advantage of a pre-created sandbox vpc and will use data resources to pull necessary data.

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
# Terraform Resources
* EventBridge
* Lambda
* SNS
* DynamoDB

# For more information on main components
* DynamoDB core components documentation: 
   *  https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html
* Python sdk: 
   *  https://boto3.amazonaws.com/v1/documentation/api/latest/index.html