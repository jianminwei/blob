
### select all entries
select e.id, e.title, e.body, et.tag_id, t.name
from entry e
left outer join entry_tags et
on e.id = et.entry_id

left outer join tag t
on et.tag_id = t.id

order by e.id, t.name
