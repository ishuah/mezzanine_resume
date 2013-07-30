# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserResume'
        db.create_table(u'mezzanine_resume_userresume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short_description', self.gf('mezzanine.core.fields.RichTextField')()),
            ('photo', self.gf('mezzanine.core.fields.FileField')(max_length=255)),
        ))
        db.send_create_signal(u'mezzanine_resume', ['UserResume'])

        # Adding model 'CareerHistory'
        db.create_table(u'mezzanine_resume_careerhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mezzanine_resume.UserResume'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('mezzanine.core.fields.RichTextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('logo', self.gf('mezzanine.core.fields.FileField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'mezzanine_resume', ['CareerHistory'])

        # Adding model 'SkillCategory'
        db.create_table(u'mezzanine_resume_skillcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mezzanine_resume.UserResume'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mezzanine_resume', ['SkillCategory'])

        # Adding model 'Skill'
        db.create_table(u'mezzanine_resume_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mezzanine_resume.UserResume'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mezzanine_resume.SkillCategory'])),
        ))
        db.send_create_signal(u'mezzanine_resume', ['Skill'])

        # Adding model 'Project'
        db.create_table(u'mezzanine_resume_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mezzanine_resume.UserResume'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('mezzanine.core.fields.RichTextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255)),
        ))
        db.send_create_signal(u'mezzanine_resume', ['Project'])

        # Adding model 'School'
        db.create_table(u'mezzanine_resume_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mezzanine_resume.UserResume'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('qualification_attained', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year_started', self.gf('django.db.models.fields.DateField')()),
            ('year_completed', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'mezzanine_resume', ['School'])


    def backwards(self, orm):
        # Deleting model 'UserResume'
        db.delete_table(u'mezzanine_resume_userresume')

        # Deleting model 'CareerHistory'
        db.delete_table(u'mezzanine_resume_careerhistory')

        # Deleting model 'SkillCategory'
        db.delete_table(u'mezzanine_resume_skillcategory')

        # Deleting model 'Skill'
        db.delete_table(u'mezzanine_resume_skill')

        # Deleting model 'Project'
        db.delete_table(u'mezzanine_resume_project')

        # Deleting model 'School'
        db.delete_table(u'mezzanine_resume_school')


    models = {
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
        u'mezzanine_resume.careerhistory': {
            'Meta': {'object_name': 'CareerHistory'},
            'description': ('mezzanine.core.fields.RichTextField', [], {}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'logo': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mezzanine_resume.UserResume']"}),
            'to_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mezzanine_resume.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mezzanine_resume.UserResume']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mezzanine_resume.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qualification_attained': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mezzanine_resume.UserResume']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_completed': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'year_started': ('django.db.models.fields.DateField', [], {})
        },
        u'mezzanine_resume.skill': {
            'Meta': {'object_name': 'Skill'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mezzanine_resume.SkillCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mezzanine_resume.UserResume']"})
        },
        u'mezzanine_resume.skillcategory': {
            'Meta': {'object_name': 'SkillCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mezzanine_resume.UserResume']"})
        },
        u'mezzanine_resume.userresume': {
            'Meta': {'object_name': 'UserResume'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('mezzanine.core.fields.FileField', [], {'max_length': '255'}),
            'short_description': ('mezzanine.core.fields.RichTextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['mezzanine_resume']