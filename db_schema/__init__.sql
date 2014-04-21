DROP ROLE IF EXISTS pacific_master;

CREATE USER pacific_master WITH CREATEDB
                                REPLICATION
                                PASSWORD 'insecure_password';
