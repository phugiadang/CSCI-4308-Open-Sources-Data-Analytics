from pollster import Pollster

pollster = Pollster()

def obamaLeadOverRomney():
	poll = pollster.polls(chart='2012-general-election-romney-vs-obama')[0]
	question = [x['subpopulations'][0] for x in poll.questions if x['chart'] == '2012-general-election-romney-vs-obama'][0]
	obama = [x for x in question['responses'] if x['choice'] == 'Obama'][0]
	romney = [x for x in question['responses'] if x['choice'] == 'Romney'][0]
	print(obama['value'] - romney['value'])


def obamaApproval():
	#this returns a list of three dictionaries
	#the first is approve, second is disapprove, third is undecided
	chart = pollster.charts(topic='obama-job-approval')[0]
	approve = chart.estimates[0]['value']
	disapprove = chart.estimates[1]['value']
	undecided = chart.estimates[2]['value']
	print('Approve: ' + str(approve))
	print('Disapprove: ' + str(disapprove))
	print('Undecided: ' + str(undecided))
	#uncomment this to see all three dictionary components
	#print(chart.estimates)

def statePolls(State):
	chart = pollster.charts(state = State)
	#change the value from 0 to see different polls, and
	#remove everything after "chart" to see all polls
	print('Obama: ' + str(chart[0].estimates[0]['value']) + ', Romney: ' + str(chart[0].estimates[1]['value']) + ', Undecided: ' + str(chart[0].estimates[2]['value']))

statePolls('CO')
