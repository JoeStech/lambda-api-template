import os
import aws_cdk as cdk
import courthouse_stack

app = cdk.App()
courthouse_stack.CourthouseStack(app, "courthouse")
app.synth()