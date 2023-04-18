```sql
CREATE DATABASE IF NOT EXISTS javbus DEFAULT CHARSET utf8mb4 ;
```

```
create table actors(
a_id int unsigned auto_increment PRIMARY KEY,
name varchar(32) not null
)

create table videos (
v_id int unsigned auto_increment PRIMARY KEY,
v_code varchar(15) not null,
a_id int unsigned not null,
name varchar(255) not null,
date datetime not null,
img_url varchar(255) not null,
FOREIGN KEY(a_id) REFERENCES actors(a_id)
)
```

