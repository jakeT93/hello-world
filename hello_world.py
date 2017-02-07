import time;

print 'hello world!'
myName = 'Kiren'
myAge = 23
print "My name is %s and I'm %d years old!" % (myName, myAge);
time_tuple = time.localtime(time.time());
date = time_tuple
print "The time right now is ", time.asctime(time_tuple); 