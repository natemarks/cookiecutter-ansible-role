 # {{ cookiecutter.github_user }}.arole-{{ cookiecutter.role_name }}
 This is a template project for the role {{ cookiecutter.github_user }}.{{ cookiecutter.role_name }}. The project directory is arole-{{ cookiecutter.role_name }}.
 
Molecule test (configured in converge.yml) must be configured with the project (directory) name. It will not reliably recognize the galaxy role name ({{ cookiecutter.github_user }}.{{ cookiecutter.role_name }}) as defined in meta/main.yml.


## Getting started

Init your repo:
```shell
cd arole-{{ cookiecutter.role_name }}
git init .
git add -A
git commit -am "initial"
git remote add origin git@github.com:{{ cookiecutter.github_user}}/arole-{{ cookiecutter.role_name }}.git
```

Setup your virtual environment and run molecule test
```shell
make clean-venv
make molecule-test
```

NOTE: Molecule uses the project directory name (arole-{{ cookiecutter.role_name }}) as the role name.  The hyphen in the project name makes it an invalid role name so I skip the role_name check in the .ansible-lint config


To execute an example playbook, configure it in example/.  If there are no required roles, delete the requirements.yml. The galaxy install will fail on an empty requirements file
```shell

bash -c 'curl "https://raw.githubusercontent.com/natemarks/pipeline-scripts/v0.0.32/scripts/run_playbook.sh" | bash -s --  -p example'
```