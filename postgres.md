### PostgreSQL on Ubuntu

:warning: I would rather recommand to install PostgreSQL inside [docker](https://gist.github.com/ankurk91/aeda6722ca7b2205c4aca28b2429a0ab#file-docker-compose-yml).

#### Add PPA [Source](https://www.postgresql.org/download/linux/ubuntu/)
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update

# Install the latest version
sudo apt-get -y install postgresql
```

**Start/stop postgresql service**
```
sudo service postgresql start
sudo service postgresql stop
sudo service postgresql restart
```

**Access psql prompt**
* Notice: we are accessing `psql` using a special user
```
sudo -u postgres psql
```
* Type `\q` and enter to exit prompt.
* Remember: `psql` is equivalent to `mysql`

**Create a new postgres user**
* By default postgres comes with a special user named `postgres` but we will not be using this for our web apps.
* This user is to perform administration only. So lets create a new user with the help of this super user.
* Notice that `postgres` is a linux user.
```
sudo -u postgres createuser --interactive --pwprompt
```
Answer the questions asked.

## Create a new database
```
sudo -u postgres createdb --owner=user_name db_name_goes_here
```
If you dont have the `user_name` as a linux user in your machine then you need to add, otherwise you will get `unable to initialize policy plugin` error on terminal. This is called `Ident authentication` in postgres.
```
# create missing linux user
sudo adduser user_name
```
You can omit `--owner=user_name` parameter if db_name is same as user_name.

**Login to psql propmt via super user**
* Lets you perform adminstrative commands on this database.
* You would rarely login with `postgres` user.
```
sudo -u postgres psql -d db_name_goes_here
```
**Login to psql prompt via this user**
```
sudo -u user_name psql db_name_goes_here
```


## Connect to database
```
Host: 127.0.0.1
Post: 5432
User: user_name_you_created_above
Password: this_should_be_the_postgres_user_password
Database: db_name_you_just_created
```

## Delete database
```
sudo -u postgres dropdb db_name
```

## Delete user
```
sudo -u postgres dropuser user_name
```

## Import/export database
```
# export
pg_dump -U user_name db_name > dbexport.pgsql
# import 
pg_dump -U user_name db_name < dbexport.pgsql
```
## Run SQL query from terminal
```
sudo su linux_user_name_that_owns_the_database
psql -U user_name -d database_name -W
```
Now you can run your queries like:
```
select * from users;
```

## Install [PostGIS](https://postgis.net/) extension
```
#sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
#sudo apt update
sudo apt install postgis
```
Now enable the extension on this database
```
sudo -u postgres psql -d db_name_goes_here
CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;
\q
```
**Eject extension from specific database**
```
DROP EXTENSION postgis;
```

**Resources**
* https://www.linode.com/docs/databases/postgresql/how-to-install-postgresql-on-ubuntu-16-04/
* https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
* https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps
* https://dev.to/jkostolansky/how-to-upgrade-postgresql-from-11-to-12-2la6