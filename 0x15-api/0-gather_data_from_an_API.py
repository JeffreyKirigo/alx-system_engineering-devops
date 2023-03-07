#!/usr/bin/python3
"""
Returns information about employee TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    num = sys.argv
    if len(num) > 1:
        url = 'https://jsonplaceholder.typicode.com'
        user = requests.get(f'{url}/users/{num[1]}').json()
        todos = requests.get(f'{url}/todos', params={"userId": num[1]}).json()

        completed = [t.get("title")
                     for t in todos if t.get("completed") is True]
        print(
            f'Employee {user.get("name")} is done with tasks({len(completed)}/{len(todos)})')
        for c in completed:
            print(f'\t{c}')
