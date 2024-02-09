terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.25.0"
    }

  }

  required_version = ">= 1.2.7"
}

provider "aws" {
  profile = "sinergia-consultores"
  region  = "us-east-1"
}

module "api" {
  source = "./api"
  prename = terraform.workspace
}

output "api_b2b" {
  value = module.api
}


