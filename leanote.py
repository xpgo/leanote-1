#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A library that provides a Python interface to the Leanote API
# Copyright (C) 2017
# Vcinex <i@vcinex.com>

import requests
import json


class leanote(object):
    def __init__(self, name, password, baseUrl="https://leanote.com"):
        self.name = name
        self.password = password
        self.baseUrl = baseUrl
        self.token = None
        self.userId = None
        self.email = None
        self.userName = None
        if self.login()["Ok"]:
            print("Login successed")
        else:
            print("Login failed. Please check you email, password or host")

    def auth(self, Token=None, UserId=None, Email=None, Username=None):
        self.token = Token
        self.userId = UserId
        self.email = Email
        self.userName = Username

    def login(self):
        url = self.baseUrl + "/api/auth/login"
        params = {"email": self.name, "pwd": self.password}
        r = json.loads(requests.get(url, params=params).text)
        self.auth(r["Token"], r["UserId"], r["Email"], r["Username"])
        return r

    def logout(self):
        url = self.baseUrl + "/api/auth/logout"
        params = {"token": self.token}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def info(self):
        url = self.baseUrl + "/api/user/info"
        params = {"token": self.token, "userId": self.userId}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def updateUsername(self, newUsername="Necessary"):
        url = self.baseUrl + "/api/user/updateUsername"
        params = {"token": self.token, "username": newUsername}
        r = json.loads(requests.post(url, params=params).text)
        return r

    def updatePwd(self, newPassword="Necessary"):
        url = self.baseUrl + "/api/user/updateUsername"
        params = {"token": self.token, "username": self.userName, "oldPwd":
            self.password,
                  "pwd": newPassword}
        r = json.loads(requests.post(url, params=params).text)
        return r

    def updateLogo(self, path="Necessary"):
        url = self.baseUrl + "/api/user/updateLogo"
        params = {"token": self.token}
        try:
            files = {'file': open(path, 'rb')}
            r = json.loads(requests.post(url, params=params, files=files).text)
            return r
        except:
            return "Illegal path"

    def getSyncState(self):
        url = self.baseUrl + "/api/user/getSyncState"
        params = {"token": self.token}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def getSyncNotebooks(self, afterUsn="Necessary", maxEntry="Necessary"):
        url = self.baseUrl + "/api/notebook/getSyncNotebooks"
        params = {"token": self.token, "afterUsn": afterUsn,
                  "maxEntry": maxEntry}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def getNotebooks(self):
        url = self.baseUrl + "/api/notebook/getNotebooks"
        params = {"token": self.token}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def addNotebook(self, title="Necessary", seq="Necessary",
                    parentNotebookId=None):
        url = self.baseUrl + "/api/notebook/addNotebook"
        params = {"token": self.token, "title": title,
                  "parentNotebookId": parentNotebookId, "seq": seq}
        keyList = []
        for key in params.keys():
            if params[key] == None:
                keyList.append(key)
        for key in keyList:
            params.pop(key)
        r = json.loads(requests.post(url, params=params).text)
        return r

    def updateNotebook(self, notebookId="Necessary", title="Necessary",
                       seq="Necessary", usn="Necessary",
                       parentNotebookId=None):
        url = self.baseUrl + "/api/notebook/updateNotebook"
        params = {"token": self.token, "notebookId": notebookId,
                  "title": title, "parentNotebookId": parentNotebookId,
                  "seq": seq, "usn": usn}
        keyList = []
        for key in params.keys():
            if params[key] == None:
                keyList.append(key)
        for key in keyList:
            params.pop(key)
        r = json.loads(requests.post(url, params=params).text)
        return r

    def deleteNotebook(self, notebookId="Necessary", usn="Necessary"):
        url = self.baseUrl + "/api/notebook/deleteNotebook"
        params = {"token": self.token, "usn": usn, "notebookId": notebookId}
        r = json.loads(requests.post(url, params=params).text)
        return r

    def getSyncNotes(self, afterUsn="Necessary", maxEntry="Necessary"):
        url = self.baseUrl + "/api/note/getSyncNotes"
        params = {"token": self.token, "afterUsn": afterUsn,
                  "maxEntry": maxEntry}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def getNotes(self, notebookId="Necessary"):
        url = self.baseUrl + "/api/note/getNotes"
        params = {"token": self.token, "notebookId": notebookId}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def getNoteAndContent(self, noteId="Necessary"):
        url = self.baseUrl + "/api/note/getNoteAndContent"
        params = {"token": self.token, "noteId": noteId}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def getNoteContent(self, noteId="Necessary"):
        url = self.baseUrl + "/api/note/getNoteContent "
        params = {"token": self.token, "noteId": noteId}
        r = json.loads(requests.get(url, params=params).text)
        return r

    # Maybe there is something wrong with files uploading, if yes, just don't
    # upload files
    def addNote(self, NotebookId="Necessary", Title="Necessary",
                Content="Necessary", Tags=None, Abstract=None,
                IsMarkdown=None, CreatedTime=None, UpdatedTime=None,
                paths=None):
        url = self.baseUrl + "/api/note/addNote"
        params = {"token": self.token, "NotebookId": NotebookId,
                  "Title": Title, "Tags": Tags, "Content": Content,
                  "Abstract": Abstract,
                  "IsMarkdown": IsMarkdown, "CreatedTime": CreatedTime,
                  "UpdatedTime": UpdatedTime}
        keyList = []
        for key in params.keys():
            if params[key] == None:
                keyList.append(key)
        for key in keyList:
            params.pop(key)
        r = json.loads(requests.post(url, params=params).text)
        return r

    # Maybe there is something wrong with files uploading, if yes, just don't
    # upload files
    def updateNote(self, NoteId="Necessary", Usn="Necessary",
                   NotebookId=None, Title=None, Tags=None, Content=None,
                   Abstract=None, IsMarkdown=None, IsTrash=None,
                   CreatedTime=None, UpdatedTime=None, paths=None):
        url = self.baseUrl + "/api/note/updateNote"
        params = {"token": self.token, "NoteId": NoteId, "Usn": Usn,
                  "NotebookId": NotebookId, "Title": Title,
                  "Tags": Tags, "Content": Content, "Abstract": Abstract,
                  "IsMarkdown": IsMarkdown, "IsTrash": IsTrash,
                  "CreatedTime": CreatedTime, "UpdatedTime": UpdatedTime}
        keyList = []
        for key in params.keys():
            if params[key] == None:
                keyList.append(key)
        for key in keyList:
            params.pop(key)
        r = json.loads(requests.post(url, params=params).text)
        return r

    def deleteTrash(self, noteId="Necessary", usn="Necessary"):
        url = self.baseUrl + "/api/note/deleteTrash"
        params = {"token": self.token, "usn": usn, "notebookId": noteId}
        r = json.loads(requests.post(url, params=params).text)
        return r

    def getSyncTags(self, afterUsn="Necessary", maxEntry="Necessary"):
        url = self.baseUrl + "/api/tag/getSyncTags"
        params = {"token": self.token, "afterUsn": afterUsn,
                  "maxEntry": maxEntry}
        r = json.loads(requests.get(url, params=params).text)
        return r

    def addTag(self, tag="Necessary"):
        url = self.baseUrl + "/api/tag/addTag"
        params = {"token": self.token, "tag": tag}
        r = json.loads(requests.post(url, params=params).text)
        return r

    def deleteTag(self, tag="Necessary"):
        url = self.baseUrl + "/api/tag/deleteTag"
        params = {"token": self.token, "tag": tag}
        r = json.loads(requests.post(url, params=params).text)
        return r

    # Process data yourself, I don't know if it is binary
    def getImage(self, fileId="Necessary"):
        url = self.baseUrl + "/api/file/getImage"
        params = {"token": self.token, "fileId": fileId}
        r = requests.get(url, params=params)
        return r

    # Process data yourself, I don't know if it is binary
    def getAttach(self, fileId="Necessary"):
        url = self.baseUrl + "/api/file/getAttach"
        params = {"token": self.token, "fileId": fileId}
        r = requests.get(url, params=params)
        return r

    # Process data yourself, I don't know if it is binary
    def getAllAttachs(self, noteId="Necessary"):
        url = self.baseUrl + "/api/file/getAllAttachs"
        params = {"token": self.token, "noteId": noteId}
        r = requests.get(url, params=params)
        return r