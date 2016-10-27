This is a short example that produces a failure I don't understand when using falcon and crochet together.

Running `tox -e test` will run a test that _should_ pass, assuming the computer
has outbound network access and the site it is accessing is not down.

Running `tox -e run` starts the actual wsgi app with a twisted server. To run a request through the
crochet resource, simply hit `localhost:8008/threaded`. It should return the json that _would_ be returned
by `https://firedamp.heroku.com`
