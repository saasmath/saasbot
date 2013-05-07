#!/usr/bin/python

# The MIT License
#
# Copyright (c) 2007 Damon Kohler
# Copyright (c) 2013 Gary Anderson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import with_statement

"""A web-based user interface using PyRobot and GSD."""

__author__ = "damonkohler@gmail.com (Damon Kohler)"

import logging
import StringIO
import sys
import simplejson
import gsd
import fido
import Queue
import threading
import urllib2
import time

FORMAT = '%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s'
DATE_FORMAT = '%H%M%S'

class FidoWeb(gsd.App):

  """Control and monitor the Robot through a web interface."""

  def __init__(self, robot_tty='/dev/ttyUSB0'):
    self._fido = fido.Fido(robot_tty)
    self._lock = threading.Lock()

  def GET_(self, handler):
    """Render main UI."""
    handler.Render(open('static/index.html').read(), locals())

  def GET_favicon_ico(self, handler):
    """Ignore requets for favico.ico."""
    pass

  def GET_forward(self, handler):
    """Drive forward in a straight line for 1 second."""
    self._fido.Forward()

  def GET_reverse(self, handler):
    """Drive backward in a straight line for 1 second."""
    self._fido.Reverse()

  def GET_left(self, handler):
    """Turn in place to the left."""
    self._fido.Left()

  def GET_right(self, handler):
    """Turn in place to the right."""
    self._fido.Right()

  def GET_undock(self, handler):
    """Backup out of dock."""
    self._fido.Undock()

  def GET_dock(self, handler):
    """Start docking procedures."""
    self._fido.Dock()

  def GET_restart(self, handler):
    """Restart systems in an emergency to get control of the robot."""
    self._fido.Restart()

  def GET_sensors(self, handler):
    """Return a JSON object with various sensor data."""
    handler.wfile.write(simplejson.dumps(self._fido.sensors.data))

  def GET_webbytes(self,handler,bytes=None):
    #logging.info('Rawbytes %s.' % bytes)
    moveitstr = bytes[0]
    moveit = map( int, moveitstr.split(',') )
    self._fido.Rawbytes(moveit)

def main():
  robot_tty = '/dev/ttyUSB0'
  if len(sys.argv) == 5:
    robot_tty = sys.argv[4]

  logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt=DATE_FORMAT)

  fido_web = FidoWeb(robot_tty)
  fido_web._fido.Start()
  fido_web.Main()


if __name__ == '__main__':
  main()
