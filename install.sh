
---

# 2. install.sh

```bash
#!/bin/bash

echo "Installing Proobbby Panel Backend and Frontend..."

cd backend || exit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

echo "Backend setup done."

cd ../frontend || exit
npm install

echo "Frontend setup done."

echo "Please configure your .env file before running."
