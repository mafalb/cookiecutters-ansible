# Ansible Role {{ cookiecutter.role }}

{% if cookiecutter.hosted_by == 'github' -%}
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

{{ cookiecutter.license }}
