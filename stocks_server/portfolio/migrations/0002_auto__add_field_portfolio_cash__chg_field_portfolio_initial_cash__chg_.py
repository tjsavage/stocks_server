# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Portfolio.cash'
        db.add_column('portfolio_portfolio', 'cash', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=15, decimal_places=5), keep_default=False)

        # Changing field 'Portfolio.initial_cash'
        db.alter_column('portfolio_portfolio', 'initial_cash', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=5))

        # Changing field 'Position.shares'
        db.alter_column('portfolio_position', 'shares', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=5))


    def backwards(self, orm):
        
        # Deleting field 'Portfolio.cash'
        db.delete_column('portfolio_portfolio', 'cash')

        # Changing field 'Portfolio.initial_cash'
        db.alter_column('portfolio_portfolio', 'initial_cash', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=5))

        # Changing field 'Position.shares'
        db.alter_column('portfolio_position', 'shares', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=5))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portfolio.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'cash': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '5'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_cash': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'portfolio.position': {
            'Meta': {'object_name': 'Position'},
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Portfolio']"}),
            'shares': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '5'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['portfolio']
