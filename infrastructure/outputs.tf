output "security_group_id" {
  description = "ID of the inventory security group"
  value       = aws_security_group.inventory_sg.id
}

output "iam_instance_profile_name" {
  description = "IAM instance profile for EC2"
  value       = aws_iam_instance_profile.ec2_profile.name
}

output "ec2_public_ip" {
  description = "Public IP address of EC2"
  value       = aws_instance.inventory_server.public_ip
}

output "ec2_public_dns" {
  description = "Public DNS name of EC2"
  value       = aws_instance.inventory_server.public_dns
}

output "ec2_instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.inventory_server.id
}