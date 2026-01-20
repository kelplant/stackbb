#!/bin/sh
set -e

if [ -n "$DB_HOST" ]; then
  echo "Waiting for MSSQL at $DB_HOST:$DB_PORT..."
  for i in $(seq 1 60); do
    if nc -z "$DB_HOST" "$DB_PORT"; then
      echo "MSSQL is available."
      break
    fi
    sleep 2
  done
fi

exec "$@"
