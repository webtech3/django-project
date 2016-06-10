from django.shortcuts import render, HttpResponse, redirect
import requests
import json
import urllib
from urllib import urlopen
import os
import zipfile
from zipfile import ZipFile

jsonList = []
parsedData = []

def downloadfile(user, repo):
    home_dir = os.path.expanduser('~')
    directory = home_dir + '/Desktop/webtechOpdracht/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    url = 'https://api.github.com/repos/' + user + '/' + repo + '/zipball/master'
    name_file = user + '_' + repo +'.zip'
    save_location = directory + name_file
    urllib.urlretrieve (url, save_location)
    folder = 'C:\Users\Apo\Desktop\webtechOpdracht'
    slash = '\\'
    extension = ".zip"
    os.chdir(folder)
    for item in os.listdir(folder):
        if item.endswith(extension):
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            my_file_name = item.split('.zip')[-2] # take zipfile name. remove the extension
            str_MyName = str(my_file_name) # convert to string
            my_path = folder + slash + str_MyName # concat string to create new folder
            zip_ref.extractall(my_path)# extract file to dir
            zip_ref.close()# close dir
	
def listCommits(user, repo_name):
    req = requests.get('https://api.github.com/repos/' + user + '/' + repo_name + '/commits')
    jsonList.append(json.loads(req.content))

def topTenFiles(user, repo_name):
    jsonListCommits = []
    req = requests.get('https://api.github.com/repos/' + user + '/' + repo_name + '/contributors')
    jsonListCommits.append(json.loads(req.content))

    userData = {}

    for data in jsonListCommits:
        userData["contributions"] = data[0]["contributions"]
        userData["repo_name"] = repo_name
    parsedData.append(userData)

def index(request):
    if request.method == 'POST':
        list_urls = [value for name, value in request.POST.iteritems() if name.startswith('repo_url')]
        for repo_url in list_urls:
            repo_name = repo_url.split('/')[-1]
            user = repo_url.split('/')[-2]
            downloadfile(user, repo_name)
            listCommits(user, repo_name)
            topTenFiles(user, repo_name)
        return lijstrepos(request)
    return render(request, 'githubrepo/lijstbestanden.html')

def lijstbestanden(request):
    global parsedData
    my_data = parsedData
    parsedData = []

    return render(request, 'githubrepo/toptien.html',{'data': my_data})

def lijstrepos(request):
    global jsonList
    repos_list = jsonList
    jsonList = []
    userData = {}
    count = 0
    my_key = ""
    for data in repos_list:
        i = 0
        count = len(data)
        while i < count:
            my_key = data[i]["commit"]["tree"]["url"].split('/')[-4]
            tempString = str(i) + "  " + my_key
            userData[tempString] = data[i]
            i += 1

    return render(request, 'githubrepo/lijstrepos.html',{'data': userData})
