# 组合两个表
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = person.merge(address[['personId', 'city', 'state']], on='personId',how='left')

    result = merged[['firstName', 'lastName', 'city', 'state']]

    return result

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