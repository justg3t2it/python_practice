# Lab 3 Skeleton
#
# Based on of_tutorial by James McCauley

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_firewall (self, packet, packet_in):
    # The code in here will be executed for every packet.
    x = of.ofp_flow_mod()  #establishes variables
    x.match = of.ofp_match.from_packet(packet)
    ipv4_type = packet.find('ipv4')
    arp_type = packet.find('arp')
    icmp_type = packet.find('icmp')
    x.hard_timeout = 35
    x.idle_timeout = 35

    if (icmp_type and ipv4_type): #if icmp and ipv4 per rules, allows
      x.data = packet_in
      x.nw_proto = 1
      action = of.ofp_action_output(port = of.OFPP_ALL)
      x.actions.append(action)
      self.connection.send(x)
    elif (arp_type): #if the packet is arp type, allows
      x.data = packet_in
      x.match.dl_type = 0x0806
      action = of.ofp_action_output(port = of.OFPP_ALL)
      x.actions.append(action)
      self.connection.send(x)
    else: #if not  drops
      x.data = packet_in
      self.connection.send(x)
      

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_firewall(packet, packet_in)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
