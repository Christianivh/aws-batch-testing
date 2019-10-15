import argparse
import boto3
from utils.config import *

batch = boto3.client(
    service_name='batch',
    region_name='us-east-1',
    endpoint_url='https://batch.us-east-1.amazonaws.com')

cloudwatch = boto3.client(
    service_name='logs',
    region_name='us-east-1',
    endpoint_url='https://logs.us-east-1.amazonaws.com')

parser = argparse.ArgumentParser()
parser.add_argument('-pais', action='store', dest='pais',
                    help='Codigo de pais que va ser corrido')
parser.add_argument('-proceso', action='store', dest='anoCampanaProcesso',
                    help='La fecha de processo de campana en formato YYYYMM')


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

    #print('RequestId: ', response['ResponseMetadata']['RequestId'])
    #print('revision: ', response['revision'])
    #print('jobDefinitionArn: ', response['jobDefinitionArn'])
    #print(response)
    return response


if __name__ == "__main__":
    args = parser.parse_args()
    code_country = args.pais
    year_campaign_process = int(args.anoCampanaProcesso)
    job_definition_ret = register_job_definition(cod_country=code_country, year_campaign=year_campaign_process)

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
