# Session Stickiness using an ALB
# Purpose
Demonstrate session stickiness when enabled, and when disabled on an Application Load Balancer’s target group.

Link to the original repository made by Adrian Cantrill: https://github.com/acantril/learn-cantrill-io-labs/tree/master/00-aws-simple-demos/aws-alb-session-stickiness

# Resources
Template used for resource creation: https://learn-cantrill-labs.s3.amazonaws.com/aws-simple-demos/aws-alb-session-stickiness/ALBSTICKINESS.yaml
This creates a VPC with 3 public subnets, with an internet gateway attached. The subnets have 2 EC2 instances per subnet, totaling to 6 EC2 instances. They are placed within the target group of an Application Load Balancer which has session stickiness turned off to begin.
The Load Balancer has a LaunchTemplate which defines how instances should be built within the target group.

# Demo
We first begin by deploying the template in cloud formation. 
There was an error that occurred and a rollback was initiated, however redeploying the architecture fixed the issue.

First, I want to demonstrate what occurs when you connect without session stickiness enabled. 
We head to the EC2 area on the AWS console.
Go to <kbd>load balancers</kbd>.
Copy the DNS name.
Open it in a new tab. 

If we refresh several times we can see that the background color and gif change. 
It may repeat a few times, but in general it should change a couple of times.

Head to the <kbd>target groups</kbd> tab under load balancers.
We select the target group that has been created, then click on attributes. 
We will then click edit, and change the session stickiness to be on. 
You can leave the values as default, or change them to be minutes instead of 1 day.

![Screenshot 2024-01-10 162537](https://github.com/MayoNotMayo/AWS-Projects/assets/100898272/eaec1774-2864-4531-9a7f-0ff98c6d98d2)


If we go back to the load balancer’s DNS tab and hit refresh several times, we can see that the same EC2 instance, with the same background color and gif will continue to load. 

This is how we are able to demonstrate session stickiness.
