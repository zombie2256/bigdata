
from pyspark.sql import Row
import re

regex = '^([^ ]+) \- \- \[(.+)\] "(.+) (.+) (.+)" ([0-9]+) ([0-9]+)'

def toarry(line):
    m = re.match(regex, line)
    if m:
        g = m.groups()
        return [Row(host=g[0], datetime=g[1], type=g[2], url=g[3], retcode=g[5], timetaken=g[6])]
    else:
        []
        
lines.flatMap(toarry).toDF().show()
