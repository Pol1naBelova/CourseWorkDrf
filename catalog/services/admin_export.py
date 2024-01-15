import datetime

import xlwt
from django.http import FileResponse

def file_iterator(filename, chuck_size=512):
    with open(filename, "rb") as f:
        while True:
            c = f.read(chuck_size)
            if c:
                yield c
            else:
                break


def export_excel(queryset, headers, columns, filename='file_name'):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("data")
    for i, h in enumerate(headers):
        sheet.write(0, i, h)
    cols = 1
    for query in queryset.values(*columns):
        for i, k in enumerate(columns):
            v = query.get(k)
            if isinstance(v, datetime.datetime):
                v = v.strftime('%Y-%m-%d %H:%M:%S')
            sheet.write(cols, i, v)
        cols += 1
    wb.save(filename)
    response = FileResponse(file_iterator(filename))
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response
