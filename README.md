admB
====

Nueva Base Core 2.0 E-Stars

To install from scratch:
```
$ sudo apt-get install libevent-dev libzmq-dev python-dev
$ wget http://peak.telecommunity.com/dist/ez_setup.py
$ sudo python ez_setup.py
$ sudo easy_install pip
$ sudo pip install virtualenv
$ virtualenv hind
$ source hind/bin/activate
```
Create and install the package:
```
$ python setup.py sdist
$ pip install dist/Hindoor-0.1.*.tar.gz
```
To test it:
```
$ start_hinterface -s 127.0.0.1:5001 &
$ cd src_dbg
$ python serverstarter.py -p 5001 &
; open explorer in http://127.0.0.1:8888/index.html
```
Installed commands
```
$ start_hinterface &
$ start_hlog &
$ start_sstats &
$ hindebug
```