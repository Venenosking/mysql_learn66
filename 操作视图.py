
import os
file_name = os.path.basename(__file__)[2:-3]

p_view = {key + ' ('+file_name+')': value for key, value in {
    "如何删除视图":"drop view 视图名称;",
    "如何修改视图":"alter view 视图名称 as select 语句;",
    # "":"",

}.items()}


