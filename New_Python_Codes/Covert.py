import os, pandas,shutil
from xlrd import open_workbook


def convert(path, Archive):
    def files(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                yield file
    for file in files(path):
        if 'json' in file:
            print (file +' is in JSON format must be coverted')
            full_path = (path + '\\' + file)
            name = file.replace("json", "csv")
            new_path=(path + '\\' + name)
            df = pandas.read_json(full_path, orient='records')
            print(df)
            df.to_csv(name, index=False)
            shutil.move(name, new_path)
            shutil.move(full_path,Archive)
        elif 'csv' in file:
            print (file + ' is in correct format format')
        else:
            print (file +' is in Excel format must be coverted')
            full_path =(path+'\\'+file)
            wb = open_workbook(full_path)
            print(full_path)
            print(wb)
            sheets = range(0, wb.nsheets)
            for i in sheets:
                sheet = wb.sheet_by_index(i)
                print sheet.name
                Sheet_name = sheet.name.replace(" ", "") + '.csv'
                print(Sheet_name)
                with open(Sheet_name, "w") as file:
                    writer = csv.writer(file, delimiter=",")
                    print sheet, sheet.name, sheet.ncols, sheet.nrows
                    header = [cell.value for cell in sheet.row(0)]
                    writer.writerow(header)
                    for row_idx in range(1, sheet.nrows):
                        row = [int(cell.value) if isinstance(cell.value, float) else cell.value
                               for cell in sheet.row(row_idx)]
                        writer.writerow(row)
                    print(file)
                    print(Sheet_name)
                shutil.move(Sheet_name, path)
            shutil.move(full_path,Archive)
