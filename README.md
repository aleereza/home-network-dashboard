# Home Network Data Engineering Dashboard

This project is a comprehensive demonstration of a modern data engineering workflow applied to a home network. By gathering network metrics from a variety of devices—ranging from routers and switches to access points and IoT gadgets—this pipeline transforms raw data into insightful visualizations. The primary goal is to highlight my data engineering skills, from data collection and orchestration to warehouse management, transformations, and finally dashboarding.

## Overview

The pipeline begins by periodically collecting network usage data via Python scripts, which interface with device APIs or network protocols. This raw data is then scheduled and managed through Apache Airflow, ensuring each step—from extraction to loading—is handled reliably with retries, logging, and error alerts. The data flows into Google BigQuery for scalable storage and querying. Using dbt, the raw data is further transformed and modeled into refined datasets ready for visualization. These polished datasets are then displayed through Looker, providing intuitive dashboards and interactive insights into device usage patterns, bandwidth consumption, and connectivity trends.

This project also incorporates a variety of best practices. Sensitive credentials are kept secure through secrets management. The codebase follows a modular architecture, making it easy to maintain and enhance. Logging is meticulously applied to ensure that issues can be diagnosed swiftly. Docker containers encapsulate each component for consistent and reproducible environments. Every stage of the pipeline is documented and version-controlled, allowing for transparent evolution and showcasing a professional, production-like setup.

## Tools & Their Roles

- **Python Scripts (Data Collection):** Custom code to query network devices and extract usage data.
- **Apache Airflow (Orchestration):** Manages the end-to-end workflow, scheduling data extractions, handling retries, and integrating alerts.
- **BigQuery (Data Warehousing):** Stores the incoming data in both staging and final schemas, offering powerful analytical capabilities at scale.
- **dbt (Data Transformation):** Transforms and tests the raw data into clean, analytics-ready models, ensuring data quality and consistency.
- **Looker (Visualization):** Presents the final datasets as intuitive dashboards, surfacing key insights and trends in an interactive environment.
- **Secrets Management:** Keeps credentials and API keys secure, preventing unauthorized access.
- **Docker:** Containerizes all components, ensuring consistent runtime environments and facilitating easy deployment.
- **Git:** Version-controls the entire codebase, enabling structured collaboration and a transparent change history.

## Project Structure

This repository is organized by functional domains to keep it clean, maintainable, and easy to navigate:

home-network-dashboard/
├─ airflow/
│ ├─ dags/ # Airflow DAGs orchestrating data extraction, loading, and transformation
│ ├─ plugins/ # Custom Airflow plugins or operators
│ └─ scripts/ # Auxiliary scripts triggered by Airflow tasks
├─ dbt/
│ ├─ models/ # dbt data models, building analytics-ready tables
│ ├─ seeds/ # Seed CSV files for reference or lookup data
│ └─ tests/ # Data tests ensuring model and data integrity
├─ docker/ # Docker-related configurations for containerizing the project components
├─ docs/ # Documentation, notes, and reference material
├─ infra/ # Infrastructure-as-code and environment configuration
├─ looker/ # Looker configuration and LookML files for visualization
├─ secrets/ # Sensitive information stored securely (not checked into version control)
└─ src/
  ├─ data_collection/ # Python scripts and modules to fetch data from network devices
  └─ data_transformation/ # Additional Python modules or logic for data processing


Each directory aligns with a distinct part of the workflow. Together, they form a cohesive, production-like data pipeline that showcases the full data engineering lifecycle in the context of a home network environment.
