
#simple data source to deploy an ec2 intance in AWS
data "aws_ami" "first-demo" {
  most_recent = true
  owners      = ["amazon"]

  # Add other required parameters
  filter {
    name  = "name"
    values = ["amzn2-ami-hvm*"]
  }
}
