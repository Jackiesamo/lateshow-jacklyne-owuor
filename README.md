# Late Show API

A Flask REST API for managing Late Show episodes, guests, and appearances.

---

## Models
- Episode
- Guest
- Appearance

---

## Relationships
- An Episode has many Guests through Appearances
- A Guest has many Episodes through Appearances

---

## Validations
- Appearance rating must be between **1 and 5**

---

## Routes

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | /episodes | List all episodes |
| GET | /episodes/<id> | Get episode details with appearances |
| GET | /guests | List all guests |
| POST | /appearances | Create a new appearance |

---

## Setup Instructions

### 1. Install dependencies
```bash
pipenv install
pipenv shell

##Run database migrations
.flask db upgrade

##Seed the database
python3 seed.py

##Start the server
python3 app.py

##The API will be available at:
http://127.0.0.1:5000


MIT License

Copyright (c) 2026 Jacklyne Owuor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.