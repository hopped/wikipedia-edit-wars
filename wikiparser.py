import xml.sax.handler

__author__ = 'Dennis Hoppe (hoppe.dennis@ymail.com)'


class WikiArticle(object):
  title = ""
  id = 0
  revisions = []


class WikiRevision(object):
  timestamp = ""
  username = ""
  userid = 0
  revid = 0
  comment = ""
  text = ""


class WikiParser(xml.sax.handler.ContentHandler):

  def __init__(self):
    self.wikiArticle = WikiArticle()
    self.wikiRevision = WikiRevision()
    self.inPage = 0
    self.inTitle = 0
    self.inRevision = 0
    self.inText = 0
    self.inId = 0
    self.inUsername = 0
    self.inContributor = 0
    self.inTimestamp = 0
    self.inComment = 0

  def startElement(self, name, attributes):
    self.buffer = ""
    if name == "page":
      self.inPage = 1
    elif name == "title":
      self.inTitle = 1
    elif name == "revision":
      self.inRevision = 1
      self.wikiRevision = WikiRevision()
    elif name == "username":
      self.inUsername = 1
    elif name == "contributor":
      self.inContributor = 1
    elif name == "text":
      self.inText == 1
    elif name == "id":
      self.inId = 1
    elif name == "timestamp":
      self.inTimestamp = 1
    elif name == "comment":
      self.inComment = 1

  def characters(self, data):
    self.buffer += data

  def endElement(self, name):
    if name == "page":
      self.inPage = 0
    elif name == "title":
      self.inTitle = 0
      self.wikiArticle.title = self.buffer
    elif name == "revision":
      self.inRevision = 0
      self.wikiArticle.revisions.append(self.wikiRevision)
    elif name == "username":
      self.inUsername = 0
      self.wikiRevision.username = self.buffer
    elif name == "contributor":
      self.inContributor = 0
    elif name == "id":
      self.id = 0
      if self.inRevision:
        if self.inContributor:
          self.wikiRevision.userid = self.buffer
        else:
          self.wikiRevision.revid = self.buffer
      else:
        self.wikiArticle.id = self.buffer
        print self.buffer
    elif name == "text":
      self.inText == 0
      self.wikiRevision.text = self.buffer
    elif name == "timestamp":
      self.inTimestamp == 0
      self.wikiRevision.timestamp = self.buffer
    elif name == "comment":
      self.inComment = 0
      self.wikiRevision.comment = self.buffer
