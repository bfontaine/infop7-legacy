# infop7-legacy

This repository contains scripts I used to export data from a dump of [IP7][]’s
[old website](https://github.com/IP7/Website-old).

It mostly involves setting up a local MySQL server; importing the dump in it;
and translating the MySQL schema into [Peewee][]-style Python classes.

[IP7]: https://github.com/IP7
[Peewee]: http://docs.peewee-orm.com/en/latest/

## Setup

### Install MySQL

```
brew install mysql@5.5
export PATH="/usr/local/opt/mysql@5.5/bin:$PATH"
```

Then follow Homebrew’s instructions for setting up a password for `root`.
Export that password somewhere:

```
export INFOP7_MYSQL_PASSWORD=...
```

### Import the dump

```
mysql -uroot -p < the-dump.sql
```

### Python setup

```
pip3 install -r requirements.txt
```
