# Cookiecutters for ansible

|||
|---|---|
|master|![master branch](https://github.com/mafalb/cookiecutters-ansible/workflows/CI/badge.svg?branch=master)|
|dev|![dev branch](https://github.com/mafalb/cookiecutters-ansible/workflows/CI/badge.svg?branch=dev)|

create a basic ansible collection:

```bash
cookiecutter https://github.com/mafalb/cookiecutters-ansible --directory collection
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
cookiecutter\
 --overwrite-if-exists\
 --config-file httpd/cookiecutter.yaml --no-input\
 https://github.com/mafalb/cookiecutters-ansible --directory molecule
```

files for molecule were added to the existing collection

```bash
cookiecutter\
 --overwrite-if-exists\
 --config-file httpd/cookiecutter.yaml --no-input\
 https://github.com/mafalb/cookiecutters-ansible --directory github-actions
```

```bash
cookiecutter\
 --overwrite-if-exists\
 --config-file httpd/cookiecutter.yaml\
 https://github.com/mafalb/cookiecutters-ansible --directory role
```

## License

Copyright (c) 2021 Markus Falb <markus.falb@mafalb.at>

GPL-3.0-or-later
