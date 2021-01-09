#/bin/bash

echo 'creating role'
cookiecutter --config-file tests/standalone-role.yaml --no-input role -o /tmp role=example.roleX
