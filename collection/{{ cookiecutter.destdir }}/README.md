# Ansible Collection - {{ cookiecutter.collection }}

{% if cookiecutter.hosted_by == 'github' %}
|||
|---|---|
|master|![master branch]({{ cookiecutter.repository_url }}/workflows/CI/badge.svg?branch=master)|
|dev|![dev branch]({{ cookiecutter.repository_url }}/workflows/CI/badge.svg?branch=dev)|
{% endif %}

Ansible collection {{ cookiecutter.collection }}

## Roles

### [{{ cookiecutter.collection }}.roleX](roles/roleX }}/README.md)

## License

Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
SPDX-License-Identifier: {{ cookiecutter.license }}
