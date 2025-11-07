rm -rf build src/staticfiles
./manage.py collectstatic
./manage.py distill-local build
