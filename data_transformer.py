import json
import boto3
import os
import sys
import yfinance as yf

company = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']

kinesis = boto3.client("kinesis", "us-east-1")

def lambda_handler(event, context):
    for ticker in company:
        data = yf.download(ticker, start='2021-11-30', end='2021-12-01', interval = "5m")

        for datetime, value in data.iterrows():
            record = {'high': value['High'], 
                'low': value['Low'],
                'ts': str(datetime), 
                'name': ticker}
            
            as_jsonstr = json.dumps(record, separators=(',', ': '))+"\n"

            kinesis.put_record(
                StreamName='STA9760f2021_P3_STREAM',
                Data= as_jsonstr.encode('utf-8'),
                PartitionKey="partitionkey")
                
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }