import cherrypy
import myprocessor


p = myprocessor.MyProcessor()

class MyWebService(object):

  @cherrypy.expose
  @cherrypy.tools.json_out()
  @cherrypy.tools.json_in()
  def getLeaderboard(self):
    data = cherrypy.request.json
    output = p.run(data)
    return output
#
#
# Main
#
#

if __name__ == '__main__':
  config = {'server.socket_host': '0.0.0.0',
            'server.socket_port': 8080}

  cherrypy.config.update(config)
  cherrypy.quickstart(MyWebService())
