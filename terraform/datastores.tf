resource "aws_s3_bucket" "bronze_bucket" {
  bucket = "${var.bronze_bucket_name}"
}

resource "aws_s3_bucket" "silver_bucket" {
  bucket = "${var.silver_bucket_name}"
}

resource "aws_s3_bucket" "gold_bucket" {
  bucket = "${var.gold_bucket_name}"
}
