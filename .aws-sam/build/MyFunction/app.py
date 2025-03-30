import json

# テスト用のLambda関数
# event... 関数を呼び出した際に 入力として渡されるデータを格納している
# context... 関数の実行環境や設定に関するデータ を格納している
def lambda_handler(event, context):
    print("テスト用のLambda関数を実行 by SAM") # 出力先は AWS CloudWatch Logs(書き込み権限が必要)
    print(f"Event: {event}")
    print(f"Context: {context}")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello, World! by SAM"})
    }
