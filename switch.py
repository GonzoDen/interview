def level_worry(ind):
	conditions = {
		0: "oi",
		1: "blen",
		2: "ok"
	}

	return conditions.get(ind, "nothing")

ind =0
print(level_worry(ind))