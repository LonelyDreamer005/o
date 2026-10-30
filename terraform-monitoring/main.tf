terraform {
  required_version = ">= 1.0"
}

resource "terraform_data" "monitoring" {
  input = "Prometheus and Grafana Monitoring"
}

output "message" {
  value = terraform_data.monitoring.output
}