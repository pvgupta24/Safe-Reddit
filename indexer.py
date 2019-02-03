# import model_output
# from collections import OrderedDict
# call filter.py and store the results in a csv file

ans = {}

def insert_element(post_id, result):
    if post_id in ans.keys() and result == 0:
        # remove the post from the index.
        del ans[post_id]
    else:
        # overwrite the new classification result of id
        ans[post_id] = result

def isToxic(id):
    if id in ans.keys():
        return 1
    else:
        return 0




