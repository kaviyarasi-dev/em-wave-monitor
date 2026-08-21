# EM Wave Monitoring System

A simple Python program that simulates electromagnetic (EM) wave levels
from electronic devices and suggests preventive actions when levels are
high — aimed at protecting animal and marine life near electronic
installations.

## Problem Statement

This program monitors EM wave levels and alerts when prevention is needed,
so that harmful exposure to wildlife (especially sensitive species near
coastal/marine areas) can be reduced.

## How It Works

- The program takes an EM wave level as input.
- If the level is within the safe limit (≤ 50 units), it reports the
  status as **Safe for animals**.
- If the level exceeds the safe limit, it flags the status as
  **DANGEROUS** and prints a list of preventive actions:
  - Reduce device power usage
  - Turn off unused electronic devices
  - Use EM shielding materials
  - Maintain distance from wildlife areas

## Sample Run

```
Enter electromagnetic wave level: 78
EM Wave Level: 78
Status: DANGEROUS
Prevention Actions:
- Reduce device power usage
- Turn off unused electronic devices
- Use EM shielding materials
- Maintain distance from wildlife areas
[Process completed]
```

## Tech Stack

- Python 3

## Future Improvements

- Log EM level readings over time and visualize trends
- Add multiple device types with different safe thresholds
- Build a simple dashboard (using Python + a charting library) to track
  readings across locations
