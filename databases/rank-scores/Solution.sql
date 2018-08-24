/**
 * Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking.
 * Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.
 *
 * +----+-------+
 * | Id | Score |
 * +----+-------+
 * | 1  | 3.50  |
 * | 2  | 3.65  |
 * | 3  | 4.00  |
 * | 4  | 3.85  |
 * | 5  | 4.00  |
 * | 6  | 3.65  |
 * +----+-------+
 * For example, given the above Scores table, your query should generate the following report (order by highest score):
 *
 * +-------+------+
 * | Score | Rank |
 * +-------+------+
 * | 4.00  | 1    |
 * | 4.00  | 1    |
 * | 3.85  | 2    |
 * | 3.65  | 3    |
 * | 3.65  | 3    |
 * | 3.50  | 4    |
 * +-------+------+
 */

select s0.Score, case when number is null then 1 else number end as Rank from Scores as s0
left join
(select id1, count(distinct score2) + 1 as number from (
    select s1.score as score1, s2.score as score2, s1.Id as id1 from Scores as s1 cross join Scores as s2
    where s1.score < s2.score
) as joined_scores group by id1) as tmp
on s0.id = tmp.id1 order by s0.Score desc;
