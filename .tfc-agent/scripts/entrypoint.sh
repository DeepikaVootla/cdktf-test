#!/bin/bash

set -e

echo "Installing pipenv & Python deps..."
pip install pipenv --user

echo "Installing packages from Pipfile..."
pipenv install --dev

echo "Synthesizing CDKTF to generate cdk.tf.json..."
pipenv run python main.py

echo "Running Terraform Init..."
terraform init

echo "Running Terraform Plan..."
terraform plan

# To Auto-apply

# echo "Running Terraform Apply..."
# terraform apply -auto-approve
