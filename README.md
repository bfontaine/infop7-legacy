# infop7-legacy

This repository contains scripts I used to export data from a dump of [IP7][]’s
[old website](https://github.com/IP7/Website-old).

Most of the work involves setting up a local MySQL server; importing the dump
in it; translating the MySQL schema into [Peewee][]-style Python classes; then
exploiting the data.

[IP7]: https://github.com/IP7
[Peewee]: http://docs.peewee-orm.com/en/latest/

The files are now available online at <https://dump-infop7.bfontaine.net/>.

## Setup

### Install MySQL

```bash
brew install mysql@5.5
export PATH="/usr/local/opt/mysql@5.5/bin:$PATH"
```

Then follow Homebrew’s instructions for setting up a password for `root`.
Export that password somewhere:

```bash
export INFOP7_MYSQL_PASSWORD=...
```

You can throw away that database after the dump.

### Import the dump

```bash
mysql -uroot -p < the-dump.sql
```

### Python setup

```bash
pip3 install -r requirements.txt
```
