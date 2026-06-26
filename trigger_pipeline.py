import boto3

sm = boto3.client("sagemaker")

pipeline = Pipeline(
    name="loan-approval-pipeline",
    steps=[...],
    sagemaker_session=session
)

pipeline.upsert(role_arn=role)

response = sm.start_pipeline_execution(
    PipelineName="loan-approval-pipeline"
)

print("Execution ARN:", response["PipelineExecutionArn"])
