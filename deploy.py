import subprocess
import os
import shlex

REPO_NAME = 'hello'
ACCOUNT_ID = ''
REGION = 'us-west-2'

with open('version.txt', 'r') as f:
    version = int(f.read())
    
os.environ['CDK_DOCKER_TAG'] = f"v{version}"

print("logging in to ecr")
subprocess.check_output(f"aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin {ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com", shell=True)
print("building container")
subprocess.check_output(f"docker build -t {REPO_NAME} .", shell=True)
print("tagging and pushing container")
subprocess.check_output(f"docker tag {REPO_NAME}:latest {ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com/{REPO_NAME}:v{version}", shell=True)
subprocess.check_output(f"docker push {ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com/{REPO_NAME}:v{version}", shell=True)

with open('version.txt', 'w') as f:
    f.seek(0)
    f.write(str(version+1))

os.chdir('cdk')
print(os.listdir())
print("building deploy container")
subprocess.check_output("docker build -t cdk_deploy .", shell=True)
print("running deploy container")
process = subprocess.Popen(shlex.split(f"docker run -v {os.environ['HOME']}/.aws/:/root/.aws/ -e CDK_DOCKER_TAG={os.environ['CDK_DOCKER_TAG']} --rm cdk_deploy cdk deploy --require-approval never"),
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)

while process.poll() is None:
    line = process.stdout.readline().decode('utf-8').strip()
    if line:
        print(line)