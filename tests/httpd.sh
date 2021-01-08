#/bin/bash

echo 'creating collection'
cookiecutter --config-file tests/httpd.yaml --no-input collection -o /tmp 

echo 'creating molecule'
cookiecutter -f --config-file /tmp/httpd/cookiecutter.yaml --no-input molecule -o /tmp

echo creating github-actions
cookiecutter -f --config-file /tmp/httpd/cookiecutter.yaml --no-input github-actions -o /tmp
