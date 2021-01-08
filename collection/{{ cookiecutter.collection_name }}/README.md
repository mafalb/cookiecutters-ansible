# Ansible Collection - {{ cookiecutter.collection_namespace }}.{{ cookiecutter.collection_name }}

{% if cookiecutter.hosted_by == 'github' %}
|||
|---|---|
|master|![master branch]({{ cookiecutter.repository_url }}/workflows/CI/badge.svg?branch=master)|
|dev|![dev branch]({{ cookiecutter.repository_url }}/workflows/CI/badge.svg?branch=dev)|
{% endif %}

Ansible collection {{ cookiecutter.collection_namespace }}.{{ cookiecutter.collection_name }}

## Roles

### [{{ cookiecutter.collection_namespace }}.{{ cookiecutter.collection_name }}.{{ cookiecutter.collection_name }}](roles/{{ cookiecutter.collection_name }}/README.md)

## License

{{ cookiecutter.license }}
