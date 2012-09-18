import urllib2
import lxml.html
from lxml.html.clean import clean_html

class ArticleParser(object):
    """ Appunti Digitali article parser class
    
    Attributes:
        opener: urllib2 url opener
    """
    def __init__(self):
        """ Setup url opener and set friendly user agent """
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        
    def __save_article_to_file(self, content):
        """ Save html string to file """
        with open("article.txt", 'w') as out:
            out.write(content)

    def get_article(self, url):
        """ Download, parse, filter an return post from a given URL
        
        Args:
            url: Article webpage url as string
        Returns:
            A string with parsed and cleaned Article's content 
        """
        response = self.opener.open(url)
        doc = lxml.html.document_fromstring(response.read())
        content = doc.find_class("post")[0]    # Select content by CSS class 
        cleaned_content = clean_html(content)
        str_cleaned_content = lxml.html.tostring(cleaned_content)
        # self.__save_article_to_file(str_cleaned_content)
        return str_cleaned_content
