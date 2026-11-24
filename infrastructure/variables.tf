variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "inventory"
}

variable "my_ip" {
  description = "128.119.202.170"
  type        = string
}

# variable "ami_id" {
#   description = "Ubuntu 24.04 AMI ID"
#   type        = string
# }