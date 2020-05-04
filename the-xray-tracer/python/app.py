#!/usr/bin/env python3

from aws_cdk import core

from the_xray_tracer.the_xray_tracer_stack import TheXrayTracerStack
from the_xray_tracer.the_http_flow_stack import TheHttpFlowStack
from the_xray_tracer.the_dynamo_flow_stack import TheDynamoFlowStack


app = core.App()
xray_tracer = TheXrayTracerStack(app, "the-xray-tracer")
TheHttpFlowStack(app, 'the-http-flow-stack', sns_topic_arn=xray_tracer.sns_topic_arn)
TheDynamoFlowStack(app, 'the-dynamo-flow-stack', sns_topic_arn=xray_tracer.sns_topic_arn)

app.synth()
