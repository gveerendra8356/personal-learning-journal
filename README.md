# Personal Learning Journal

## Project description
A personal project for recording Python practice, Git commands, and daily learning goals.

## Goals
- Practice Python with small examples.
- Track changes with clear Git commits and meaningful commit messages.
- Keep learning notes organized.

## Version control workflow
Clone the repository, edit README.md locally, inspect git diff, stage with git add, commit with a meaningful message, and push to main.

## Collaboration update
Pull the latest main branch before starting a new learning task.

## Login exercise
`login.py` contains `login(username, password, users)`, which returns a Boolean after comparing a derived password hash with a stored hash. `users` maps a username to `(salt, hash)`; generate a unique random salt for each real record. This in-memory example has no sessions, persistence, or rate limiting.

Run the four tests with `python -B -m unittest -v`. Test credentials are fictional fixtures.
