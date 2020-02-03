



docker build --build-arg PYTHON_HELLO_WEB_MSG="BAR BAR BAR" -t haalcala/python-hello-web-bar-v1 -t python-hello-web-bar-v1 .


docker build --build-arg PYTHON_HELLO_WEB_MSG="FOO FOO FOO" -t haalcala/python-hello-web-foo-v1 -t python-hello-web-foo-v1 .

docker push haalcala/python-hello-web-bar-v1
docker push haalcala/python-hello-web-foo-v1


