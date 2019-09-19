# Run the following on spark console

from pyspark.sql import Row
import re

regex = '^([^ ]+) \- \- \[(.+)\] "(.+) (.+) (.+)" ([0-9]+) ([0-9]+)'

def toarry(line):
    m = re.match(regex, line)
    if m:
        g = m.groups()
        if len(g) > 0:
            return [Row(host=g[0], datetime=g[1], type=g[2], url=g[3], retcode=g[5], timetaken=g[6])]
    return []


lines = sc.textFile("/data/spark/project/access/")
rows = lines.flatMap(toarry)
df = rows.toDF()
df.show()
