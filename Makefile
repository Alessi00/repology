FLAKE8?=	flake8
MYPY?=		mypy
PYTEST?=	pytest

STATICDIR=	repologyapp/static

all: gzip-static

gzip-static:
	gzip -9 -f -k -v ${STATICDIR}/*.css ${STATICDIR}/*.js ${STATICDIR}/*.ico ${STATICDIR}/*.svg

clean:
	rm -f ${STATICDIR}/*.gz

lint:: test flake8 mypy

test::
	${PYTEST} ${PYTEST_ARGS} -v -rs

test-with-dump::
	psql -U repology_test < testdata/repology_test.sql
	env REPOLOGY_CONFIG=./repology-test.conf.default ${PYTEST} ${PYTEST_ARGS} -v -rs

flake8:
	${FLAKE8} *.py repologyapp tests

mypy:
	${MYPY} repology-app.py repologyapp
