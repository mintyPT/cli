#!/usr/bin/env python

import urllib



def textBetween(text, token1, token2):
    # Initial point
    iniP = text.find(token1)+len(token1)

    # Final point
    finP = text[iniP:].find(token2)

    # Result
    result = text[iniP:finP+iniP].strip()
    return result



class dontEvenReply(object):

    # Url of the blog
    url = "http://dontevenreply.com/"


    def getLastPostTitle(self):

        source = urllib.urlopen(self.url).read()
        token1 = "<div class='mainpost_header'>"
        token2 = "</div>"

        return textBetween(source, token1, token2)
               
        
title = dontEvenReply().getLastPostTitle()
print 'Don\'t even reply: %s' % (title)