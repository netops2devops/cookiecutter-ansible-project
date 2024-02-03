# About 
A slightly opinionated `cookiecutter` template that creates a barebones Ansible project with static inventory mostly for my own personal use. The template creates a virtual environment (venv) and installs the following inside it
- `ansible` 
- `molecule` for ansible role testing
- `molecule-docker` run molecule tests inside a container
- `ansible-lint`
- `flake8`

# Requirements 
- [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)
- [Poetry](https://python-poetry.org)

# Usage
Create a new ansible project by running
```
cookiecutter https://github.com/netops2devops/cookiecutter-ansible-project.git

❯ cookiecutter cookiecutter-ansible-project
  [1/9] project_name (new-ansible-project):
  [2/9] project_short_description (My exciting new Ansible project):
  [3/9] full_name (Kapil Agrawal):
  [4/9] email (noneofyourbusiness@email.com):
  [5/9] vcs_username (netops2devops):
  [6/9] version (0.0.1):
  [7/9] ansible_version (latest):
  [8/9] setup_pre_commit_hooks [y/n] (y):
  [9/9] initialize_git [y/n] (y):

```

Barebones Ansible project gets created as shown below
```
❯ tree
.
├── README.md
├── ansible.cfg
├── inventory
│   ├── group_vars
│   │   └── all.yml
│   ├── host_vars
│   │   └── dummy.yml
│   └── hosts.ini
├── playbooks
│   └── playbook.yml
├── poetry.lock
└── pyproject.toml

5 directories, 8 files
```

To create a new Ansible role 
```
# source .venv/bin/activate 
.venv ❯ ansible-galaxy role init roles/new_role
```


## Author
netops2devops (Kapil Agrawal)
