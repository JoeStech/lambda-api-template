import os
import aws_cdk as cdk
import hello_stack

app = cdk.App()
hello_stack.HelloStack(app, "hello")
app.synth()