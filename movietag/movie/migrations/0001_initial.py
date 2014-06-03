# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'movie_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title_aka', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('title_eng', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('title_url', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=-1, null=True)),
            ('running_time', self.gf('django.db.models.fields.IntegerField')(default=-1, null=True)),
            ('released_at', self.gf('django.db.models.fields.DateField')(null=True)),
            ('re_released_at', self.gf('django.db.models.fields.DateField')(null=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('other_rating', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('poster_big', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('stillcut_big', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('unique_id', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('main_genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Genre'], null=True)),
        ))
        db.send_create_signal(u'movie', ['Movie'])

        # Adding M2M table for field sub_genre_set on 'Movie'
        m2m_table_name = db.shorten_name(u'movie_movie_sub_genre_set')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movie.movie'], null=False)),
            ('genre', models.ForeignKey(orm[u'movie.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'genre_id'])

        # Adding model 'Genre'
        db.create_table(u'movie_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'movie', ['Genre'])

        # Adding model 'Tag'
        db.create_table(u'movie_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'movie', ['Tag'])

        # Adding M2M table for field movie_set on 'Tag'
        m2m_table_name = db.shorten_name(u'movie_tag_movie_set')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'movie.tag'], null=False)),
            ('movie', models.ForeignKey(orm[u'movie.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'movie_id'])

        # Adding M2M table for field like_user on 'Tag'
        m2m_table_name = db.shorten_name(u'movie_tag_like_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'movie.tag'], null=False)),
            ('account', models.ForeignKey(orm[u'account.account'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'account_id'])

        # Adding model 'Frequency'
        db.create_table(u'movie_frequency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Tag'])),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'], null=True)),
            ('freq', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'movie', ['Frequency'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'movie_movie')

        # Removing M2M table for field sub_genre_set on 'Movie'
        db.delete_table(db.shorten_name(u'movie_movie_sub_genre_set'))

        # Deleting model 'Genre'
        db.delete_table(u'movie_genre')

        # Deleting model 'Tag'
        db.delete_table(u'movie_tag')

        # Removing M2M table for field movie_set on 'Tag'
        db.delete_table(db.shorten_name(u'movie_tag_movie_set'))

        # Removing M2M table for field like_user on 'Tag'
        db.delete_table(db.shorten_name(u'movie_tag_like_user'))

        # Deleting model 'Frequency'
        db.delete_table(u'movie_frequency')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'null': 'True', 'to': u"orm['account.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'movie.frequency': {
            'Meta': {'object_name': 'Frequency'},
            'freq': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Movie']", 'null': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Tag']"})
        },
        u'movie.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'movie.movie': {
            'Meta': {'object_name': 'Movie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Genre']", 'null': 'True'}),
            'other_rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'poster_big': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            're_released_at': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'released_at': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'running_time': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True'}),
            'stillcut_big': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sub_genre_set': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sub_genre'", 'symmetrical': 'False', 'to': u"orm['movie.Genre']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_aka': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title_eng': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title_url': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'movie.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like_user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['account.Account']", 'symmetrical': 'False'}),
            'movie_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.Movie']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['movie']