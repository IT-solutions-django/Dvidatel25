from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse



class Site: 
    domain = '82.202.128.97' 


class BaseSitemap(Sitemap):
    protocol = 'http' 
    
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(BaseSitemap, self).get_urls(site=site, **kwargs)
    

class HomeViewSitemap(BaseSitemap): 
    priority = 1 

    def items(self): 
        return [
            'home:home',
        ]
    
    def location(self, item):
        return reverse(item)
    

    