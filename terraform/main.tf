terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "ca-west-1"
}

resource "aws_s3_bucket" "terraform_state" {
  bucket = "terraform-state-bucket"
}