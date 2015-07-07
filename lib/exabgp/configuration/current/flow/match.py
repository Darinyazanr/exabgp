# encoding: utf-8
"""
parse_match.py

Created by Thomas Mangin on 2015-06-22.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
"""

from exabgp.configuration.current.core import Section

from exabgp.configuration.current.flow.parser import source
from exabgp.configuration.current.flow.parser import destination
from exabgp.configuration.current.flow.parser import any_port
from exabgp.configuration.current.flow.parser import source_port
from exabgp.configuration.current.flow.parser import destination_port
from exabgp.configuration.current.flow.parser import tcp_flags
from exabgp.configuration.current.flow.parser import protocol
from exabgp.configuration.current.flow.parser import next_header
from exabgp.configuration.current.flow.parser import fragment
from exabgp.configuration.current.flow.parser import packet_length
from exabgp.configuration.current.flow.parser import icmp_code
from exabgp.configuration.current.flow.parser import icmp_type
from exabgp.configuration.current.flow.parser import dscp
from exabgp.configuration.current.flow.parser import traffic_class
from exabgp.configuration.current.flow.parser import flow_label


class ParseFlowMatch (Section):
	definition = [
		'source 10.0.0.0/24',
		'source ::1/128/0',
		'destination 10.0.1.0/24',
		'port 25',
		'source-port >1024',
		'destination-port =80|=3128|>8080&<8088',
		'packet-length >200&<300|>400&<500',
		'(ipv4 only) protocol [ udp tcp ]',
		'(ipv4 only) fragment [ not-a-fragment dont-fragment is-fragment first-fragment last-fragment ]',
		'(ipv6 only) next-header [ udp tcp ]',
		'(ipv6 only) flow-label >100&<2000',
	]

	syntax = \
		'match {\n' \
		'  %s;\n' \
		'}' % ';\n  '.join(definition)

	known = {
		'source':           source,
		'destination':      destination,
		'port':             any_port,
		'source-port':      source_port,
		'destination-port': destination_port,
		'protocol':         protocol,
		'packet-length':    packet_length,
		'tcp-flags':        tcp_flags,
		'next-header':      next_header,
		'fragment':         fragment,
		'icmp-code':        icmp_code,
		'icmp-type':        icmp_type,
		'packet-length':    packet_length,
		'dscp':             dscp,
		'traffic-class':    traffic_class,
		'flow-label':       flow_label,
	}

	# 'source-ipv4','destination-ipv4',

	action = {
		'source':           'nlri-add',
		'destination':      'nlri-add',
		'port':             'nlri-add',
		'source-port':      'nlri-add',
		'destination-port': 'nlri-add',
		'protocol':         'nlri-add',
		'packet-length':    'nlri-add',
		'tcp-flags':        'nlri-add',
		'next-header':      'nlri-add',
		'fragment':         'nlri-add',
		'icmp-code':        'nlri-add',
		'icmp-type':        'nlri-add',
		'packet-length':    'nlri-add',
		'dscp':             'nlri-add',
		'traffic-class':    'nlri-add',
		'flow-label':       'nlri-add',
	}

	name = 'flow/match'

	def __init__ (self, tokeniser, scope, error, logger):
		Section.__init__(self,tokeniser,scope,error,logger)

	def clear (self):
		pass

	def pre (self):
		self.scope.set(self.name,self.scope.get('flow/route'))
		return True

	def post (self):
		self.scope.pop(self.name)
		return True