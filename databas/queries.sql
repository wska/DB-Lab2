select teamID
from specin
join team
on specin.teamID = team.teamID
where issue = {}
