# Initial Data Model

## Purpose

This document defines the initial relational model for LeaveFlow before the
database implementation begins.

## Entity Relationship Diagram

```mermaid
erDiagram
    USERS ||--o{ TEAM_MEMBERSHIPS : has
    TEAMS ||--o{ TEAM_MEMBERSHIPS : has
    USERS ||--o{ LEAVE_REQUESTS : submits
    USERS ||--o{ LEAVE_REQUESTS : reviews
    LEAVE_REQUESTS ||--o{ LEAVE_REQUEST_EVENTS : records
    USERS ||--o{ LEAVE_REQUEST_EVENTS : performs