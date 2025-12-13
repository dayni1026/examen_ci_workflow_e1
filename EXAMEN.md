# Examen: GitHub Actions CI/CD

**Puntuación: 20 puntos | Tiempo: 90 minutos**

## Objetivo

Implementar workflows de CI/CD usando GitHub Actions para automatizar testing y deployment de una API en Python.

---

## Preparación

1. Fork este repositorio
2. Clona tu fork localmente
3. Crea branch `examen-workflows`
4. Crea archivo `.env` basándote en `.env.example`

---

## Parte 1: CI Workflow (10 puntos)

**Archivo:** `.github/workflows/ci.yml`

**Trigger:** Pull Requests hacia `main`

**Requisitos:**
- Python 3.11
- Instalar dependencias de `requirements.txt`
- Ejecutar tests con pytest
- Configurar variables de entorno necesarias

**Evaluación:**
- Trigger correcto (2 pts)
- Setup Python (2 pts)
- Instalación dependencias (2 pts)
- Ejecución tests (3 pts)
- Variables de entorno (1 pt)

---

## Parte 2: CD Workflow (10 puntos)

**Archivo:** `.github/workflows/deploy.yml`

**Trigger:** Tags que inicien con `v*` (ej: `v1.0.0`)

**Requisitos:**
- Deploy a plataforma cloud (Render/Railway/Vercel)
- Usar GitHub Secrets para credenciales
- Configurar variables de entorno de producción

**Evaluación:**
- Trigger tags correcto (2 pts)
- Configuración deployment (4 pts)
- GitHub Secrets (2 pts)
- Variables de entorno (1 pt)
- Compartir URL del sitio deplorado y una captura de un API funcionando (1 pt)

---

## Secrets Requeridos

Configura en GitHub (Settings → Secrets):
- `SECRET_KEY` - Clave secreta de Flask
- Credenciales de tu plataforma de deployment

---

## Entrega

1. Push a branch `examen-workflows`
2. Crea PR hacia `main`
3. Verifica que CI ejecute correctamente
4. Crea tag `v1.0.0`
5. Verifica deployment exitoso
6. Comparte enlace del repositorio

---

## Notas

- Workflows en `.github/workflows/`
- Los tests DEBEN pasar antes de aprobar
- Consulta GitHub Actions Marketplace si necesitas
- Variables de entorno son críticas para el funcionamiento
