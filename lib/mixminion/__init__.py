# Copyright 2002-2003 Nick Mathewson.  See LICENSE for licensing information.
# $Id: __init__.py,v 1.18 2003/01/06 05:03:34 nickm Exp $

"""mixminion

   Client and shared code for type III anonymous remailers.
   """

# This version string is generated from setup.py; don't edit it.
__version__ = "0.0.2rc1"
__all__ = [ 'server', 'directory' ]

## import mixminion.BuildMessage
## import mixminion.Crypto
## import mixminion.Common
## import mixminion.Config
## import mixminion.MMTPClient
## import mixminion.Packet
## import mixminion.ServerInfo

## This next segment keeps pychecker from making spurious complaints.
import sys
if sys.modules.has_key("pychecker"):
    import mixminion.ClientMain
    import mixminion.server
    import mixminion.test
    import mixminion.testSupport
del sys
