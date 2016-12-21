# Falcon Framework running on Google App Engine (Flexible environment.)

[Falcon official](http://falconframework.org/)

[Google App Engine official](1https://cloud.google.com/appengine/docs/flexible/python/)


## Prerequisites
- Python 3.x
- [gunicorn](http://gunicorn.org/) for local test.
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/)

It's highlly recommended to use [Anaconda](https://docs.continuum.io/anaconda/install) to keep your python env clean with multiple python versions.

## Setup instructions
1. Install [Anaconda](https://docs.continuum.io/anaconda/install).
2. Create anaconda environment for python3.x and activate it.
```bash
$ conda create --name py35 python=3
$ source activate py35
```
3. Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
4. Install gunicorn
```bash
(py35)~/ % pip install gunicorn
```
5. Clone this repository to your workspace.
```bash
(py35)~/ % mkdir workspace/
(py35)~/ % cd workspace/
(py35)~/ % git clone https://github.com/yukoga/falcon-appengine.git
(py35)~/ % cd falcone-appengine
```
6. Resolve dependencies.
```bash
(py35)~/ % mkdir lib
(py35)~/ % pip install -t lib -r requirements.txt
```
7. Local test.
```bash
(py35)~/ % gunicorn -b :8080 main:api
```
Then you'll see the sample html page at [http://localhost:8080/things](http://localhost:8080/things) on your browser.
