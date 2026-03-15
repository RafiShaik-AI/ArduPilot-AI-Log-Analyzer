# ArduPilot AI-Assisted Log Diagnosis_

## 📌 Project Overview
This repository serves as a technical proof-of-concept for the **AI-Assisted Log Diagnosis** project under ArduPilot for GSoC 2026. The goal is to bridge the gap between complex binary telemetry data and human-readable flight insights.

## 🚀 The Demo
The current script (`demo_analyzer.py`) demonstrates a core logic engine that:
1.  **Scans Telemetry Streams:** Monitors altitude, vibration levels, and system messages.
2.  **Identifies Anomalies:** Uses threshold-based logic to detect mechanical stress (Vibration) and sensor failures (EKF).
3.  **Generates Diagnosis:** Provides clear, actionable feedback for the pilot.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Environment:** GitHub Codespaces
* **Libraries:** `pymavlink` (in progress), `json`, `time`

## 📅 Development Roadmap
- [x] Initial Prototype (Mock Logic)
- [ ] Integration with `pymavlink` for `.tlog` parsing
- [ ] Classification model for "Crash vs. Pilot Error"
- [ ] CLI Tool for automated batch log processing

## 📊 Demo Execution
Below is the output of the `demo_analyzer.py` script running in GitHub Codespaces, successfully identifying flight anomalies:

![ArduPilot AI Diagnostic Output](assets/demo-output.png)

## 👨‍💻 Contributor
**Shaik Rafi** - 2nd Year AIML Student  
*Mentor: Nate Mailhot*
