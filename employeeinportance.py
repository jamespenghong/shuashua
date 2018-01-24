"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emps = {employee.id : employee for employee in employees}
        def dfs(id):
            sub_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
            return sub_importance + emps[id].importance
        return dfs(id)

"""
使用了字典生成式
"""