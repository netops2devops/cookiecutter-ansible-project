# About 
A slightly opinionated `cookiecutter` template that creates a barebones Ansible project with static inventory mostly for my own personal use. The template creates a virtual environment (venv) and installs the following inside it
- `ansible` (specified version or latest by default)
- `molecule`  for ansible role testing
- `molecule-docker` run molecule tests inside a container
- `ansible-lint`
- `flake8`

# Requirements 
- cookiecutter 

# Usage
Create a new ansible project by running
```
cookiecutter https://github.com/netops2devops/cookiecutter-ansible-project.git
```

# To Do


# Author 
Kapil Agrawal 