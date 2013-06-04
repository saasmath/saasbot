#!/usr/bin/python



import gst
import shutil
import tempfile
import threading
import time
import traceback
import os



class Camera(object):

  """Interact with the OLPC camera."""

  def __init__(self, snap_path):
    self._snap_path = snap_path
    unused, self._tmp_path = tempfile.mkstemp(dir='static')
    self.lock = threading.Lock()
    self.pipe = self._GetCameraPipe(self._tmp_path)
    self.bus = self.pipe.get_bus()
    self.bus.add_signal_watch()
    self.bus.connect('message', self._OnGstMessage)

  def _GetCameraPipe(self, snap_path):
    pipe = gst.Pipeline('olpc-camera')
    elems = []
    
    def Add(name):
      elem = gst.element_factory_make(name, name)
      pipe.add(elem)
      elems.append(elem)

    Add('v4l2src')
    Add('ffmpegcolorspace')
    Add('pngenc')
    Add('filesink')

    gst.element_link_many(*elems)
    pipe.get_by_name('filesink').set_property('location', snap_path)

    return pipe

  def Snap(self):
    """Take a snapshot."""
    self.lock.acquire()
    self.pipe.set_state(gst.STATE_PLAYING)
    while not self.lock.acquire(False):
      # TODO(damonkohler): I don't see any other sample code doing this.
      # Instead, they all have a GUI loop of some sort that I think makes
      # everything work. What's the right way to do this?
      self.bus.poll(-1, 1)  # Should be instant if there's anything waiting.
      time.sleep(0.5)
    try:
      shutil.move(self._tmp_path, self._snap_path)
    except IOError:
      # NOTE(damonkohler): Ignoring errors for now.
      print 'Failed to move webcam snapshot.'
      traceback.print_exc()
    self.lock.release()

  def _OnGstMessage(self, bus, message):
    """Called when a GST message is received."""
    t = message.type
    if t == gst.MESSAGE_EOS:
      self.pipe.set_state(gst.STATE_NULL)
      self.lock.release()
    elif t == gst.MESSAGE_ERROR:
      self.pipe.set_state(gst.STATE_NULL)
      self.lock.release()
      # NOTE(damonkohler): Ignoring errors for now.

  def StartWebcam(self, delay=1):
    """Starts a thread to take snapshots every 'delay' seconds."""
    webcam = threading.Thread(target=self._Webcam, args=(delay,))
    webcam.setDaemon(True)
    webcam.start()

  def _Webcam(self, delay):
    """Takes a snapshot at a minimum of every 'delay' seconds."""
    while True:
      self.Snap()
      time.sleep(delay)


if __name__ == '__main__':
  snap_path = 'snap.png'
  c = Camera(snap_path)
  c.Snap()
  print 'Captured snapshot to %s' % snap_path
