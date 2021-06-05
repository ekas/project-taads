# project-taads

Project repo for Taads &amp; HMI

## Frontend

[] yarn install
[] yarn run dev

## Backend

[] cd backend
[] python3 -m venv venv/
[] pip3 install -r requirements.txt
[] python3 main.py
[] docker build -t taads .
[] docker run -d --name taads-container -p 3000:3000 taads
[] http://localhost:3000/docs
