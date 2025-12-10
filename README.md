                                    #Locust API load test

This script runs a full CRUD (Create, Get, Update and Delete) load test. This is to measure RPS (Response Per Second), latency and error rate against jsonplaceholder.typicode.com. 
Performance stays flat even past 5000 concurrent users, no throttling. 

Note: endpoints are like bouncers. http://bin.org or .io blocked me with 503 and 404 errors, this one didn't. Learned it and tested it.  
