locals {

  common_tags = {
    application       = "${var.app_name}"
    environment       = "${var.environment}"
    region            = "${var.AWS_REGION}"
  }

  private_subnet_ids = [for s in data.aws_subnet.private : s.id]
  public_subnet_ids  = [for s in data.aws_subnet.public : s.id]

}