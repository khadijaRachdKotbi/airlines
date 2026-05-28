-- 00_overview_tables.sql
-- Vue d'ensemble des tables et volumes

SELECT
    t.name as table_name,
    SUM(p.rows) as row_count
FROM sys.tables t
INNER JOIN sys.partitions p ON t.object_id = p.object_id
WHERE p.index_id IN (0, 1)
GROUP BY t.name
ORDER BY row_count DESC;