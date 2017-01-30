# WEEK 4 Assignment: Eric Wahlstrom

# ===========================================================
# IMPORTS
# Here are the libraries and functions I'm importing for my
# yelpapi.py script to fucntion properly.
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# ===========================================================
# ONE FUNCTION TO RULE THEM ALL!!!
# The 'get_businesses' function returns the top 3 yelp results
# when the arguments 'location' and 'term' are defined.
# Specifically, it lists 3 result names, ratings and phone 
# numbers.  
# I had a lot of trouble improving the look of the formatting
# for the three different results on the index page.
# I'm still not completely happy with the look but below 
# is the best I could come up with after spending hours
# trying different methods.  I created a variable that loops
# the 3 different results.  It's doesn't look great but it 
# does look much better than returning 'businesses' alone.
# Below is some code that's commented out.  This is how I
# would have preferred displaying each of the 3 businesses,
# however, I could only produce the first business result
# with this and could not find a way to list all 3.
def get_businesses(location, term):
	auth = Oauth1Authenticator(
    	consumer_key=os.environ["YELP_CONSUMER_KEY"],
	    consumer_secret=os.environ["YELP_CONSUMER_SECRET"],
	    token=os.environ["YELP_TOKEN"],
	    token_secret=os.environ["YELP_TOKEN_SECRET"]
	    )

	client = Client(auth)

	params = {
	    'term': term,
	    'lang': 'en',
	    'limit': 3
	}

	response = client.search(location, **params)

	businesses = []

	for business in response.businesses:
		# return "{} has {}/5.0 rating.  The phone # is: {}".format(
		# 	business.name, business.rating, business.phone)
		# return "Business: {}, Rating: {}, Phone #: {}".format(business.name, 
			# business.rating, business.phone)
		businesses.append({"name": business.name, 
			"rating": business.rating, 
			"phone": business.phone
		})

	business_dictionary = (businesses[0]["name"], 
		businesses[0]["rating"], businesses[0]["phone"], 
		businesses[1]["name"], businesses[1]["rating"], 
		businesses[1]["phone"], businesses[2]["name"], 
		businesses[2]["rating"], businesses[2]["phone"])

	return business_dictionary

