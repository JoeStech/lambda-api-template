# lambda-api-template
A CDK template for a Docker-based AWS Lambda API.

To use, first build a container to run on Lambda using the root Dockerfile.

Next, fill out the global variables in deploy.py with relevant values, including the ECR repo name where you have stored your Docker image.

In the `cdk` directory, you may want to change the 'hello' stack name values to something unique to your project.

Edit app_handler.py to include your API logic.

Run `deploy.py` and have fun with your new serverless API!


