import boto3

sm = boto3.client("sagemaker")

response = sm.start_pipeline_execution(
    PipelineName="loan-approval-pipeline"
)

print("Execution ARN:", response["PipelineExecutionArn"])
