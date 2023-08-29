import pandas as pd
def Read_table():
    dataframe1 = pd.read_excel('res/table.xlsx')
    d=dataframe1.to_numpy()
    dict={}

    for raw in d:
        dict[raw[0]]={}
    for raw in d:
        dict[raw[0]][raw[1]]={}
    for raw in d:
        dict[raw[0]][raw[1]][raw[2]]={}
    for raw in d:
        dict[raw[0]][raw[1]][raw[2]]={"Name" : raw[3] ,"cost_C" :raw[4],"cost_T" :raw[5],"cost_D" :raw[6],"cost_S" :raw[7],"gain" :raw[8],"w" :raw[9] if type(raw[9])==int else list(map(int,raw[9].split(","))),"t" :raw[10] if type(raw[10])==int else list(map(int,raw[10].split(","))),"l" :raw[11] if type(raw[11])==int else list(map(int,raw[11].split(","))),"g_w" :raw[12],"g_t" :raw[13],"g_l" :raw[14]}
    return dict
