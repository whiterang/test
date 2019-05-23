import xlrd

def read_excel(execl_path,execl_name):

    result=[]
    data = xlrd.open_workbook(execl_path)
    table = data.sheet_by_name(execl_name)
    for row in range(1,table.nrows):
        result.append(table.row_values(row))
    
    return result

if __name__ == "__main__":
    data = read_excel("./testcases/接口测试用例模板.xlsx", "Sheet1")
    for a in data:
        print(a)