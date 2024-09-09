#!/bin/bash
set -e

export PGPASSWORD="$POSTGRES_PASSWORD"

until psql -h db -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

psql -h db -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS public.sensor_readings (
        id SERIAL PRIMARY KEY,
        equipment_id VARCHAR(8) NOT NULL,
        timestamp TIMESTAMPTZ NOT NULL,
        reading_value NUMERIC(10,2) NOT NULL
    );
    
    TRUNCATE TABLE public.sensor_readings;

    INSERT INTO public.sensor_readings (equipment_id, timestamp, reading_value) VALUES
        ('EQ-12345', CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo', 78.42),
        ('AB-99999', '2024-09-09T01:30:00.000-03:00', 65.89),
        ('VG-04510', CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo', 1234.12),
        ('AB-99999', '2024-09-07T01:30:00.000-03:00', 1700.12),
        ('VG-04510', '2024-09-02T01:30:00.000-03:00', 75.24),
        ('AB-99999', '2024-08-04T01:30:00.000-03:00', 98.03),
        ('EQ-12345', '2024-08-27T01:30:00.000-03:00', 120.01),
        ('TG-66666', '2024-08-20T01:30:00.000-03:00', 59.31),
        ('GT-19992', '2024-08-20T01:30:00.000-03:00', 1620.29);
EOSQL
