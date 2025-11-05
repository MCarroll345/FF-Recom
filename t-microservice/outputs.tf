# modules/microservice/outputs.tf
output "service_url" {
  description = "URL of the deployed microservice"
  value       = aws_ecs_service.microservice.name
}

output "security_group_id" {
  description = "ID of the security group created for the service"
  value       = aws_security_group.microservice.id
}