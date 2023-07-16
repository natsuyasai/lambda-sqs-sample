import boto3


def lambda_handler(event, context):
    client = boto3.client('sqs')
    client.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/705356739051/lambda-trigger-sample.fifo',
        MessageBody='TestMessage',
        MessageAttributes={
            'TestData': {
                'StringValue': 'TestStringData',
                'DataType': 'String'
            }
        },
        MessageDeduplicationId='Group1-Id1',
        MessageGroupId='Group1'
    )


if __name__ == '__main__':
    lambda_handler(None, None)
