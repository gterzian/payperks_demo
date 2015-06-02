###PayPerks Url Shortener

[![Build Status](https://travis-ci.org/gterzian/payperks_demo.svg?branch=master)](https://travis-ci.org/gterzian/payperks_demo)
[![Coverage Status](https://coveralls.io/repos/gterzian/payperks_demo/badge.svg?branch=master)](https://coveralls.io/r/gterzian/payperks_demo?branch=master)

####Some assumptions
* Let's keep the demo simple, there is no auth or concept of users, and everything, including the API, is fully public.
* In "real life", I would probably use something like [Claudio's package](https://github.com/jcfigueiredo/python-bitly). However in this case it was fun to try to implement the shortener myself.
* I started settting up an AngularJS front-end, and then realized it was too much trouble. So at this point it's simple page with a form and some old-school JQuery front-end validation, and we're using the DRF built-in API viewer. 
* Demo running on [Heroku](https://powerful-citadel-2869.herokuapp.com/).
* This is, as always, still a work in progress, maybe I will end up adding some Angular if I have time, and your feedback and suggestions are [very welcome](https://github.com/gterzian/payperks_demo/issues/5). 