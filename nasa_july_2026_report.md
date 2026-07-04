# NASA NeoWS Data Analytics Report

**Date of Analysis:** July 5, 2026
**Data Source:** NASA Near Earth Object Web Service (NeoWS) API
**Project:** Orbit & Order Technical Portfolio

## Current Near-Earth Objects (NEOs) Summary
This automated report displays the data parsed by our Python script (`main.py`) evaluating potential cosmic hazards passing close to Earth today.

| Object Name | Estimated Diameter (m) | Relative Velocity (km/h) | Status |
| :--- | :---: | :---: | :---: |
| **Asteroid 2026 AM4** | 120m | 72,400 km/h | ✅ Safe |
| **Asteroid 2011 SF22** | 340m | 43,150 km/h | ⚠️ Potentially Hazardous |
| **Asteroid 2026 NL1** | 45m | 95,800 km/h | ✅ Safe |

## Technical Insights
* **Hazard Detection:** Object **2011 SF22** has been flagged by the system because its diameter exceeds 140 meters and its trajectory falls within the proximity parameters established by international planetary defense groups.
* **Velocity Metrics:** The average velocity of tracked objects for today is **70,450 km/h**.

---
*Developed by Sofiya as part of the IT and Space Governance academic track.*
