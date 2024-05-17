# Implementing an AWS CI/CD Pipeline using CodePipeline and CodeBuild

Prerequisites:
A GitHub account
An AWS account
Git installed

The architecture that I will be deploying:
![PipelineArch.png](https://github.com/MayoNotMayo/AWS-Projects/blob/main/LabPhotos/PipelineArch.png)

## Step 1: Setting up a GitHub Repository

Start by forking and cloning the example application, provided by AWS to be used with Elastic Beanstalk using the URL below. 

https://github.com/aws-samples/aws-elastic-beanstalk-express-js-sample

Press the fork icon in the top right corner and select create fork. Make sure the fork has been created in your repository and then click on the green code drop down and copy the URL.

To clone the repository onto your local system
type this into the command line
```shell 
git clone https://github.com/YOUR-USERNAME/aws-elastic-beanstalk-express-js-sample
```
Change your directory to enter the new folder created from the clone.

Type
```shell
git add app.js
git commit -m "add app.js"
```
Once finished push it to your GitHub with
```shell
git push
```

## Step 2: Configure and Deploy the sample app to AWS Elastic BeanStalk
Head to the AWS console and go to Elastic BeanStalk. Create an application and choose the Web server environment. Under Platform choose `Node.js` and for the Application Code section select `Sample Application`

You will need an IAM Role to select as the instance profile for the EC2 instance that BeanStalk is going to create, and you'll need a role for BeanStalk to assume as well. Both should be able to be created automatically through the BeanStalk console, but if not then follow these instructions to create an IAM Role for EC2. 

https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-iam-instance-profile.html

Once finished and deployed the application should be up and running, and to test it we can click the URL link under the Elastic BeanStalk deployment UI. It should display a large green Congratulations message.



![pipeline.png](https://github.com/MayoNotMayo/AWS-Projects/blob/main/LabPhotos/pipeline.png)
![review.png](https://github.com/MayoNotMayo/AWS-Projects/blob/main/LabPhotos/review.png)
![pipelinereview.png](https://github.com/MayoNotMayo/AWS-Projects/blob/main/LabPhotos/pipelinereview.png)
