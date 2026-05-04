#!/bin/bash

CONTAINER="pgsqlapi"
DB_USER="postgres"
DB_NAME="indices"
BACKUP_DIR="/home/rangel/revise/backup-api-db"

mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +"%d-%m-%Y_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql"

echo "============================================================================================"
echo "Iniciando backup do banco: $DB_NAME"
echo "Container: $CONTAINER"
echo "Data/Hora: $(date +"%d/%m/%Y %H:%M:%S")"
echo "Destino: $BACKUP_FILE"
echo "============================================================================================"

docker exec -t $CONTAINER pg_dump -U $DB_USER $DB_NAME > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "--------------------------------------------------------------------------------------------"
    echo "Backup do banco '$DB_NAME' realizado com sucesso!"
    echo "Arquivo gerado: $BACKUP_FILE"
    echo "--------------------------------------------------------------------------------------------"
else
    echo "--------------------------------------------------------------------------------------------"
    echo "ERRO ao realizar backup do banco '$DB_NAME'!"
    echo "Verifique o container, credenciais e permissões."
    echo "--------------------------------------------------------------------------------------------"
fi


