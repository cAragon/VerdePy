#!/bin/bash

#VERIFICA CONEXAO DO DISPOSITIVO

wget -q --spider https://google.com

if [ $? -eq 0 ]; Then
  echo "online"
  echo "      "
  #VERIFICA ARQUIVOS DE SISTEMA
else
  echo "offline"
fi
