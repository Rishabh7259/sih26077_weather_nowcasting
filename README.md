# ⚡ MoES AI-Driven Hyper-Local Early Warning System for Severe Weather Nowcasting
**Smart India Hackathon 2026 | Problem Statement: SIH26077**  
**Ministry of Earth Sciences (MoES) / Indian Meteorological Department (IMD)**

---

## 🚀 Overview
The **MoES AI-Driven Hyper-Local Weather Nowcasting System** is an advanced, production-grade automated disaster warning and risk assessment prototype built for **Smart India Hackathon 2026 (SIH26077)**. 

Traditional weather forecasting operates on regional or macro scales (district-wide or state-wide). This system bridges the gap by providing **2–6 hour hyper-local lead-time severe weather predictions** (Thunderstorms, Cloudbursts, and Flash Floods) integrated with automated emergency dispatch protocols and Explainable AI (XAI) diagnostics.

---

## 🏗️ Core System Architecture

```text
sih26077_weather_nowcasting/
│
├── api/
│   ├── main.py                  # FastAPI Backend & Multi-Region Dynamic Nowcasting Engine
│   └── alert_dispatcher.py      # Automated Emergency SMS & District Authority Dispatcher
│
├── app.py                       # Interactive Streamlit Frontend Dashboard
├── requirements.txt             # Project Dependencies
└── README.md                    # Project Documentation
