# hepta-application

Etapas para iniciar

```
git clone https://github.com/tomasrajao/hepta-application.git
cd hepta-application
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py

docker-compose up -d

python manage.py migrate
python manage.py createsuperuser --email="admin@admin.com"
python manage.py runserver 8000
```

Para criar Contato, inserir através do admin.
* Acessar localhost:8000 e logar com email e senha;
* Em "Contatos", clicar em "+ Adicionar".