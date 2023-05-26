# Django + Flowbite + Tailwindcss

## Running In Development


- create your project folder to clone into

``` sh
mkdir <project_folder>
git clone <url> <project_folder>
```

- create virtual environment

``` sh
python -m venv .venv
source .venv/bin/activate
```

- install requirements

``` sh
pip install -r requirements.txt
```

- install tailwindcss & flowbite

``` sh
npm install -D tailwindcss
npm install flowbite
```

- Generate css files

``` sh
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

- Run server

```sh
python manage.py runserver
```
