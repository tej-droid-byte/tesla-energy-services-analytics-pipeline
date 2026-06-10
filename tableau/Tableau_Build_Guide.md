# Tableau Build Guide

Connect Tableau Public/Desktop to:

tableau/tesla_energy_services_dashboard_data.csv

Recommended dashboard title:
Energy Services Operations Dashboard

Recommended sheets:
1. Ticket Volume by Region
   - Columns: region
   - Rows: SUM(ticket_volume)

2. SLA Breach Rate by Region
   - Columns: region
   - Rows: AVG(sla_breach_rate_pct)

3. Average Resolution Time by Issue Type
   - Columns: issue_type
   - Rows: AVG(avg_resolution_hours)

4. Monthly Service Ticket Trend
   - Columns: service_month
   - Rows: SUM(ticket_volume)

5. Resolution Rate by Issue Type
   - Columns: issue_type
   - Rows: AVG(resolution_rate_pct)

6. Cost by Region
   - Columns: region
   - Rows: AVG(avg_service_cost_usd)

Filters:
- service_month
- region
- issue_type
