-- Write your query below
with score_cte as(
    select *,
    row_number() over(partition by student_id order by score DESC, exam_id) as rnk
    from exam_results
    order by student_id, score DESC, exam_id
)
select student_id, exam_id, score
from score_cte
where rnk = 1


