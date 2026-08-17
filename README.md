# super-guide

This repository was created to walk through the basics of production development.

## Repository structure

```
tasks/ - all tasks stored here
|-00-task/ - nn-task folder with task description and requirements
solutions/ - all solutions for tasks stored here
|-00-task/ - nn-task folder with task solution
README.md - this README
.gitignore - files that should be ignored by git
```

## Repository rules

1. No code should be pushed directly to `main` branch. Create new branch, do your task there, commit, push, and make the Pull Request (PR).
2. No code (except for examples) should be presented in folder tasks
3. All hand-written solutions must be stored under `solutions/` folder
4. Every PR must contain `description` with explanation what is done in this PR
5. Every task must match its solution, folder names must match each other
6. Every solution must be independents and contain it's own requirements.txt or pyproject.toml

## Workflow

1. Fetch updates on `main` branch using `git switch main` and `git pull`
2. Create new branch with `git switch -c <new-branch-name>`
3. Work inside the new branch and commit changes using `git commit -m "<your-commit-message-here>"`
4. After finishing work on some changes push it to the remote branch to save them using `git push origin <your-branch-name>`
5. After finishing work on some feature create Pull Request from the link in CLI or on github
6. Write a description, select correct reviewer and wait for review
7. If a reviewer left some comments resolve them by pushing new commits
8. Re-request review after resolving comments
9. Wait until reviewer will merge your branch into main

> That's not the final version of the README.md, check back for updates *WIP*
