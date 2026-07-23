# Enterprise Marble Manufacturing & Distribution Data Platform

**Project Specification (Living Document)**

> **Version:** 0.5
> **Status:**  Silver Layer in Progress (Phase 1)
> **Last Updated:** 2026-07-23

------------------------------------------------------------------------

# 1. Purpose

This project aims to build a flagship Data Engineering portfolio project
that resembles a real enterprise manufacturing environment rather than a
typical academic project.

The objective is to demonstrate modern ELT architecture, scalable data
engineering practices, and realistic ERP-style data modeling using
synthetic data.

This specification serves as the single source of truth for the
project's architecture, design decisions, business rules, and
implementation progress.

------------------------------------------------------------------------

# 2. Project Goals

-   Simulate multiple enterprise source systems.
-   Generate realistic synthetic business data.
-   Implement Bronze, Silver, and Gold layers.
-   Design analytical star schemas.
-   Build Power BI dashboards.
-   Keep the architecture modular and extensible.
-   Prioritize engineering quality over fake data complexity.

------------------------------------------------------------------------

# 3. Technology Stack

  Layer             Technology
  ----------------- --------------
  Data Generation   Python
  REST API          Express.js
  Processing        PySpark
  Bronze Storage    Parquet
  Silver Storage    Parquet
  Gold Layer        SQL Server
  Reporting         Power BI
  Version Control   Git & GitHub

------------------------------------------------------------------------

# 4. High-Level Architecture

``` text
CSV
JSON
REST API
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

------------------------------------------------------------------------

# 5. Project Structure

``` text
Marble-Data-Platform/
├── api/
├── data_generator/
├── docs/
│
├── source_data/
│   ├── procurement/
│   ├── inventory/
│   ├── production/
│   ├── sales/
│   ├── finance/
│   └── logistics/
│
├── pipeline/
│   ├── bronze/
│   │   ├── common/
│   │   └── procurement/
│   ├── silver/
│   └── gold/
│
├── lakehouse/
│   └── bronze/
└── .gitignore
```

------------------------------------------------------------------------
# Bronze Layer Architecture

CSV
JSON
REST API (Future)
        │
        ▼
Reusable Bronze Framework
        │
        ▼
Parquet

# Bronze Responsibilities
      -Read source systems.
      -Apply predefined Spark schemas.
      -Preserve source data.
      -Add ingestion metadata.
      -Write Parquet files.
      -No transformations.
      -No business validation.
      -No joins.
      -No aggregations.
------------------------------------------------------------------------
# 6. Development Philosophy

The following principles guide every design decision:

-   Schema before implementation.
-   Engineering over fake data perfection.
-   Only include columns with business value.
-   Use realistic enterprise business processes.
-   Complete one department before starting the next.
-   Design for scalability and maintainability.
-   Avoid redesigning schemas later.

------------------------------------------------------------------------

# 7. Business Calendar

  Property     Value
  ------------ ------------
  Start Date   2024-01-01
  End Date     2026-12-31

------------------------------------------------------------------------

# 8. Current Scope

The current implementation focuses exclusively on the **Procurement
Department**.

Future departments will include:

-   Inventory
-   Production
-   Sales
-   Finance
-   Logistics
-   Others as required

------------------------------------------------------------------------

# 9. Source Systems

  Department    Dataset                Source
  ------------- ---------------------- ----------
  Procurement   Suppliers              CSV
  Procurement   Materials              CSV
  Procurement   Purchase Orders        REST API
  Procurement   Purchase Order Lines   REST API
  Procurement   Goods Receipts         JSON
  Procurement   Goods Receipt Lines    JSON

------------------------------------------------------------------------

# 10. Procurement Operational Schemas

## Suppliers

  Column
  ---------------
  supplier_id
  supplier_code
  supplier_name
  city
  state
  supplier_type
  status

### Business Rules

-   200 records
-   Sequential IDs
-   Supplier codes use `SUP0001` format
-   90% Active
-   10% Inactive
-   85% Domestic
-   15% International
-   Unique company names

------------------------------------------------------------------------

## Materials

  Column
  -------------------
  material_id
  material_code
  material_name
  material_category
  unit_of_measure
  status

### Business Rules

-   500 records
-   Sequential IDs
-   Material codes use `MAT0001` format
-   95% Active
-   5% Inactive
-   Unique material names
-   Material price is **not** stored here

------------------------------------------------------------------------

## Purchase Orders

  Column
  ------------------------
  po_id
  po_number
  supplier_id
  order_date
  expected_delivery_date
  currency
  payment_term
  status

------------------------------------------------------------------------

## Purchase Order Lines

  Column
  ------------------
  po_line_id
  po_id
  material_id
  ordered_quantity
  unit_price

------------------------------------------------------------------------

## Goods Receipts

  Column
  --------------
  grn_id
  po_id
  warehouse_id
  receipt_date

------------------------------------------------------------------------

## Goods Receipt Lines

  Column
  -------------------
  grn_line_id
  grn_id
  po_line_id
  quantity_received

------------------------------------------------------------------------

# 11. Entity Relationships

``` text
Supplier
    │
    ▼
Purchase Order
    │
    ▼
Purchase Order Line
    │
    ▼
Goods Receipt Line
    ▲
    │
Goods Receipt

Material
    │
    └────────────► Purchase Order Line
```

------------------------------------------------------------------------

# 12. Data Volumes

  Dataset                  Approx. Rows
  ---------------------- --------------
  Suppliers                         200
  Materials                         500
  Purchase Orders               100,000
  Purchase Order Lines          400,000
  Goods Receipts                 80,000
  Goods Receipt Lines           320,000

------------------------------------------------------------------------

# 13. Coding Standards

-   snake_case naming
-   Integer surrogate keys
-   Prefix-based business codes
-   One generator per file
-   Centralized configuration in `config.py`
-   No UUIDs
-   Generated data is not committed to Git

------------------------------------------------------------------------

# 14. Runtime Configuration

`config.py` is responsible for:

-   Project paths
-   Data volumes
-   Business calendar
-   Random seed
-   Automatic folder creation

------------------------------------------------------------------------

# 15. Completed Components

## Infrastructure

-   Folder structure finalized
-   Runtime folder creation
-   `.gitignore`
-   `run_all.py`

## Core Modules

-   `config.py`
-   `master_data.py`
-   `utils.py`

## Data Generators

- `generate_suppliers.py`
- `generate_materials.py`
- `generate_purchase_orders.py`
- `generate_purchase_order_lines.py`
- `generate_goods_receipts.py`
- `generate_goods_recipts_lines.py`

------------------------------------------------------------------------

# 16. Current Progress

 Component                      | Status          
 ------------------------------ | --------------- 
 Architecture                   | ✅ Complete    
 Procurement Design             | ✅ Complete    
 Suppliers Generator            | ✅ Complete    
 Materials Generator            | ✅ Complete    
 Purchase Orders Generator      | ✅ Complete    
 Purchase Order Lines Generator | ✅ Complete    
 Goods Receipts Generator       | ✅ Complete        
 Goods Receipt Lines Generator  | ✅ Complete    
 Bronze Architecture	        | ✅ Complete
 Bronze Framework	        | ✅ Complete
 CSV Ingestion	                | ✅ Complete
 JSON Ingestion	                | ✅ Complete
 Procurement Bronze Pipeline	| ✅ Complete
 Procurement Completion         | Bronze Completed

------------------------------------------------------------------------

# 17. Design Decisions

## Accepted Decisions

------------------------------------------------------------------------

### Transaction Generation Order

Transactional tables are generated in business-process order.

Suppliers
→ Purchase Orders
→ Purchase Order Lines
→ Goods Receipts
→ Goods Receipt Lines

Each generator reads previously generated data instead 
of generating unrelated random foreign keys.

------------------------------------------------------------------------

### Goods Receipt Generation

A Goods Receipt is generated only for eligible Purchase Orders.

Business Rules:

- Closed Purchase Orders always receive a Goods Receipt.
- Approved Purchase Orders have a 50% chance of receiving a Goods Receipt.
- Open Purchase Orders do not receive a Goods Receipt.

------------------------------------------------------------------------

### One Goods Receipt Per Purchase Order

Version 1 of the project models a single Goods Receipt for each eligible Purchase Order.

Partial deliveries and multiple receipts are intentionally excluded to 
keep the procurement process simple while preserving realistic business relationships.

------------------------------------------------------------------------

### Warehouse Assignment

Warehouse IDs are assigned randomly from the available warehouse pool.

A dedicated Warehouse master table will be introduced during the Inventory module.

------------------------------------------------------------------------

### Material Price

Material prices are stored in **Purchase Order Lines**, not in
Materials, because prices vary over time and by supplier.

------------------------------------------------------------------------

### Load Reference Data Once

Reference datasets are loaded once before generation loops begin.

Generators operate on in-memory objects instead of repeatedly reading files from disk to improve performance.

------------------------------------------------------------------------

### Generated Data

Generated datasets are excluded from Git.

------------------------------------------------------------------------

### Folder Creation

Project folders are created automatically by `config.py`.

No `.gitkeep` files are used.

------------------------------------------------------------------------

### Logging

Development currently uses `print()`.

Python logging will replace print statements after the Procurement
module is complete.

------------------------------------------------------------------------

### Execution

The project is executed only through:

``` bash
python run_all.py
```

Individual generators are not intended to be run directly.

------------------------------------------------------------------------

### Bronze Layer

Bronze stores immutable source copies.

Bronze performs no business transformations.

Schema inference is disabled.

All Bronze datasets are stored as Parquet.

Metadata columns are added during ingestion.

Reusable ingestion framework is shared across all business domains.

Bronze output is organized by business domain.

Current write mode uses overwrite because Version 1 models full ERP snapshots.

Future versions will support append and incremental ingestion.

# Bronze Metadata

ingestion_timestamp

source_system

# Performance Optimizations

## Purchase Order Generation

Active suppliers are loaded into memory once before generation begins.

This reduced purchase order generation time from approximately 3 minutes to around 
10 seconds by eliminating repeated file reads and DataFrame sampling inside the 
generation loop.

# 18. Development Workflow

Business Requirements
        ↓
Schema Design
        ↓
Source System Generation
        ↓
Bronze Ingestion
        ↓
Silver Transformation
        ↓
Gold Modeling
        ↓
Power BI

------------------------------------------------------------------------

### Silver Layer

------------------------------------------------------------------------

pipeline/
└── silver/
    ├── common/
    │   ├── config.py
    │   ├── paths.py
    │   ├── contracts.py
    │   ├── reject_codes.py
    │   ├── validators.py
    │   ├── writer.py
    │   ├── metrics.py
    │   └── audit.py
    │
    └── procurement/
        ├── supplier_rules.py
        ├── material_rules.py
        ├── purchase_order_rules.py
        ├── purchase_order_line_rules.py
        ├── goods_receipt_rules.py
        ├── goods_receipt_line_rules.py
        │
        ├── transform_suppliers.py
        ├── transform_materials.py
        ├── transform_purchase_orders.py
        ├── transform_purchase_order_lines.py
        ├── transform_goods_receipts.py
        └── transform_goods_receipt_lines.py


------------------------------------------------------------------------


## Silver Architecture

Runner

↓

Read Bronze

↓

transform_xxx(df)

↓

(valid_df, reject_df, metrics)

↓

write_silver()

↓

write_rejects()

↓

write_audit()

## Silver Responsibilities

Responsibilities

Document each module's responsibility:

File	                           Responsibility
validators.py	                   Generic validation framework
contracts.py	                   Allowed business values
reject_codes.py	                   Standard reject reason constants
supplier_rules.py	           Supplier-specific business rules
transform_suppliers.py	           Orchestrates supplier transformation
writer.py	                   Writes Silver, Rejects, and Audit
metrics.py	                   PipelineMetrics data model
audit.py	                   Converts PipelineMetrics into audit records and writes them
run_procurement.py	           Coordinates the Procurement Silver pipeline



# 19. Future Plans

The following items are planned but not yet implemented:

## Procurement

Silver layer

## Data Pipeline

-   Silver Layer
-   Gold Layer

## Analytics

-   Star Schema
-   Power BI Dashboards

## Engineering Enhancements

-   Incremental Loads
-   CDC
-   SCD
-   Data Validation
-   Logging
-   Error Handling
-   Performance Optimization

## Additional Business Domains To Be Added

-   Inventory
-   Production
-   Sales
-   Finance
-   Logistics

------------------------------------------------------------------------

# 20. Maintenance

This document is intended to evolve with the project.

Whenever a major architectural decision is made, this specification
should be updated before implementation proceeds.
