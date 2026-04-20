# Task Tracker (Python Console + SQL)

Simple task tracker with SQL database and console (UI) in (CLI)

---

### PROJECT STRUCTURE

- Structure based on **clean code architecture**
    - (services) as complete logic and (repositories) only for getting data from datbases
    - (config.py) for database authorization (not added to github!), (database) for mysql connection

```bash
app/
├── schema.sql # SQL query to create databases
├── config.py # SQL configuration dictionary / Added to .gitignore!
├── main.py
└── app/
    ├── models/
    │   └── models.py # @dataclasses
    ├── core/
    │   └── database.py
    ├── utils/
    │   └── helpers.py
    ├── repositories/
    │   ├── user_repository.py
    │   ├── task_repository.py
    ├── services/
    │   ├── auth_service.py
    │   └── task_service.py
    └── cli/
        ├── auth_cli.py
        └── main_cli.py
```
