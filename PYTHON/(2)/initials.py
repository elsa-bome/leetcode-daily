def get_initials(fullname):
	initials = ""
	for name in fullname.split():
		initials += name[0]+"."
	print(initials)
