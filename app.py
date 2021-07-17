import sys
import json

solutions = []
def check_for_sum(vals, tar, dic, arr, i):
    """arr and dic store information between each itteration, i, of the loop"""
    if tar > 0:
        for key in vals.keys():
            v = vals[key]
            res_dict = dic.copy()
            res = arr.copy()
            if res_dict.get(key):
                res_dict[key] = res_dict[key] + 1
            else:
                res_dict[key] = 1
            res.append(v)
            val = round(sum(res), 2)
            if val == tar:
                solutions.append(res_dict)
            elif val < tar:
                check_for_sum(vals, tar,res_dict, res, i + 1)
    
    if i == 0:
        if len(solutions) > 0:
            res = f'${tar} can be made by getting '
            sol_vals = solutions[0]
            for key in sol_vals.keys():
                res = res + f'{sol_vals[key]} {key}'
            return res
        else:
            return f'{tar} could not be made by summing prices'


def get_item_price(item):
    try:
        float_price = float(item["Price"].replace('$', '')) 
    except:
        print(f"{item['Name']}: {item['Price']} is not a valid price")
        sys.exit(404)
    
    return float_price

if __name__ == '__main__':
    file = sys.argv[1]
    data = open(file)
    json_data = json.load(data)

    try:
        tar_p = float(json_data['Target Price'].replace('$', ''))
    except:
        if json_data.get('Target Price'):
            print(f"Target Price:{json_data['Target Price']} is not a valid target price")
        else:
            print('no target price could be found')
        sys.exit(404)

    items = {}
    if json_data.get('Items'):
        try:
            for item in json_data['Items']:
                item_price = get_item_price(item)
                items[item['Name']] = item_price    
        except:
            print(f'list of items or prices is not valid')
            sys.exit(404)

    arr = []
    dic = {}
    print(check_for_sum(items, tar_p, dic, arr, 0))