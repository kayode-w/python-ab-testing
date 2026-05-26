from db_conn import get_engine
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

