# -*- coding: utf-8 -*-
import httplib2
import base64
from xmlrpc import client as xmlrpclib

ticket = {
    'summary': '2. new Ticket via API simple',
    'description': 'nice desc',
    'priority': None,
    'assigned': None,
}
rpc_srv = xmlrpclib.ServerProxy('http://admin:admin@192.168.33.11/rpc/', allow_none=True, use_datetime=True)
info = rpc_srv.ticket.createSimple(ticket, True)

print('ticket created #%s' % info[0])

h = httplib2.Http()
headers = {
   'User-Agent': 'miadi',
   'Authorization': 'Basic YWRtaW46YWRtaW4=',
   'content-type': 'text/plain',
}
(resp, content) = h.request("http://192.168.33.11/tickets/upload/%s/?filename=test.txt" % info[0],
                            "PUT", body="This is text",
                            headers=headers)
print(resp)
