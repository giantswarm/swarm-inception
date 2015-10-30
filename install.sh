#!/bin/bash

# load latest version
VERSION=$(curl -sS https://downloads.giantswarm.io/swarm/clients/VERSION)

# download latest version
curl http://downloads.giantswarm.io/swarm/clients/$VERSION/swarm-$VERSION-linux-amd64.tar.gz > swarm-$VERSION.tar.gz

# unzip
gzip -cd swarm-$VERSION.tar.gz | tar -x

# move and cleanup
mv swarm /usr/bin/swarm
rm swarm-*