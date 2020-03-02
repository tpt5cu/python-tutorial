- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration - configuration options
- https://calculator.s3.amazonaws.com/index.html - cost calculator
- https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session - client vs resource vs session
- https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html - send emails to non-verified addresses
# These notes should probably go in their own .odt
# Introduciton
- The service being used in Amazon Simple Email Service (SES)
# Costs
- According to the online calculator, sending [1, 100] emails per month from boto3 will cost me $0.01
# Configuration
- In order to do anything with boto3, I need AWS credentials and a region
## Sources
- There are several options for configuration:
- Though not shown in the boto3.client() API, credentials CAN be passed directly into the initializer
- Particular environment variables can also be used to directly specify credentials
- Credentials can be stored in files and loaded by boto3
### Shared credentials file
- A "shared credentials file" is one configurtion option
- $ export AWS_SHARED_CREDENTIALS_FILE=\<file>
    - Set the location of the ini file using this command so boto3 can find and use it
# Client, resource, session
- Resource is high-level API and conveneient
- Client is low-level API 
- boto3 creates a default session for me, but I can specify a session (e.g. in order to connect to a different region)
    - A session object can create client and/or resource objects
# Sending emails
## Send email to non-verified email
- I have to literally fill out a report and submit it on Amazon to have them remove my account from the SES sandbox 
    - Use the mailbox simulator instead