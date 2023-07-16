
def lambda_handler(event, context):
    print(event['Records'])
    batch_item_failures = []
    sqs_batch_response = {}
    for record in event["Records"]:
        print(event['Records'][0]['messageAttributes']['TestData']['stringValue'])
        batch_item_failures.append({"itemIdentifier": record['messageId']})
    
    sqs_batch_response["batchItemFailures"] = batch_item_failures
    return sqs_batch_response


if __name__ == '__main__':
    lambda_handler(None, None)
