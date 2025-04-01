import logging

# ロガーの設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def list_tasks(task_table):

  logger.info("Starting to fetch tasks from DynamoDB")

  try:
    response = task_table.scan()
    tasks = response.get("Items", [])
    logger.debug("Success to get Tasks list: {tasks}")

    return tasks

  except Exception as e:
    error_message = f"Failed to fetch tasks from DynamoDB: {str(e)}"
    logger.error(error_message, exc_info=True)
    raise RuntimeError(error_message)
