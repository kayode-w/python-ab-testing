from db_conn import get_engine
from analytics import get_user_transactions, get_plan_groups, perform_test, user_txn_test
import pandas as pd


engine = get_engine()

conn_test = pd.read_sql(
    '''
    select table_name FROM information_schema.tables WHERE table_schema = 'public'
    ''', engine
)
if len(conn_test) > 0:
    print(f'The schema contains {len(conn_test)} tables.\n')
    print(conn_test)

else:
    print('Connection successful but schema contains 0 tables.')


users_df = pd.read_sql('select * from users', engine)
transactions_df = pd.read_sql('select * from transactions', engine)
events_df = pd.read_sql('select * from events', engine)


user_txn_test(users_df, transactions_df)



