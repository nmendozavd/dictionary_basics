

def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)

        # alternate method:
        # concatenating variables to strings commonly done with the .format() method (can be used on any string, or variable that
            # contains a string

        #print "My {} is {}".format(some_key, some_value)



information = {"name": "My name is Noel", "age": "My age is 27", "country": "My country of birth is The United States", "langauge": "My favorite language is Python" }
for data in information:
    print data
