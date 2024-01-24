terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "oregon"
  region = "us-west-2"
}

  #resource
  resource "aws_instance" "first-sedmo" {
    ami = data.aws_ami.first-demo.id
    instance_type = "t3.micro"
  }
