#!/bin/bash

echo "🔧 Installing Proobbby Panel backend..."

cd backend || exit

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

if [ -f ".env.example" ]; then
    cp .env.example .env
    echo "✅ .env file created from example."
else
    echo "⚠️  .env.example file not found. Please create it manually."
fi

echo "✅ Backend installed."
echo "⚡ Start it with: source venv/bin/activate && uvicorn app.main:app --reload"
