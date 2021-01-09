# Cookiecutters for ansible

|||
|---|---|
|master|![master branch](https://github.com/mafalb/cookiecutters-ansible/workflows/CI/badge.svg?branch=master)|
|dev|![dev branch](https://github.com/mafalb/cookiecutters-ansible/workflows/CI/badge.svg?branch=dev)|

cookiecutters for ansible development

```bash
$ cookiecutter https://github.com/mafalb/cookiecutters-ansible --directory collection
```

This creates not only the directories and files for the ansible collection but also a cookiecutter.yaml with the context

```yaml
default_context:
    collection_namespace: "mafalb"
    collection_name: "httpd"
    author_name: "Markus Falb"
    author_email: "markus.falb@mafalb.at"
    license: "GPL-3.0-or-later"
    repository_url: "https://github.com/mafalb/ansible-collection-httpd"
    hosted_by: "github"
```

e.g. in the shell:

```bash
cookiecutter --config-file httpd/cookiecutter.yaml --no-input https://github.com/mafalb/cookiecutters-ansible --directory molecule
cookiecutter --config-file httpd/cookiecutter.yaml --no-input https://github.com/mafalb/cookiecutters-ansible --directory github-actions
cookiecutter --config-file httpd/cookiecutter.yaml --no-input https://github.com/mafalb/cookiecutters-ansible --directory role
```

## License

Copyright (c) 2021 Markus Falb
GPLv3 or later
