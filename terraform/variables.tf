variable "bronze_bucket_name" {
  description = "Bucket used to storage raw data."
  default     = "data-platform-bronze"
}

variable "silver_bucket_name" {
  description = "Bucket to store transformed data."
  default     = "data-platform-silver"
}

variable "gold_bucket_name" {
  description = "Bucket to store clean data that is ready for production analytics."
  default     = "data-platform-gold"
}