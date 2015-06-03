from jobman.tools import DD, flatten
from jobman import api0, sql
import multiprocessing
import os
import numpy as np
from experiment import *





db = api0.open_db('postgres://postgres:wasser@localhost/log_reg?table=exp_600')
os.system("jobman sqlstatus --all --set_status=START 'postgres://postgres:wasser@localhost/log_reg?table=exp_600'")

A = 10**np.arange(-7,7)

state = DD()
for l2 in A:
    state.l2=l2
    for l2 in A:
        state.second = l2
        sql.insert_job(sk_log_reg, flatten(state), db)



def run(n_times):os.system("jobman sql -n0 'postgres://postgres:wasser@localhost/log_reg?table=exp_600' .")
P = multiprocessing.Pool(12)
P.map(run,range(12))


# sudo -u postgres createdb log_reg --no-password       create database
# psql -h localhost -d mydb -U postgres                 login pass: wasser
# \d                                                    show tables
# DROP TABLE table_name;                                removes table
# dropdb -h localhost -U postgres log_reg               delete database
