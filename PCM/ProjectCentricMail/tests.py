from django.test import TestCase,Client
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ProjectCentricMail.forms import SignUpForm
from ProjectCentricMail.caller import gmail_read
from ProjectCentricMail.auto import run
from ProjectCentricMail.merge import mer
from ProjectCentricMail.models import MessageInfo,ProjectClassify,ProjectNames
from ProjectCentricMail.sort import read
from ProjectCentricMail.formalinformal import PCM_formalinformal
import csv
import os
# Create your tests here.
class ProjectCentricMailCase(TestCase):

	def setUp(self):
		user = User.objects.create_user(username='ayushbansal323',
                                 email='ayushbansal323@gmail.com',
                                 password='a1as2sd3d')
		user.save()
		user = User.objects.create_user(username='ayushbansal321',
                                 email='ayushbansal323@gmail.com',
                                 password='a1as2sd3d')
		user.save()
		project=ProjectNames.objects.create(username='ayushbansal323',projectname = "cn")
		project.save()
		project=ProjectNames.objects.create(username='ayushbansal323',projectname = "dbms")
		project.save()

	def test_login(self):
		c = Client()
		response = c.post('/login', {'username': 'ayushbansal323', 'password': 'a1as2sd3d'})
		self.assertEqual(response.status_code, 302)

	def test_invalid_login(self):
		c = Client()
		response2 = c.post('/login', {'username': 'ayushbansal323', 'password': 'a1assd3d'})
		self.assertEqual(response2.status_code, 200)
		self.assertEqual(response2.context['message'], "Invalid credentials.")

	def test_Spam(self):
		c = Client()
		response0=c.post('/login', {'username': 'ayushbansal323', 'password': 'a1as2sd3d'})
		self.assertEqual(response0.status_code, 302)
		response = c.get('/spam')	
		self.assertEqual(response.status_code, 200)

	def test_FormalInformal(self):
		c = Client()
		response0=c.post('/login', {'username': 'ayushbansal323', 'password': 'a1as2sd3d'})
		self.assertEqual(response0.status_code, 302)
		response = c.get('/formalinformal')	
		self.assertEqual(response.status_code, 200)

	def test_Project(self):
		c = Client()
		response0=c.post('/login', {'username': 'ayushbansal323', 'password': 'a1as2sd3d'})
		self.assertEqual(response0.status_code, 302)
		response = c.post('/project', {'projectname':'toc'})	
		self.assertEqual(response.status_code, 200)
		response2 = c.get('/project/cn')
		self.assertEqual(response2.status_code, 200)

	def test_logout(self):
		c = Client()
		response0=c.post('/login', {'username': 'ayushbansal323', 'password': 'a1as2sd3d'})
		self.assertEqual(response0.status_code, 302)
		response = c.get('/logout')	
		self.assertEqual(response.status_code, 200)
		
	def test_delete(self):
		c = Client()
		response0=c.post('/login', {'username': 'ayushbansal323', 'password': 'a1as2sd3d'})
		self.assertEqual(response0.status_code, 302)
		response = c.get('/delete')	
		self.assertEqual(response.status_code, 200)
