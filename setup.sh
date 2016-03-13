#!/usr/bin/env sh

VENV_DIR=./venv
PYTHON_EXE=python3

if (! command -v $PYTHON_EXE > /dev/null 2>&1); then
  echo "Please install $PYTHON_EXE before running $0"
  exit 1
fi

if (! command -v virtualenv > /dev/null 2>&1); then
  echo "Please install virtualenv before running $0"
  exit 1
fi

if [ ! -d $VENV_DIR ]; then
  echo "Setting up virtualenv directory in $VENV_DIR..."
  virtualenv $VENV_DIR -p $PYTHON_EXE
fi

echo "Activating virtualenv..."
source $VENV_DIR/bin/activate
