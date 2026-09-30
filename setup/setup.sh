#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

echo "Opdaterer pakkelister..."
sudo apt update

echo "Installerer nødvendige systempakker..."
sudo apt install -y git python3 python3-pip python3-venv

if [ ! -d ".venv" ]; then
    echo "Opretter virtuelt Python-miljø..."
    python3 -m venv .venv
else
    echo ".venv findes allerede."
fi

echo "Installerer Python dependencies..."
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo
echo "Setup færdigt."
echo "Aktivér miljøet med:"
echo "source .venv/bin/activate"