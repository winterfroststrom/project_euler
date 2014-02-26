days = 1
sundays = 0
for year in range(1901, 2000):
	if days % 7 == 0:
		sundays = sundays + 1
	days = days + 31
	if days % 7 == 0:
		sundays = sundays + 1
	if year % 4 == 0 and year % 400 != 0:
		days = days + 1
	days = days + 28
	for i in range(0, 2):
		if days % 7 == 0:
			sundays = sundays + 1
		days = days + 31
		if days % 7 == 0:
			sundays = sundays + 1
		days = days + 30
	if days % 7 == 0:
		sundays = sundays + 1
	days = days + 31
	if days % 7 == 0:
		sundays = sundays + 1
	days = days + 31
	for i in range(0, 2):
		if days % 7 == 0:
			sundays = sundays + 1
		days = days + 30
		if days % 7 == 0:
			sundays = sundays + 1
		days = days + 31

print sundays
