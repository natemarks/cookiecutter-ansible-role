Cookiecutter template for ansible role projects

 - Setup a minimal project structure
 - get molecule linting and test working immediately
 - use .env to provide secure variables to test runs without leaking into the repo
 - provide testinfra example
 - provide a Makefile that useful locally and in pipelines


## Usage
If you don't want to install cookiecutter system wide, just install it in a .venv
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip setuptools cookiecutter
cookiecutter gh:natemarks/cookiecutter-ansible-role

role_name [my_role]: ghj
github_user [natemarks]:
author [Nate Marks]:
ansible_version [4.4.0]:
molecule_version [3.4.0]:
ansible_lint_version [5.1.2]:
galaxy_tag_1 [example_tag1]:
galaxy_tag_2 [example_tag2]:
galaxy_tag_3 [example_tag3]:

tree
.
└── arole_ghj
    ├── Makefile
    ├── defaults
    │   └── main.yml
    ├── env.example
    ├── files
    ├── handlers
    ├── meta
    │   └── main.yml
    ├── molecule
    │   └── default
    │       ├── converge.yml
    │       ├── example_requirements.yml
    │       ├── group_vars
    │       ├── host_vars
    │       │   ├── ubuntu20.04-all
    │       │   └── ubuntu20.04-only-ac
    │       ├── hosts
    │       ├── molecule.yml
    │       └── tests
    │           └── test_default.py
    ├── playbook
    ├── scripts
    │   └── generate_env.sh
    ├── tasks
    │   └── main.yml
    ├── templates
    │   └── tmp_version_file.j2
    ├── tests
    │   ├── inventory
    │   └── test.yml
    └── vars

16 directories, 16 files
```