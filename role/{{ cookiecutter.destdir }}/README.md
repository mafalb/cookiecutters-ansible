# Ansible Role {{ cookiecutter.role }}

{% if cookiecutter.hosted_by == 'github' and cookiecutter.role.split('.')|length == 2 -%}
|||
|---|---|
|master|![master branch]({{ cookiecutter.repository_url }}/workflows/CI/badge.svg?branch=master)|
|dev|![dev branch]({{ cookiecutter.repository_url }}/workflows/CI/badge.svg?branch=dev)|
{% endif %}

## Basic Usage

```yaml
- name: install {{ cookiecutter.role }}
  hosts: localhost
  roles:
  - role: {{ cookiecutter.role }}
```

## Variables

## License

Copyright (c) 2021 {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>

{{ cookiecutter.license }}
