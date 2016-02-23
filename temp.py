from jsonize import jsonize

days = ['from 20160213000000 to 20160213010000', 'from 20160213010000 to 20160213020000', 'from 20160213020000 to 20160213030000', 'from 20160213030000 to 20160213040000', 'from 20160213040000 to 20160213050000', 'from 20160213050000 to 20160213060000', 'from 20160213060000 to 20160213070000', 'from 20160213070000 to 20160213080000', 'from 20160213080000 to 20160213090000', 'from 20160213090000 to 20160213100000', 'from 20160213100000 to 20160213110000', 'from 20160213110000 to 20160213120000', 'from 20160213120000 to 20160213130000', 'from 20160213130000 to 20160213140000', 'from 20160213140000 to 20160213150000', 'from 20160213150000 to 20160213160000', 'from 20160213160000 to 20160213170000', 'from 20160213170000 to 20160213180000', 'from 20160213180000 to 20160213190000', 'from 20160213190000 to 20160213200000', 'from 20160213200000 to 20160213210000', 'from 20160213210000 to 20160213220000', 'from 20160213220000 to 20160213230000', 'from 20160213230000 to 20160214000000']

counts = ['0', '0', '0', '0', '0', '952', '5630', '4228', '3361', '3086', '2735', '4267', '4751', '6239', '7852', '8901', '10201', '9896', '10367', '9656', '10099', '10451', '13129', '11405']

jsonizer = jsonize()
f = open('sandersJson.json', 'w')
f.write(jsonizer.makeJson('Sanders', days, counts))
