
def write_feather(arr, dst):
    df = pd.DataFrame(arr)
    df.columns('somthing')
    feather.write_dataframe(df, dst)