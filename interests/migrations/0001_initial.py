# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table(u'interests_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'interests', ['Subject'])

        # Adding model 'Book'
        db.create_table(u'interests_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('date_read', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'interests', ['Book'])

        # Adding model 'Membership'
        db.create_table(u'interests_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interests.Subject'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['interests.Book'])),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'interests', ['Membership'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table(u'interests_subject')

        # Deleting model 'Book'
        db.delete_table(u'interests_book')

        # Deleting model 'Membership'
        db.delete_table(u'interests_membership')


    models = {
        u'interests.book': {
            'Meta': {'object_name': 'Book'},
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