from distutils.command.upload import upload
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel

class EmailExtract(models.Model):
    email = models.CharField(max_length=100000, verbose_name=_('email'),default=False, null=True,blank=True)

    class Meta:
        indexes = [models.Index(fields=['email' ]),]
    
    def __str__(self):
        return 'id - {}, - emails {}'.format(self.id, self.email)


class NumberExtract(models.Model):
    phone = models.IntegerField(verbose_name=_('phone'), default=False, null=True,blank=True)

    class Meta:
        indexes = [models.Index(fields=['phone' ]),]
    
    def __str__(self):
        return 'id - {}, - phone {}'.format(self.id, self.phone)

class DomainExtract(models.Model):
    link = models.CharField(max_length=300, verbose_name=_('link'),default=False, null=True,blank=True)

    class Meta:
        indexes = [models.Index(fields=['link' ]),]
    
    def __str__(self):
        return 'id - {}, - link {}'.format(self.id, self.link)


class ImageToText(models.Model):
    image = models.ImageField(upload_to ='uploads/', verbose_name=_('image'))

    class Meta:
        indexes = [models.Index(fields=['image' ]),]
    
    def __str__(self):
        return 'id - {}, - image {}'.format(self.id, self.image)


class ArticleCategory(models.Model):
    category=models.CharField(max_length=100, verbose_name=_('category'),default=False,null=True,blank=True)
    keyword=models.CharField(max_length=100, verbose_name=_('keyword'),default=False, null=True,blank=True)
    class Meta:
        indexes = [models.Index(fields=['category' ]),]
    
    def __str__(self):
        return 'id - {}, - category {}'.format(self.id, self.category)

class AutomaticArticle(models.Model):
    category = models.ForeignKey(to='tools.ArticleCategory', verbose_name=_('category'),default=False, related_name='contacts',
                                    on_delete=models.CASCADE)
    article = models.CharField(max_length=300, verbose_name=_('article'),default=False, null=True,blank=True)

    class Meta:
        indexes = [models.Index(fields=['article' ]),]
    
    def __str__(self):
        return 'id - {}, - category {}'.format(self.id, self.category)