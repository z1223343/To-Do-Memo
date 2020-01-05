def continue_crawl(search_history,target_url):
	if len(search_history) > 24:
	return False
	'''loop is shut down because the loop run enough time'''
	elif search_history(len(search_history)) == target_url:
	return False
	#'loop is shut down because we find the target website'
	else if search_history[-1] in search_history[:-1]:
	return False
	# 'loop is shut down becaues we find'
	else :
	return True