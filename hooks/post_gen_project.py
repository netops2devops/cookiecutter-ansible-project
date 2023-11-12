import os
import subprocess

print()
print("----- INSTALLING PACKAGES -----")
print()

subprocess.run(["poetry", "install"])
print("----- GENERATING PROJECT -----")

if "{{cookiecutter.initialize_git}}":
    subprocess.run(["git", "init", "."])
else:
    pass

if "{{cookiecutter.setup_pre_commit_hooks}}":
    subprocess.run(["pre-commit", "install"])
else:
    subprocess.run(["rm", ".pre-commit-config.yml"])
