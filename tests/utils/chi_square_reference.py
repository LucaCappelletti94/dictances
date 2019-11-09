from scipy.stats import chisquare

def chi_square_distance(vals):
	return chisquare(vals)[0]