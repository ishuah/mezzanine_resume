from django.shortcuts import render
from django.http import HttpResponse
from models import UserResume, CareerHistory, SkillCategory, Skill, Project, School
from django.contrib.auth.models import User

def index(request):
	resumes = UserResume.objects.all()
	return render(request, 'resume_list.html', { 'resumes': resumes })

def user_resume(request, username=None):
	
	try:
		user = User.objects.get(username=username)
	except:
		return render(request, "error.html", { 'error': "Oops! '"+username+"' Is not among us!" }, status=404)

	try:
		resume = UserResume.objects.get(user=user)
	except:
		return render(request, "error.html", { 'error': username+" doesn't have a resume, yet." }, status=404)

	career_history = CareerHistory.objects.filter(resume=resume).order_by("-from_date")
	skill_category = SkillCategory.objects.filter(resume=resume)
	skills = Skill.objects.filter(resume=resume)
	projects = Project.objects.filter(resume=resume)
	schools = School.objects.filter(resume=resume)

	return render(request, "resume.html", { "resume": resume, "career_history": career_history, "skill_category": skill_category, "skills": skills, "projects": projects, "schools": schools  })
