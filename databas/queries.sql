select teamID
from specin
join team
on specin.teamID = team.teamID
where issue = {}




select * from patient
join inqueue
on inqueue.patid = patient.pnum
where teamid = %s
order by teamid, prio;
