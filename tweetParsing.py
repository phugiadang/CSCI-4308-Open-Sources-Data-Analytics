import json

tweets = []

i = 0
for line in open('tweets.json'):
	i += 1
	try:
		tweets.append(json.loads(line))
	except:
		pass

print(tweets.keys())
# i = 0
# for result in results:
# 	i = i + 1
# 	save_file = open('tweets.json', 'a')
# 	save_file.write(str(results))
	# print ("TWEET NUMBER : " + str(i) + " " + result.text + "\n" +"Created at :" +  str(result.created_at) + "\n")

