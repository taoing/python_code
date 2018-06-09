import os
from datetime import datetime

def time2str(timestamp):
	fmtime = datetime.fromtimestamp(timestamp)
	return fmtime.strftime('%b %d %H:%M')
for filename in os.listdir():
	file = os.path.join(os.path.abspath('.'), filename)
	finfo = '%s      %s      %s' % (time2str(os.path.getmtime(file)),os.path.getsize(file),filename)
	print(finfo)