# MusicBot back-end
Start date: `12.11.2023`

## Getting Started

Setup project environment with venv and [pip](https://pip.pypa.io).

For Mac:
```bash
 python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py runserver
```
For others:
```bash
 python -m venv venv
```


```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
## Test

```bash
$ python manage.py test && flake8
```
