DROP TABLE IF EXISTS service_kpi_summary;

CREATE TABLE service_kpi_summary AS
SELECT
    service_month,
    region,
    issue_type,
    COUNT(*) AS ticket_volume,
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours,
    ROUND(AVG(service_cost_usd), 2) AS avg_service_cost_usd,
    ROUND(100.0 * SUM(is_resolved) / COUNT(*), 2) AS resolution_rate_pct,
    ROUND(100.0 * SUM(sla_breach_flag) / COUNT(*), 2) AS sla_breach_rate_pct,
    ROUND(AVG(customer_rating), 2) AS avg_customer_rating
FROM service_tickets_clean
GROUP BY service_month, region, issue_type;

DROP TABLE IF EXISTS technician_performance;

CREATE TABLE technician_performance AS
SELECT
    technician_id,
    COUNT(*) AS tickets_handled,
    ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours,
    ROUND(SUM(service_cost_usd), 2) AS total_service_cost_usd,
    ROUND(100.0 * SUM(is_resolved) / COUNT(*), 2) AS resolution_rate_pct,
    ROUND(AVG(customer_rating), 2) AS avg_customer_rating
FROM service_tickets_clean
GROUP BY technician_id
HAVING COUNT(*) >= 10;
