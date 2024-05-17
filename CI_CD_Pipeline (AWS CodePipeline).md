# Implementing an AWS CI/CD Pipeline using CodePipeline and CodeBuild

Prerequisites:

- A GitHub account

- An AWS account

- Git installed

```diff
- Warning: Be sure to keep AWS in the US-east-1 region for everything you do, OR keep AWS in the same region for every deployment/build you complete. If not, then there will be errors, as some AWS services are regional, and cannot interact outside of the region created and deployed into.
```

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

Here is our architecture at this current state:

![HalfwayPipeArch.png](https://github.com/MayoNotMayo/AWS-Projects/blob/main/LabPhotos/HalfwayPipeArch.png)

## Step 3: Creating a CodeBuild Project
Head to the CodeBuild console and select `Create project`

Under the `Source provider` select `GitHub`

Make sure `Connect using OAuth` is selected.

Choose the connect to GitHub button and log into GitHub so it can verify who you are.

Continue on and select `Repository in my GitHub account`

Be sure to select the example node.js app that we cloned in Step 1.

Under image check that `Amazon Linux 2` is selected. Select `Standard` for the runtime. Select `aws/codebuild/amazonlinux2-x86_64-standard:3.0` from the dropdown.

Make sure that create a New Service Role is selected.

Next step is to `Insert Build commands` and `Switch to editor`

Now copy and paste this code into the Buildspec file
```shell
version: 0.2
phases:
    build:
        commands:
            - npm i --save
artifacts:
    files:
        - '**/*'
```
This Buildspec file is read by CodeBuild to set the configuration for the build. The artifacts section at the bottom points CodeBuild towards the build output artifact in the build environment to upload to our output bucket.

Finally, click `Create build project` and then press `Start Build` to confirm that it works and connects through.

## Step 4: Setting up the Pipeline

First, head to the CodePipeline console and create a new pipeline. Select New service role.

Under the source stage: select `GitHub version 1` from the Source provider, connect to GitHub as we did before, make sure the main branch of your repository is selected and select `GitHub webhooks`

Under the build stage: Select AWS CodeBuild, then be sure that the region selected is the same region as your app (US-east-1).

Under the deploy stage: Select `AWS Elastic Beanstalk` from the dropdown. Be careful with the region here. If you can't find your application then chances are you deployed it in a different region. 

Create your pipeline. Below is what mine looks like before we continue:

![pipeline.png](https://github.com/MayoNotMayo/AWS-Projects/blob/main/LabPhotos/pipeline.png)

## Review
We are going to implement a review stage so that we have to manually accept any proposed changes to our code on GitHub. Without approving the changes, our code won't be pushed to our GitHub repository.

![review.png](https://github.com/MayoNotMayo/AWS-Projects/blob/main/LabPhotos/review.png)

Click `Edit` on our pipeline and select `Add stage`. Name it "Review" to keep it simple and easy to understand.

After you add the stage, press the `Add action group` button, and call the Action name something along the lines of "Manual_Review" 

From the action provider dropdown select `Manual Review` and press Done. Be sure to Save your changes. 

Now, to test the manual review with our pipeline, open app.js in a code editor and change the message on line 5 and save the file. Just as before, add, commit, and then push the changes using the git commands in command line. 

Quickly head over to the AWS tab again and watch as the code moves through the Pipeline. When the option appears, at the review stage press the review button and accepts the changes. Here we would write a comment about the changes made, and then watch as the code gets pushed all the way through to GitHub.

Once finished you should be able to see your new line 5 on GitHub.

![pipelinereview.png](https://github.com/MayoNotMayo/AWS-Projects/blob/main/LabPhotos/pipelinereview.png)
