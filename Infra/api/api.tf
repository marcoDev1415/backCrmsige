resource "aws_api_gateway_rest_api" "sinergia-api" {
  name        = "${var.prename}-sinergia-api"
  description = "Sinergia API"
}

resource "aws_api_gateway_resource" "sinergia-access" {
  rest_api_id = aws_api_gateway_rest_api.sinergia-api.id
  parent_id   = aws_api_gateway_rest_api.sinergia-api.root_resource_id
  path_part   = "access"
}

resource "aws_api_gateway_resource" "sinergia-user" {
  rest_api_id = aws_api_gateway_rest_api.sinergia-api.id
  parent_id   = aws_api_gateway_rest_api.sinergia-api.root_resource_id
  path_part   = "user"
}

resource "aws_api_gateway_resource" "sinergia-role" {
  rest_api_id = aws_api_gateway_rest_api.sinergia-api.id
  parent_id   = aws_api_gateway_rest_api.sinergia-api.root_resource_id
  path_part   = "posts"
}
