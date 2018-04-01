# Let's say you want to scale a range [min,max] to [a,b].
#  You're looking for a (continuous) function that satisfies
# f(min) = a
# f(max) = b
# Formula -        (b-a)(x - min)
#			 f(x) = --------------  + a
# 					max - min 
# a is lower limit of sub-category
# b is upper limit of sub-category

a = 1
b = 10

def normalize(x, a, b, minLikes, maxLikes):
	return (((b - a) * (x - minLikes))/(maxLikes - minLikes+1)) + a

#print(normalize(20,a,b,minLikes,maxLikes))