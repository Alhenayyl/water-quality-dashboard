# water-quality-dashboard
Smart Water Quality Monitoring Dashboard for rural communities.
=====================================

Overview
--------
This dashboard displays water quality data (pH, Turbidity, Free Chlorine, TDS, Nitrate) for rural communities in Africa and Asia. It shows trends, summaries (Min, Max, Average), and safety status based on SANS 241:2015 standards (e.g., pH 5.0–9.5 is safe). Built by Yeung Yin Ling for The Chemistry Solutions Company.

Requirements
------------
- Web browser (Chrome, Firefox, or Safari)
- Internet (for online access or CDNs)
- Optional: Local server (e.g., VS Code Live Server) for CSV data

How to Run
----------
1. **Online**:
   - Open https://yourusername.github.io/water-quality-dashboard/dashboard_final.html in a browser.
   - Uses built-in sample data (5 days).

2. **Local**:
   - Save `dashboard_final.html` to your computer.
   - Use a local server to avoid errors:
     - **VS Code**: Install Live Server extension, open file, click "Go Live".
     - **Python**: Run `python -m http.server 8000` in the folder, then open http://localhost:8000/dashboard_final.html.

Usage
-----
1. **Select Parameters**: Use the dropdown ("Select Parameters to Display") to choose parameters (e.g., pH, Turbidity). Hold Ctrl (or Cmd on Mac) to select multiple.
2. **View Insights**: Check the "Data Insights" section for Min, Max, Average, and Status (Good in green, Warning in red).
3. **View Charts**: Line graphs show trends over time. Hover (or tap) for exact values.

Troubleshooting
---------------
- **No data**: Ensure CSV is in the folder if not using sample data.

Note: This is a prototype with simulated data. For real sensors, contact the project team.
