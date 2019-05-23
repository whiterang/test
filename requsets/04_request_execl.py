import xlrd

def read_execl(execl_path,sheet_name):

    results=[]
    data = xlrd.open_workbook(execl_path)
    table = data.sheet_by_name(sheet_name)
    print(table.nrows)
    for row in range(1,table.nrows):
        results.append(table.row_values(row))
        return results


if __name__ == "__main__":
    data = read_execl("./testcases\接口测试用例模板.xlsx","Sheet1")
    for a in data:
        print(a)