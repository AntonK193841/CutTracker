# CutTracker

CutTracker — веб-приложение для учета и расчета раскроя листового металла.

Система предназначена для инженеров судостроительного цеха и позволяет:

- учитывать металлические листы на складе;
- загружать спецификации деталей;
- рассчитывать раскрой;
- минимизировать отходы;
- сохранять результаты расчетов.

## Стек

### Backend

- Python
- FastAPI

### Frontend

- React
- TypeScript

### Database

- PostgreSQL

### Infrastructure

- Docker
- Docker Compose

## Project structure

```text
backend/     — REST API
frontend/    — web interface
importer/    — Excel/CSV importer
tests/       — tests
data/        — test data