# Testing

Guia para hacer pruebas con AWS Bash


````dockerfile

docker build -t apdcont .

docker run -d -e ENV='qas' -e PAIS='PA' -e PROCESO='201901' apdcont launch_APD_modelos

docker tag apdcont XXXX.dkr.ecr.us-east-1.amazonaws.com/analytics-apd-model-batch:201901

aws ecr get-login

## copiar lo mismo sin   ' -e none '

docker push XXXX.dkr.ecr.us-east-1.amazonaws.com/analytics-apd-model-batch:201901

````



## Container Batch Test with CLI


Create Enviroment :
```bash
aws batch create-compute-environment --cli-input-json file://job-apd-env.json --region us-east-1
```
result:

{
    "computeEnvironmentName": "batch-apd-env", 
    "computeEnvironmentArn": "arn:aws:batch:us-east-1:XXXX:compute-environment/batch-apd-env"
}

Create Job Queue :
```bash
aws batch create-job-queue --cli-input-json file://job-apd-queue.json --region us-east-1
```
result

{
    "jobQueueArn": "arn:aws:batch:us-east-1:XXXX:job-queue/batch-apd-queue", 
    "jobQueueName": "batch-apd-queue"
}

Register Job Definition :
```bash
aws batch register-job-definition --cli-input-json file://job-apd-def.json --region us-east-1
```
result

{
    "jobDefinitionArn": "arn:aws:batch:us-east-1:XXX:job-definition/batch-apd-def:1", 
    "jobDefinitionName": "batch-apd-def", 
    "revision": 1
}

Submit Job :
```bash

aws batch submit-job --cli-input-json file://submit-job-apd.json --region us-east-1
```
result

{
    "jobName": "batch-apd-job", 
    "jobId": "de61eff0-7e21-4242-b837-036746d7ce87"
}

## Container Batch Test with Python


```python

python3 -m startjob -pais {PAIS} -proceso {PROCESO}

 ```
