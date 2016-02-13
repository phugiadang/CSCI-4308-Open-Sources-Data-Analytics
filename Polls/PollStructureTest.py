from pollster import Pollster

pollster = Pollster()

print('\npollster.charts(): ----------------------------------------------')
print(pollster.charts())

print('\npollster.charts(topics = \'obama-job-approval\'))--------------------')
print(pollster.charts(topic = 'obama-job-approval'))

print('\npollster.charts()[0]: -------------------------------------------')
print(pollster.charts()[0])

print('\npollster.charts()[0].estimates: ---------------------------------')
print(pollster.charts()[0].estimates)

print('\npollster.charts()[0].estimates_by_date()[1]: --------------------')
print(pollster.charts()[0].estimates_by_date()[1])