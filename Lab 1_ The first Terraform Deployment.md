# Your first Terraform Deployment
We are going to deploy basic AWS infrastructure using Terraform.

## Setup
Before starting, insure that you have an AWS account (remember to not use the root account, but instead use an iam user under the root account), and just make temporary access keys.

Make sure that you have installed Terraform and the AWS CLI, and have set the PATH variable for your system to whatever folder you installed the Terraform application into.

The commands to set your AWS credentials/environment variables are

for Linux, MacOS, or Bash on Windows:

```shell
export AWS_ACCESS_KEY_ID="<YOUR ACCESS KEY>"
export AWS_SECRET_ACCESS_KEY="<YOUR SECRET KEY>"
```

For Powershell:
```shell
PS C:\> $Env:AWS_ACCESS_KEY_ID="<YOUR ACCESS KEY>"
PS C:\> $Env:AWS_SECRET_ACCESS_KEY="<YOUR SECRET KEY>"
```

For the default Windows cmd:
```shell
C:\> setx AWS_ACCESS_KEY_ID <YOUR ACCESS KEY>
C:\> setx AWS_SECRET_ACCESS_KEY <YOUR SECRET KEY>
```
Note that when setting environment variables, depending on the terminal/command used that it is not permanently changing the credentials. For instance, in the default Windows cmd `set` only sets the environment variable for that specific command prompt session. `setx` saves the variables for the following sessions.

To read more about configuring the AWS CLI ----> https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

^^^ All of this is out of the scope of this tutorial, please refer to the AWS and Terraform documentation! https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html ^^^

## Creating the Terraform files for main and variables

### **Step 1** 
In your chosen code editor, create a directory/file and name it whatever you like. I suggest `/terraform`.
### **Step 2**
Create 2 files, name them `main.tf` and `variables.tf`.
### **Step 3**
The following code was provided by Bryan Krausen, and can be found on his Hashicorp lab tutorials page ----> https://github.com/btkrausen/hashicorp/tree/master/terraform/Hands-On%20Labs

In the `main.tf` file, copy and paste the code below:

```hcl
# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

#Retrieve the list of AZs in the current AWS region
data "aws_availability_zones" "available" {}
data "aws_region" "current" {}

#Define the VPC
resource "aws_vpc" "vpc" {
  cidr_block = var.vpc_cidr

  tags = {
    Name        = var.vpc_name
    Environment = "practice_enviroment"
    Terraform   = "true"
  }
}

#Deploy the private subnets
resource "aws_subnet" "private_subnets" {
  for_each          = var.private_subnets
  vpc_id            = aws_vpc.vpc.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, each.value)
  availability_zone = tolist(data.aws_availability_zones.available.names)[each.value]

  tags = {
    Name      = each.key
    Terraform = "true"
  }
}

#Deploy the public subnets
resource "aws_subnet" "public_subnets" {
  for_each                = var.public_subnets
  vpc_id                  = aws_vpc.vpc.id
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, each.value + 100)
  availability_zone       = tolist(data.aws_availability_zones.available.names)[each.value]
  map_public_ip_on_launch = true

  tags = {
    Name      = each.key
    Terraform = "true"
  }
}

#Create route tables for public and private subnets
resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    gateway_id     = aws_internet_gateway.internet_gateway.id
    #nat_gateway_id = aws_nat_gateway.nat_gateway.id
  }
  tags = {
    Name      = "practice_public_rtb"
    Terraform = "true"
  }
}

resource "aws_route_table" "private_route_table" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    # gateway_id     = aws_internet_gateway.internet_gateway.id
    nat_gateway_id = aws_nat_gateway.nat_gateway.id
  }
  tags = {
    Name      = "practice_private_rtb"
    Terraform = "true"
  }
}

#Create route table associations
resource "aws_route_table_association" "public" {
  depends_on     = [aws_subnet.public_subnets]
  route_table_id = aws_route_table.public_route_table.id
  for_each       = aws_subnet.public_subnets
  subnet_id      = each.value.id
}

resource "aws_route_table_association" "private" {
  depends_on     = [aws_subnet.private_subnets]
  route_table_id = aws_route_table.private_route_table.id
  for_each       = aws_subnet.private_subnets
  subnet_id      = each.value.id
}

#Create Internet Gateway
resource "aws_internet_gateway" "internet_gateway" {
  vpc_id = aws_vpc.vpc.id
  tags = {
    Name = "practice_igw"
  }
}

#Create EIP for NAT Gateway
resource "aws_eip" "nat_gateway_eip" {
  domain     = "vpc"
  depends_on = [aws_internet_gateway.internet_gateway]
  tags = {
    Name = "practice_igw_eip"
  }
}

#Create NAT Gateway
resource "aws_nat_gateway" "nat_gateway" {
  depends_on    = [aws_subnet.public_subnets]
  allocation_id = aws_eip.nat_gateway_eip.id
  subnet_id     = aws_subnet.public_subnets["public_subnet_1"].id
  tags = {
    Name = "practice_nat_gateway"
  }
}
```
In the `variables.tf` file, copy and paste the code below:

```hcl
variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "vpc_name" {
  type    = string
  default = "practice_vpc"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "private_subnets" {
  default = {
    "private_subnet_1" = 1
    "private_subnet_2" = 2
    "private_subnet_3" = 3
  }
}

variable "public_subnets" {
  default = {
    "public_subnet_1" = 1
    "public_subnet_2" = 2
    "public_subnet_3" = 3
  }
}
```

### **Step 4**
Head on over to your terminal and change your directory to where the files are located. 

To start off, we need to initiate terraform using the `terraform init` command.

Now, feel free to use the `terraform fmt` command to format the code and make it pretty. After that, use the `terraform validate` command to check to see if the code is correct and valid to use.

### **Step 5**
Let's check if the code will run by using the command `terraform plan`. This will run for a second and then tells us how many changes are going to be made. It should say it will add 18, change 0, and destroy 0 resources.

### **Step 6**
Finally, run the `terraform apply` command, and when prompted type `yes` to confirm. You should be able to see the AWS resources in your account start being created, starting with the VPC itself. 

Make sure that the terminal doesn't prompt you any errors, and finally it's time to move on to the final step.

### **Step 7**
Let's tear down the whole infrastructure! (So that there won't be any random bills at the end of the month)

Also, don't forget about deactivating and then deleting your temporary access keys under the IAM console.

Head back to your terminal and type `terraform destroy -auto-approve` <------- the -auto-approve command does exactly what you believe it does. It automatically approves the action, so we don't have to type `yes` to confirm our intentions like we did when we applied the infrastructure.

## And that is the end of this first lab!
Be sure to check that everything was properly cleaned up in your AWS account
