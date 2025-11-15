-- Script SQL para crear la base de datos y tabla en PostgreSQL
-- Ejecutar como usuario postgres o con permisos de creación de base de datos

-- Crear base de datos (ejecutar como superusuario)
-- CREATE DATABASE portfolio_consultas;

-- Conectar a la base de datos portfolio_consultas
-- \c portfolio_consultas;

-- Crear tabla de consultas
CREATE TABLE IF NOT EXISTS consultas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    empresa VARCHAR(255),
    mensaje TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear índice para búsquedas por email
CREATE INDEX IF NOT EXISTS idx_consultas_email ON consultas(email);

-- Crear índice para búsquedas por fecha
CREATE INDEX IF NOT EXISTS idx_consultas_fecha ON consultas(fecha_creacion);

-- Verificar que la tabla se creó correctamente
SELECT * FROM consultas LIMIT 1;

