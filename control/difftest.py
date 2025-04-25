import pyuart
def regret(last, current):
    """
    将两个长度为9的字符串转换为整数数组。
    X -> 1, O/N -> 0
    """
    def convert_to_int_array(input_str):
        return [1 if char == 'X' else 0 for char in input_str]

    # 生成两个新的整数组 a 和 b
    a = convert_to_int_array(last)
    b = convert_to_int_array(current)
    print(a,'---',b)
    # 逐元素计算 b - a
    diff = [b[i] - a[i] for i in range(len(a))]
    #print("Difference array:", diff)
    
    if all(val == 0 for val in diff):
        return True
    else:
        
        addr1 = next((i + 1 for i, val in enumerate(diff) if val == 1), None)
        addr2 = next((i + 1 for i, val in enumerate(diff) if val == -1), None)
        #print("Position of 1 in diff:", addr1)
        #print("Position of -1 in diff:", addr2)
        print("!!!diff!!!",diff)
        print(f"{0}{addr1}{addr2}")
        pyuart.send_message_once(f"{0}{addr1}{addr2}")
    return False
'''
c1 = "XOOOXXOOO"
c2 = "OOXOXXOOO"

print(regret(c1, c2))'''