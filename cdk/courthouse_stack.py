from aws_cdk import (
aws_lambda as lambda_,
aws_apigateway as apigw,
aws_iam as iam,
aws_ecr as ecr,
aws_certificatemanager as acm,
aws_route53 as route53,
Duration,
Stack)
from constructs import Construct
import os

class HelloStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # execution role
        #lambda_role = iam.Role(self, id="hello-lambda")
        
        repo = ecr.Repository.from_repository_name(self, "helloRepo", "hello")
        
        hello_lambda = lambda_.DockerImageFunction(self,
            "helloLambda",
            code=lambda_.DockerImageCode.from_ecr(
                repository=repo,
                tag=os.environ["CDK_DOCKER_TAG"]
            ),
            memory_size=2048,
            timeout=Duration.seconds(60)
        )
        
        # do auth inside lambda
        api = apigw.LambdaRestApi(self,
            "hello-endpoint",
            handler=hello_lambda
        )
        
        custom_domain = apigw.DomainName(
            self,
            "custom-domain",
            domain_name="",
            certificate=acm.Certificate.from_certificate_arn(self,'cert',""),
            endpoint_type=apigw.EndpointType.EDGE
        )
        
        apigw.BasePathMapping(
            self,
            "base-path-mapping",
            domain_name=custom_domain,
            rest_api=api
        )
        
        hosted_zone = route53.HostedZone.from_hosted_zone_attributes(
            self,
            "hosted-zone",
            hosted_zone_id="",
            zone_name=""
        )
        
        route53.CnameRecord(
            self,
            "cname",
            zone=hosted_zone,
            record_name="hello",
            domain_name=custom_domain.domain_name_alias_domain_name
        )