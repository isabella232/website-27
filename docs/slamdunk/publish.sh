#!/bin/bash

set -e

IMAGE_NAME=slamdunk-website

if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]
then
    docker build -t $IMAGE_NAME .
fi

docker run \
     -v /etc/passwd:/etc/passwd -v $(pwd):$(pwd) -w $(pwd) -u $(id -u):$(id -g) \
     --rm \
     $IMAGE_NAME \
     bundle exec middleman build
