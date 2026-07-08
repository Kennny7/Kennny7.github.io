---
title: "PostgreSQL Function Performance Monitor"
order: 99
description: "Modular monitoring system for PostgreSQL that safely executes functions in transactions, detects performance bottlenecks, and generates automated reports with email alerts."
image: "/images/projects/postgres-monitor.png"
github: "https://github.com/Kennny7/PostgreSQL-Function-Performance-Monitor"
tags: ["PostgreSQL", "Python", "Monitoring", "Automation", "Email"]
featured: true
fetchGithubData: true
---

## Overview

Built a modular monitoring system that analyzes PostgreSQL functions, procedures, and views for performance issues without modifying database state.

### Key Features
- **Safe transactional execution** ensures all tests run with rollback and no data modification
- **Performance anomaly detection** identifies long-running functions with automatic timeout handling
- **Parallel monitoring engine** enables efficient testing with controlled database load
- **Automated reporting pipeline** generates CSV, Excel, and HTML reports with detailed metrics
- **Integrated alerting system** sends email notifications with attachments and system insights