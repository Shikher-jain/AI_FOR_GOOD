# AI-Assisted Home & Building Inspection — Problem Statement

## Problem & Goal

Home buyers and tenants often have little visibility into hidden issues in new or under-construction buildings—such as damp walls, exposed wiring, cracked beams, or poor finishing. Many of these risks show up in photos, videos, or inspection notes, but are not analysed systematically.

**Goal:**
Using a sample inspection dataset (e.g., tables of properties, rooms, findings, and a folder of labelled images like “crack”, “leak”, “ok”), design an AI-assisted inspection workspace that:

- Uses Snowflake Intelligence / AI SQL to classify or tag potential defects from text or image metadata
- Aggregates findings into a simple risk score per property or room
- Produces a plain-language inspection summary (e.g., “High risk: visible damp in 3/5 rooms, exposed wiring in kitchen”)

## Why This is AI for Good

This solution helps families and regulators spot unsafe or poor-quality housing earlier, improving residential infrastructure safety.

## Technology Requirements

- Use Snowflake (structured + optional unstructured data)
- Worksheets/SQL, Snowflake Cortex / AI SQL, Streamlit
- Optional: Dynamic Tables, Streams & Tasks for regular re-evaluation
