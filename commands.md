# Terminal Record: Cloudstep Software

## 1. Building the project
cd ~
mkdir ism3232-midterm && cd ism3232-midterm
python3 -m venv .venv && source .venv/bin/activate
pip install pytest ruff && pip freeze > requirements.txt
echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
touch business_rules.py main.py command.md README.md
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
mv command.md commands.md
echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
git init && git add . && git status
git commit -m "Part 1: Set up project structure"
git remote add origin https://github.com/EileneRios/ism3232-midterm.git
git branch -M main && git push -u origin main
