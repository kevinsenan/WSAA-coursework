# assignments04-github.py
# Assignment 4. 
# author K Donovan

import requests 
from github import Github
#from the config.py file, import the apikeys dictionary object containing the keys to the variable cfg
from config import apikeys as cfg
#assign the key from the git hub repository to apikey
apikey = cfg["githubkey"]
g = Github(apikey)
#to get the url of the named repository using the apikey in g and assign it to repo
repo = g.get_repo("kevinsenan/mywork")
#get the contents of the text file named in repo and assign it to fileInfo
fileInfo = repo.get_contents("WSAAass4.txt")
#get the url for the text file downloaded into fileInfo, saves copying or typing it out
url_of_file = fileInfo.download_url
#use the url of the file to send the http request to the file and save the text to content_of_file
response = requests.get(url_of_file) 
content_of_file = response.text
#replace the word Andrew with Kevin in content_of_file and assign to contents_updated
contents_updated = content_of_file.replace("Andrew", "Kev") 
#update the contents of the file in Github
gitHubResponse=repo.update_file(fileInfo.path, "update by kev", contents_updated, fileInfo.sha)
print(gitHubResponse)