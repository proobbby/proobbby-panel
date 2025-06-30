#!/bin/bash

echo "Installing Proobbby Panel backend..."

cd backend || exit

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

echo "Backend installed. Please edit .env before running."
