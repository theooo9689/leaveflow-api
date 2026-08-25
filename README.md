# LeaveFlow

LeaveFlow is a REST API for managing employee leave requests and approval workflows in small teams.

## Project Status

Under active development.

## Current Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- uv
- Ruff

## Available Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/health` | Checks whether the application is running. |
| GET | `/api/v1/system/info` | Returns public API information. |

## Architecture

LeaveFlow is being developed as a modular monolith with versioned API routes.

For detailed architecture decisions and the current request flow, see
[Architecture](docs/architecture.md).

## Getting Started

### Requirements

- Python 3.12
- uv

### Run Locally

```bash
uv sync
uv run fastapi dev app/main.py