import boto3
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.session import Session
from sagemaker.workflow.steps import TrainingStep
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.sklearn.estimator import SKLearn
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
