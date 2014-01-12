from mininet.link import TCIntf

class VLANIntf( TCIntf ):
	def config( self, mode="tag", vlan=[0], **params ):
		result = TCIntf.config( self, **params )
		self._mode = mode
		self._vlan = None

		if len(vlan) == 0:
			self._mode='tag'
			self._vlan = '1'
			return result
		if mode == "tag":
			self._vlan = str(vlan[0])
		elif mode == "trunk":
			self._mode = "trunks"
			self._vlan = ','.join([str(x) for x in vlan])

		return result

	def set_vlan( self ):
		if self._vlan:
			output = ""
			output = self.cmd( 'ovs-vsctl set port %s %s=%s' % ( self, self._mode, self._vlan ) )
