# modules/microservice/variables.tf
variable "service_name" {
  description = "Name of the microservice"
  type        = string
}

variable "container_image" {
  description = "Docker image for the microservice"
  type        = string
}

variable "container_port" {
  description = "Port the container exposes"
  type        = number
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
}

variable "subnet_ids" {
  description = "Subnet IDs for the service"
  type        = list(string)
}

variable "environment_variables" {
  description = "Environment variables for the container"
  type        = map(string)
  default     = {}
}