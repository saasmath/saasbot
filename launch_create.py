#!/usr/bin/python

# MIT License
#
# Copyright (c) 2013 Gary Anderson

__author__ = "ganderson@seattleacademy.org (Gary Anderson)"

import logging
import StringIO
import sys
import simplejson
import gsd
import create
import Queue
import threading
import urllib2
import time
import camera

FORMAT = '%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s'
DATE_FORMAT = '%H%M%S'

class CreateWeb(gsd.App):

  """Control and monitor the Robot through a web interface."""

  def __init__(self):
    self._create = create.Create()
    self._lock = threading.Lock()
 #   cam = camera.Camera('static/webcam.png')
 #   cam.StartWebcam()

  def GET_(self, handler):
    """Render main UI."""
    handler.Render(open('static/index.html').read(), locals())

  def GET_abc(self, handler):
    """Render main UI."""
    handler.Render(open('static/sensors.html').read(), locals())

  def GET_favicon_ico(self, handler):
    """Ignore requets for favico.ico."""
    pass

  def GET_forward(self, handler):
    handler.wfile.write(self._create.forward())

  def GET_reverse(self, handler):
    """Drive backward in a straight line for 1 second."""
    handler.wfile.write(self._create.reverse())

  def GET_left(self, handler):
    """Turn in place to the left."""
    handler.wfile.write(self._create.left())

  def GET_right(self, handler):
    """Turn in place to the right."""
    handler.wfile.write(self._create.right())

  def GET_goleft(self, handler):
    """Turn in place to the right."""
    handler.wfile.write(self._create.goleft())

  def GET_goright(self, handler):
    """Turn in place to the right."""
    handler.wfile.write(self._create.goright())

  def GET_stop(self, handler):
    """Turn in place to the right."""
    handler.wfile.write(self._create.stop())

  def GET_accelerate(self, handler):
    """Turn in place to the right."""
    handler.wfile.write(self._create.accelerate())

  def GET_brake(self, handler):
    """Turn in place to the right."""
    handler.wfile.write(self._create.brake())

  def GET_decelerate(self, handler):
    """Turn in place to the right."""
    handler.wfile.write(self._create.decelerate())

  def GET_toPassiveMode(self, handler):
    """To Passive Mode"""
    handler.wfile.write(self._create.toPassiveMode())

  def GET_toSafeMode(self, handler):
    """To Passive Mode"""
    handler.wfile.write(self._create.toSafeMode())

  def GET_toFullMode(self, handler):
    """To Passive Mode"""
    handler.wfile.write(self._create.toFullMode())

  def GET_drive(self,handler,velocity=['0'],radius=['32768']):
    self._create.drive(velocity[0],radius[0])
    handler.wfile.write(radius[0])

  def GET_sensors(self, handler):
    """Return a JSON object with various sensor data."""
    handler.wfile.write(simplejson.dumps(self._create.sensors.data))

  def GET_webbytes(self,handler,bytes=None):
    #logging.info('Rawbytes %s.' % bytes)
    moveitstr = bytes[0]
    moveit = map( int, moveitstr.split(',') )
    handler.wfile.write(self._create._rawSend(moveit))

  def GET__rawSend(self,handler,bytes=None):
    #logging.info('Rawbytes %s.' % bytes)
    moveitstr = bytes[0]
    moveit = map(int, moveitstr.split(',') )
    handler.wfile.write(self._create._rawSend(moveit))

  def GET_getSensor(self,handler,sensorToRead):
    sensor = sensorToRead[0]
    handler.wfile.write(self._create.getSensor(sensor))

def main():

  logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt=DATE_FORMAT)
  create_web = CreateWeb()
  create_web.Main()


if __name__ == '__main__':
  main()
