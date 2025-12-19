# 组合两个表
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    #插入数据
    result_frame = pd.merge(person,address,on = 'personId',how = 'left')
    #选择输出的列
    result_frame = result_frame[['firstName','lastName','city','state']]
    return result_frame

# Example usage:
person = pd.DataFrame({
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
})
address = pd.DataFrame({
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
})
output = combine_two_tables(person, address)
print(output)