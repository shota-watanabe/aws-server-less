import json
import logging
import boto3
from list_tasks import list_tasks

# DynamoDBテーブルの初期化
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TasksTable')

# ロガーの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
  try:
    logger.debug("Received event: %s", json.dumps(event))

    tasks = list_tasks(table)
    logger.info(f"Get Task List: {tasks}")

    # 成功レスポンスを返す
    return {
      "statusCode": 200,
      "body": json.dumps({
        "tasks": tasks
      })
    }

  except Exception as e:
    logger.error(f"Unexpected error occurred: {str(e)}", exc_info=True)
    return error_handler(500, "An unexpected error occurred")

def error_handler(statusCode: int, message: str):
  return {
        "statusCode": statusCode,
        "body": json.dumps({
            "error": message
        })
    }
