# firebase-in-flask

### Objective
* base project for firebase deploy with test environment (flask) / Mac OS X Catalina - 10.15.4 (19E266) 
* use jinja2 to render modulized and reusable templates for static serving on firebase hosting service


### Usage
```bash
$ . init.env        # configuring dev environment...
$ startup           # starting flask server!
$ deploy            # deploy to firebase hosting server
```


### Basic Flow
 + -- Flask -- +                   + -- Firebase -- +
 | testing env |  == $ deploy == > |  real service  |
 + ----------- +      (jinja2)     + -------------- +


### Framework
* Flask : devel
    * used for testing on local machine
    * please do not attempt to use flask no more than rendering html page...
    * every action must be defined in front-end
    * if need to use REST API, need to configure server to support **CORS**
    * using firebase database is suitable for this framework

* Jinja2
    * used to render flask templates
    * render pages to firebase/public when use of **'deploy'** command

* Firebase Hosting : real
    * serve real service on internet
    * can access from external device
    * only serve static pages
