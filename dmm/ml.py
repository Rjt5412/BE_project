from sklearn.externals import joblib


"""

main_dict = {
	'Sports' : 1,
	'News' : 2,
	'Entertainment' : 3,
	'Lifestyle' : 4,
	'Business' : 5,
}
sub_dict = {
	# 1
	'Cricket' : 10,
	'Football' : 20,
	'Basketball' : 30,
	'Volleyball' : 40,
	'Hockey' : 50,
	'Baseball' : 60,
	'Golf' : 70,
	'Tennis' : 80,
	'Wrestling' : 90,
	'Formula One' : 100

	# 2
	'Local' : 10,
	'International' : 20,
	'Regional' : 30,
	'Politics' : 40

	# 3
	'Bollywood' : 10,
	'Hollywood' : 20,
	'Regional Cinema' : 30,
	'Foreign Televison' : 40,
	'Domestic Televison' : 50,
	'Hindi Music' : 60,
	'English Music' : 70,
	'Regional Music' : 80
	# 4
	'Food' : 10,
	'Travel' : 20,
	'Shopping' : 30,
	# 5
	'Private' : 10,
	'Public' : 20,
	'Start Up' : 30
}

# Co-ordinate Generation
print(main_dict['Politics'], sub_dict['National'])
"""
def ml_func(x,y):
    clf = joblib.load('mlp.pkl')
    result = clf.predict([[int(x),int(y)]])
    return result