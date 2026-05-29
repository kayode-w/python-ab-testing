import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Merge the tables needed and get the necessary fields.
def get_user_transactions(usr: pd.DataFrame, txn: pd.DataFrame) -> pd.DataFrame:
    try:
        df = pd.merge(usr[['user_id', 'plan']], txn['sender_id'], left_on= 'user_id', right_on='sender_id', how = 'left')
        grped_df = df.groupby(['user_id', 'plan']).agg({'sender_id': 'count'}).reset_index().rename(columns = {'sender_id': 'txn_count'})
        return grped_df
    
    except Exception as e:
        raise ValueError(f"An error occured while trying to merge both tables: {e}")
    

#Get the groups
def get_plan_groups(df: pd.DataFrame) -> tuple:
    try:
        grp_basic = df.loc[df['plan'] == 'basic', 'txn_count']
        grp_standard = df.loc[df['plan'] == 'standard', 'txn_count']
        grp_premium = df.loc[df['plan'] == 'premium', 'txn_count']
        return grp_basic, grp_standard, grp_premium
    
    except Exception as e:
        raise ValueError(f"An error occured while trying to group the data by plan: {e}")
    
#Run the t-test
def perform_test(grp_1: pd.Series, grp_2:pd.Series) -> tuple:
    try:
        t_static, p_value = ttest_ind(grp_1, grp_2, equal_var=False)
        return t_static, p_value

    except Exception as e:
        raise ValueError(f"An error occured while trying to perform the t-test: {e}")
    
#Ochestrotor fxn to run the test and print the results
def user_txn_test(user_df: pd.DataFrame, txn_df: pd.DataFrame) -> None:
    df = get_user_transactions(user_df, txn_df)
    grps = get_plan_groups(df)
    basic, standard, premium = grps
    b_p = perform_test(basic, standard)
    s_p = perform_test(standard, premium)
    p_b = perform_test(basic, premium)

    print(f"\nBasic vs Standard: t-statistic = {round(b_p[0], 2)}, p-value = {round(b_p[1], 2)}")
    print(f"Standard vs Premium: t-statistic = {round(s_p[0], 2)}, p-value = {round(s_p[1], 2)}")
    print(f"Basic vs Premium: t-statistic = {round(p_b[0], 2)}, p-value = {round(p_b[1], 2)}")

#---------------------------------------------------------
# Do KYC verified users make more transactions than unverified

def user_kyc_txn(df_1: pd.DataFrame, df_2: pd.DataFrame)-> pd.DataFrame:
    try:
        df = pd.merge(df_1[['user_id', 'kyc_verified']], df_2[['sender_id']], left_on= 'user_id', right_on='sender_id', how = 'left')
        grped_df = df.groupby(['user_id', 'kyc_verified']).agg({'sender_id': 'count'}).reset_index().rename(columns = {'sender_id': 'txn_count'})
        return grped_df

    except Exception as e:
        raise ValueError(f"An error occured while trying to merge both tables: {e}")
            
    
def user_kyc_grp(df:pd.DataFrame) -> tuple:
    try:
        grp_y = df.loc[df['kyc_verified'] == True, 'txn_count']
        grp_n = df.loc[df['kyc_verified'] == False, 'txn_count']
        return grp_y, grp_n

    except Exception as e:
        raise ValueError(f"An error occured while trying to group the data by KYC status: {e}")
    
def perform_test(grp_1: pd.Series, grp_2:pd.Series) -> tuple:
    try:
        t_static, p_value = ttest_ind(grp_1, grp_2, equal_var=False)
        return t_static, p_value

    except Exception as e:
        raise ValueError(f"An error occured while trying to perform the t-test: {e}")
    

def user_kyc_txn_test(user_df: pd.DataFrame, txn_df: pd.DataFrame) -> None:

    df = user_kyc_txn(user_df, txn_df)
    grp = user_kyc_grp(df)
    grp_y, grp_n = grp
    y_n = perform_test(grp_y, grp_n)

    print(f"\nKYC Verified vs Unverified: t-statistic = {round(y_n[0], 2)}, p-value = {round(y_n[1], 2)}")


#---------------------------------------------------------
# Do iOS users generate more events than Android users?

def user_device_event(df_1: pd.DataFrame, df_2: pd.DataFrame, df_3: pd.DataFrame)-> pd.DataFrame:
    try:
        df = pd.merge(df_1[['user_id']], df_2[['sender_id']], left_on= 'user_id', right_on='sender_id', how = 'left')
        df_2 = pd.merge(df, df_3[['user_id', 'device_type']], on= 'user_id',  how = 'left')

        grped_df = df_2.groupby(['user_id', 'device_type']).agg({'sender_id': 'count'}).reset_index().rename(columns = {'sender_id': 'event_count'})
        return grped_df

    except Exception as e:
        raise ValueError(f"An error occured while trying to merge both tables: {e}")
    
def user_device_grp(df:pd.DataFrame) -> tuple:
    try:
        grp_ios = df.loc[df['device_type'] == 'iOS', 'event_count']
        grp_android = df.loc[df['device_type'] == 'Android', 'event_count']
        return grp_ios, grp_android

    except Exception as e:
        raise ValueError(f"An error occured while trying to group the data by device type: {e}")

def user_device_test(user_df: pd.DataFrame, user_txn_df: pd.DataFrame, event_df: pd.DataFrame) -> None:
    
    df = user_device_event(user_df, user_txn_df, event_df)
    grp = user_device_grp(df)
    grp_ios, grp_android = grp
    
    ios_android = perform_test(grp_ios, grp_android)

    print(f"\niOS vs Android: t-statistic = {round(ios_android[0], 2)}, p-value = {round(ios_android[1], 2)}")

