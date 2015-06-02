###PayPerks Url Shortener

[![Build Status](https://travis-ci.org/gterzian/payperks_demo.svg?branch=master)](https://travis-ci.org/gterzian/payperks_demo)


####Some assumptions
* Let's keep the demo simple, there is no auth and everything, including the API, is fully public
* In "real life", I would probably use Bitly. However in this case it was fun to try to implement the shortener myself
* I started settting up an AngularJS front-end, and then realized it was too much trouble. So at this point it's simple page with a form and some old-school JQuery front-end validation, and we're using the DRF built-in API viewer. 