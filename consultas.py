reporteOhMembers = """
SELECT subquery.id, subquery.cicle, subquery.student, subquery."group",   subquery.semana1, subquery.semana2, subquery.semana3, subquery.semana4, subquery.semana5, subquery.semana6, subquery.semana7, subquery.semana8, subquery.semana9, subquery.semana10,
subquery.semana11, subquery.semana12, subquery.semana13, subquery.semana14, subquery.semana15, subquery.semana16, subquery.semana17,
subquery.semana18,
COALESCE(sum(registros.duration), 0) as cantidad
FROM (
  SELECT *,
         COALESCE(SUM(CASE WHEN registros.oh_week = 1 THEN registros.duration END), 0) as semana1,
         COALESCE(SUM(CASE WHEN registros.oh_week = 2 THEN registros.duration END), 0) as semana2,
         COALESCE(SUM(CASE WHEN registros.oh_week = 3 THEN registros.duration END), 0) as semana3,
         COALESCE(SUM(CASE WHEN registros.oh_week = 4 THEN registros.duration END), 0) as semana4,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 5 THEN registros.duration END), 0) as semana5,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 6 THEN registros.duration END), 0) as semana6,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 7 THEN registros.duration END), 0) as semana7,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 8 THEN registros.duration END), 0) as semana8,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 9 THEN registros.duration END), 0) as semana9,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 10 THEN registros.duration END), 0) as semana10,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 11 THEN registros.duration END), 0) as semana11,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 12 THEN registros.duration END), 0) as semana12,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 13 THEN registros.duration END), 0) as semana13,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 14 THEN registros.duration END), 0) as semana14,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 15 THEN registros.duration END), 0) as semana15,
         COALESCE(SUM(CASE WHEN registros.oh_week = 16 THEN registros.duration END), 0) as semana16,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 17 THEN registros.duration END), 0) as semana17,
    	   COALESCE(SUM(CASE WHEN registros.oh_week = 18 THEN registros.duration END), 0) as semana18


  FROM estudiantes
  LEFT JOIN registros ON estudiantes.student = registros.student_name
  GROUP BY estudiantes.student
) as subquery
LEFT JOIN registros ON subquery.student = registros.student_name AND registros.cicle = "Y23C1"
GROUP BY subquery.student
ORDER BY subquery."group";
"""