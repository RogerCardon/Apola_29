
path:str="devices" 
mission_type:list=["ORBONE","CLNM","TMRS","GALXONE","UNKN"]
#registry_number_1:list=[1,2,3,4,5,6,7,8,9,10]
registry_number_2:list=[1,2,3,4,5,6,7,8,9,10]


def file_generator(path:str,mission_type:list,registry_number_2:list)->str:
  with open((f'{path}/APL-{mission_type}-{registry_number_2}.log'),"x") as file_x:
    result=file_x
  return result

file_generator(path,mission_type[3],registry_number_2[2])