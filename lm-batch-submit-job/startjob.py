import boto3
import json
from utils.config import *

batch = boto3.client(
    service_name='batch',
    region_name='us-east-1',
    endpoint_url='https://batch.us-east-1.amazonaws.com')


def lambda_handler(event, context):
    print(json.dumps(event))
    message = get_message_hash(event)
    print(message)

    country = message['codpais']
    closure_campaign = message['aniocampana_cierre']

    print("submit job: ", country, ":", closure_campaign)

    submit_job(code_country=country, year_campaign=closure_campaign)


def register_job_definition(cod_country, year_campaign):
    # Set up a batch client
    session = boto3.session.Session()
    client = session.client('batch')

    response = client.register_job_definition(
        jobDefinitionName='batch-apd-def',
        type='container',
        containerProperties={
            'image': '639556434474.dkr.ecr.us-east-1.amazonaws.com/analytics-apd-model-batch:latest',
            'vcpus': execute_parameters[enum_country[cod_country].value]['vcpus'],
            'memory': execute_parameters[enum_country[cod_country].value]['memory'],
            'command': ['launch_APD_modelos'],
            'jobRoleArn': 'arn:aws:iam::639556434474:role/ecsTaskExecutionRole',
            'volumes': [],
            'environment': [
                {
                    'name': 'PAIS',
                    'value': cod_country
                },
                {
                    'name': 'PROCESO',
                    'value': str(year_campaign)
                }
            ],
            'mountPoints': [],
            'user': 'nobody'
        }
    )

    return response


def submit_job(code_country, year_campaign):
    job_definition_ret = register_job_definition(cod_country=code_country, year_campaign=year_campaign)

    # Set up a batch client
    session = boto3.session.Session()
    client = session.client('batch')

    # Submit the job
    job1 = client.submit_job(
        jobName='batch-apd-job',
        jobQueue='batch-apd-queue',
        jobDefinition=job_definition_ret['jobDefinitionName']+':'+str(job_definition_ret['revision'])
    )
    print("Started Job: {}".format(job1['jobName']))
    print(job1)


def get_message_hash(event):
    return json.loads(event['Records'][0]['body'])
