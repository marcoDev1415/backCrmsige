
output "sinergia-api" {
  description = "REST API sinergia-api"
  value       = aws_api_gateway_rest_api.sinergia-api.id
}

output "sinergia-access" {
  value       = aws_api_gateway_resource.sinergia-access.id
}

output "sinergia-user" {
  value       = aws_api_gateway_resource.sinergia-user.id
}

output "sinergia-role" {
  value       = aws_api_gateway_resource.sinergia-role.id
}

