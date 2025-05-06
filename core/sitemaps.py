from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse



class Site: 
    domain = 'eldvidatel25.ru' 


class BaseSitemap(Sitemap):
    protocol = 'https' 
    
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
    

    