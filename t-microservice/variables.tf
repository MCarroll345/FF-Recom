# modules/microservice/variables.tf
variable "service_name" {
  description = "Name of the microservice"
  type        = string
  default     = "FF-Recom"
}

variable "container_image" {
  description = "Docker image for the microservice"
  type        = string
  default     = "mcarroll321/recom-test:latest"
}

variable "container_port" {
  description = "Port the container exposes"
  type        = number
  default     = 8080
}

variable "desired_count" {
  description = "Number of instances to run"
  type        = number
  default     = 2
}

variable "cpu" {
  description = "CPU units for the task"
  type        = number
  default     = 256
}

variable "memory" {
  description = "Memory for the task in MiB"
  type        = number
  default     = 512
}

variable "vpc_id" {
  description = "ID of the VPC"
  type        = string
  default     = "vpc-009b673acd08290d8"
}

variable "subnet_ids" {
  description = "Subnet IDs for the service"
  type        = list(string)
  default     = ["subnet-0e669f11a52309ead", "subnet-073a47939db6ba8fc"]
}

variable "environment_variables" {
  description = "Environment variables for the container"
  type        = map(string)
  default     = {}
}