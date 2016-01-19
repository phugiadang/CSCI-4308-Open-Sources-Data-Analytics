Below is the structure of the data returned by running the queryPolls and then getPolls functions of a pollGrabber object.

For example...
```
pg = PollGrabber('2016-president-dem-primary', '2014-01-01', '2016-12-31')
pg.queryPolls
pg.getPolls
```

...will return data with the following structure, complete with example data:

```

[{
	startDate '2015-08-05',
	endDate '2015-08-05',
	pollster 'Landmark (R)',
	name '2016 Georgia Presidential Democratic Party'
	observations '600'
	responses
	[{
		first_name 'Joe'
		last_name 'Biden'
		value '18'
		choice 'Biden'
		incumbent 'false'
		party 'Dem'
	},
	{
		first_name 'Hillary'
		last_name 'Clinton'
		value '56'
		choice 'Clinton'
		incumbent 'false'
		party 'Dem'
	},
	{
		...
		...
		...
	}]
},
{
	startDate
	endDate
	pollster
	...
	...
	...
}]
```
