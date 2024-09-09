CREATE TABLE IF NOT EXISTS public.sensor_readings (
    id SERIAL PRIMARY KEY,
    equipment_id VARCHAR(8) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    reading_value NUMERIC(10,2) NOT NULL
);

INSERT INTO public.sensor_readings (equipment_id, timestamp, reading_value) VALUES
    ('EQ-12345', CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo', 78.42),
    ('AB-99999', '2024-09-10T01:30:00.000-03:00', 65.89),
    ('VG-04510', CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo', 1234.12),
    ('AB-99999', '2024-08-10T01:30:00.000-03:00', 64.77);