# Streaming Finance Data with AWS Lambda

For this project, I used a Lambda function to generate near real time finance data records for interactive querying. 

This project consists of three major infrastructure elements that work in tandem:
1.	A lambda function that gathers our data (DataTransformer)
2.	A Kinesis stream that holds our data (DataCollector)
3.	A serverless process that allows us to query our S3 data (DataAnalyzer)

## Infrastructure

![Infrastructure](assets/Infrastructure.png)


In the collector lambda, using the yfinance module ([documentation ](https://github.com/ranaroussi/yfinance)here), I grabbed one full day’s worth of stock HIGH and LOW prices for each company listed above on Thursday, May 14th 2020, at an one minute interval. Note that by “full day” we mean one day of stock trading, which is not 24 hours.

- Facebook (FB)
- Shopify (SHOP)
- Beyond Meat (BYND)
- Netflix (NFLX)
- Pinterest (PINS)
- Square (SQ)
- The Trade Desk (TTD)
- Okta (OKTA)
- Snap (SNAP)
- Datadog (DDOG)

## DataCollector Lambda Configuration Page 

![Lambda](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/assets/lambda.png?raw=true)

## Kinesis Data Firehose Delivery Stream Monitoring

![Firehose](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/assets/firehose.png?raw=true)

## Athena Ad-Hoc Queries

![Firehose](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/assets/athena.png?raw=true)

## [Analysis - Check it out ](https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/Analysis.ipynb)
https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda/blob/master/Analysis.ipynb


### * Lambda Deployment Package

In order to run lambda functions that also manage dependencies, a "deployment package" must be leveraged, basically a zip file containing your lambda code and all the dependencies it needs all packaged into a single artifact.

This [repo](https://github.com/mottaquikarim/STA9760_simple_deployment_package) from Taq Karim provides a few tools that will help you manage your lambda functions and the dependencies.


***Jack Yang Copy Right 2020***
https://github.com/JackJoeng/Streaming-Finance-Data-with-AWS-Lambda

