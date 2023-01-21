// Common Variables

variable "AWS_ACCESS_KEY_ID" {
  description = "AWS Access key"
  type = string
}

variable "AWS_SECRET_ACCESS_KEY" {
  description = "AWS Secret key"
  type = string
}

variable "AWS_REGION" {
  description = "AWS preferred region"
  type = string
}

variable "app_name" {
  description = "Application name"
  type = string
}

variable "environment" {
  description = "Application lifecycle stage"
  type = string
}

variable "additional_tags" {
  description = "Tags used to identify the project and other details"
  default     = {}
  type        = map(string)
}

variable "vpc_id" {
  description = "AWS Sandbox VPC"
}

variable "backend_bucket" {
  description = "Terraform backend for tf.state files"
}

// DynamoDB variables 

variable "link" {
  description = "Oncall re-direct link"
}

variable "hash_key" {
  description = "DynamoDB partition key"
  default = "index"
}

variable "range_key" {
  description = "DynamoDB range key"
  default = "turn"
}

variable "user1" {
  description = "User for item 1"
}

variable "email1" {
  description = "Email for item 1"
}

variable "user2" {
  description = "User for item 2"
}

variable "email2" {
  description = "Email for item 2"
}

variable "user3" {
  description = "User for item 3"
}

variable "email3" {
  description = "Email for item 3"
}