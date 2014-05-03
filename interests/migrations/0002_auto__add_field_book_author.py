# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.author'
        db.add_column(u'interests_book', 'author',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.author'
        db.delete_column(u'interests_book', 'author')


    models = {
        u'interests.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'date_read': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'subject': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['interests.Subject']", 'through': u"orm['interests.Membership']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'interests.membership': {
            'Meta': {'object_name': 'Membership'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['interests.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['interests.Subject']"})
        },
        u'interests.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['interests']