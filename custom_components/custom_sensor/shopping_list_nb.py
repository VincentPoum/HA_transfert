#--------------------------------------------------------------------------------------------------
# Creates sensor with shopping list items
#--------------------------------------------------------------------------------------------------

#!/usr/local/bin/python
# coding: utf8
import json

with open('/config/.shopping_list.json') as data_file:
    shoppingListData = json.load(data_file)

content = 0
for entry in shoppingListData:
    if not entry['complete']:
        content ++

print(content)