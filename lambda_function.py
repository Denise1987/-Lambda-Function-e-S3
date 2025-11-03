import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = os.environ.get('BUCKET_NAME', 'meu-bucket-exemplo')
    file_name = 'example_file.txt'
    
    # Faz upload de um arquivo de exemplo para o S3
    try:
        s3.upload_file(f'/tmp/{file_name}', bucket_name, file_name)
        return {
            'statusCode': 200,
            'body': f'Arquivo {file_name} enviado para {bucket_name} com sucesso!'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Erro: {str(e)}'
        }
