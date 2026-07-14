# Enterprise Marble Manufacturing & Distribution Data Platform

A flagship Data Engineering portfolio project that simulates a realistic enterprise ERP system and modern ELT architecture using synthetic business data.

The goal of this project is to demonstrate production-oriented Data Engineering practices rather than simply building an ETL pipeline.

---

# Architecture

```text
CSV
JSON
REST API (Planned)
        │
        ▼
PySpark Bronze
        │
        ▼
PySpark Silver
        │
        ▼
SQL Server Gold
        │
        ▼
Power BI
```

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Data Generation | Python |
| Source Systems | CSV, JSON, REST API |
| Processing | PySpark |
| Bronze Storage | Parquet |
| Silver Storage | Parquet |
| Gold Layer | SQL Server |
| Reporting | Power BI |
| Version Control | Git & GitHub |

---

# Project Structure

```text
Marble-Data-Platform/

├── api/
├── data_generator/
├── docs/
├── source_data/
├── pipeline/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── lakehouse/
├── sql/
├── powerbi/
└── .gitignore
```

---

# Current Business Domain

The project currently models the **Procurement Department**.

Implemented datasets:

- Suppliers
- Materials
- Purchase Orders
- Purchase Order Lines
- Goods Receipts
- Goods Receipt Lines

---

# Bronze Layer

Implemented features:

- Generic ingestion framework
- Centralized Spark schemas
- CSV ingestion
- JSON ingestion
- Metadata enrichment
- Parquet storage
- Domain-based folder structure
- Reusable ingestion architecture

Bronze responsibilities:

- Read source data
- Apply predefined schemas
- Preserve source values
- Add ingestion metadata
- Store immutable Parquet datasets

No business transformations are performed in Bronze.

---

# Project Principles

- Engineering over fake data complexity
- Schema-first development
- Business process before implementation
- Modular and reusable architecture
- Domain-driven project organization
- Scalable design for future expansion

---

# Roadmap

## Completed

- Procurement source system
- Synthetic ERP data generators
- Relationship verification
- Bronze architecture
- Bronze ingestion framework

## In Progress

- Silver Layer

## Planned

- Gold Layer
- Star Schema
- Power BI dashboards
- REST API ingestion
- Incremental Loads
- Change Data Capture (CDC)
- Slowly Changing Dimensions (SCD)
- Orchestration
- Data Quality Framework

---

# Repository Status

This project is under active development and continuously evolves as new enterprise data engineering concepts are implemented.

The objective is to progressively build a production-inspired data platform rather than a one-time ETL project.