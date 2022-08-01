
# Cloudformation Template for Lambda, SQS, RDS.  

### Deploy a static website along with domain accessible from internet.
- Create an SQS queue with appropriate policy and a dead letter queue for it.
- Create a lambda function with runtime of your choice. If possible, try to containerize this application for lambda.
- Read JSON from SQS and push any contents of object &quot;data&quot; in the message in RDS
- If a sample JSON is published to SQS, it should have x number of objects and one object as “data”. Just store the contents of data in RDS.

#### Commands 
```bash
aws cloudformation deploy --template-file ./lambda.yml --stack-name <stack_name> --profile <profile>
aws cloudformation deploy --template-file ./rds.yml --stack-name <stack_name> --profile <profile>

aws lambda update-function-code --function-name <function_name> --zip-file fileb://lambda_function.zip
```
Note: 
- Update the RDS endpoint url in lambda function once it deployed. 
- Below is test SQS message. 
- Whitelist ingress tcp port 3306 in defult VPC.   
``` bash
{"id": 1, "data": {"one": "red", "two": "yellow"}}
```





