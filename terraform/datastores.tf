resource "aws_s3_bucket" "bronze_bucket" {
  bucket = var.bronze_bucket_name
}
