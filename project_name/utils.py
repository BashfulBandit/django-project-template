def str2bool(str):
	if isinstance(str, bool):
        return str
	else:
		if str.lower() == 'true':
            return True
		elif str.lower() == 'false':
            return False
		else:
            raise ValueError(
                "Cannot covert {} to a bool".format(str)
            )
