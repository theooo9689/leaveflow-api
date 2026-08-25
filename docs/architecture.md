# Architecture

## Overview

LeaveFlow is a modular monolith built with FastAPI.

The application starts as a single deployable service with clearly separated
responsibilities. This keeps the project simple to develop and deploy while
allowing its modules to grow independently.

## Current Request Flow

```mermaid
flowchart LR
    Client --> App["FastAPI application<br/>app/main.py"]
    App --> Router["Versioned router<br/>app/api/v1/router.py"]
    Router --> Endpoint["Endpoint module<br/>app/api/v1/system.py"]
    Endpoint --> Settings["Configuration<br/>app/core/config.py"]