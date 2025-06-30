#!/bin/bash

echo "Installing Node.js WebSocket Service..."

cd node-service || exit
npm install

echo "Node service installed. Start it with: npm start"
