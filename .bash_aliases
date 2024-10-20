# Python Package Management
alias ins='python -m pip install'
alias unins='python -m pip uninstall'
alias up='python -m pip install --upgrade'
alias lsp='python -m pip list'
alias req='python -m pip freeze > requirements.txt'

# Django Project Management
alias mng='python manage.py'                     # Django manage file
alias r='python manage.py runserver'          # Start Django server
alias dsh='python manage.py shell'               # Open Django shell
alias mm='python manage.py makemigrations'       # Create new migrations
alias mg='python manage.py migrate'              # Apply migrations
alias dsc='python manage.py createsuperuser'     # Create a superuser
alias dcl='python manage.py collectstatic'       # Collect static files

# Testing
alias dtest='python manage.py test'              # Run tests
alias dtestc='python manage.py test --keepdb'    # Run tests without dropping DB

# Git Workflow
alias gs='git status'                            # Check Git status
alias ga='git add .'                             # Add all changes
alias gc='git commit -m'                        # Commit with a message
alias gp='git push'                            # Push changes
alias gpl='git pull'                             # Pull changes from repo
alias gco='git checkout'                         # Switch branches
alias gb='git branch'                            # List branches
alias gcb='git checkout -b'                      # Create and switch to a new branch

# Virtual Environment Management
alias venv='source venv/bin/activate'            # Activate virtual environment
alias deact='deactivate'                         # Deactivate virtual environment

# Docker Commands (if applicable)
alias dcu='docker-compose up'                    # Start Docker containers
alias dcd='docker-compose down'                  # Stop containers
alias dcb='docker-compose build'                 # Build Docker services
alias dclogs='docker-compose logs -f'            # Tail Docker logs

# PostgreSQL Commands
alias psql='psql -U postgres'                    # Open PostgreSQL shell
