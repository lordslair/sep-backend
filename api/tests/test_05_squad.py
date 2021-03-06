# -*- coding: utf8 -*-

import json
import os
import requests

SEP_URL     = os.environ['SEP_URL']
pjname_test = 'PJTest'
payload     = {'username': 'user@exemple.com', 'password': 'plop'}

def test_singouins_squad_create():
    url      = SEP_URL + '/auth/login'
    response = requests.post(url, json = payload)
    token    = json.loads(response.text)['access_token']
    headers  = json.loads('{"Authorization": "Bearer '+ token + '"}')

    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    pjid     = json.loads(response.text)['payload'][0]['id']

    url       = SEP_URL + '/mypc/{}/squad'.format(pjid)
    payload_s = {"name": 'SquadTest'}
    response  = requests.post(url, json = payload_s, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert response.status_code == 201

def test_singouins_squad_get():
    url      = SEP_URL + '/auth/login'
    response = requests.post(url, json = payload)
    token    = json.loads(response.text)['access_token']
    headers  = json.loads('{"Authorization": "Bearer '+ token + '"}')

    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    pjid     = json.loads(response.text)['payload'][0]['id']
    squadid  = json.loads(response.text)['payload'][0]['squad']

    url      = SEP_URL + '/mypc/{}/squad/{}'.format(pjid,squadid)
    response = requests.get(url, headers=headers)
    squad_r  = json.loads(response.text)['payload']['members'][0]['squad_rank']

    assert squad_r == 'Leader'
    assert json.loads(response.text)['success'] == True
    assert response.status_code == 200

def test_singouins_squad_invite():
    url      = SEP_URL + '/auth/login'
    response = requests.post(url, json = payload)
    token    = json.loads(response.text)['access_token']
    headers  = json.loads('{"Authorization": "Bearer '+ token + '"}')

    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    pjid     = json.loads(response.text)['payload'][0]['id']
    squadid  = json.loads(response.text)['payload'][0]['squad']

    url      = SEP_URL + '/mypc/{}/squad/{}/invite/{}'.format(pjid,squadid,'1')
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == False
    assert 'already in a squad' in json.loads(response.text)['msg']
    assert response.status_code == 200

def test_singouins_squad_kick():
    url      = SEP_URL + '/auth/login'
    response = requests.post(url, json = payload)
    token    = json.loads(response.text)['access_token']
    headers  = json.loads('{"Authorization": "Bearer '+ token + '"}')

    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    pjid     = json.loads(response.text)['payload'][0]['id']
    squadid  = json.loads(response.text)['payload'][0]['squad']

    # We create a PJTestSquadKick
    url      = SEP_URL + '/mypc'
    response = requests.post(url, json = {'race': '3', 'name': 'PJTestSquadKick'}, headers=headers)
    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    targetid = json.loads(response.text)['payload'][1]['id']

    # We invite PJTestSquadKick
    url      = SEP_URL + '/mypc/{}/squad/{}/invite/{}'.format(pjid,squadid,targetid)
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert 'PC successfully invited' in json.loads(response.text)['msg']
    assert response.status_code == 201

    # We kick PJTestSquadKick
    url      = SEP_URL + '/mypc/{}/squad/{}/kick/{}'.format(pjid,squadid,targetid)
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert 'PC successfully kicked' in json.loads(response.text)['msg']
    assert response.status_code == 201

    # We cleanup the PJTestSquadKick
    url      = SEP_URL + '/mypc/{}'.format(targetid)
    response = requests.delete(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert response.status_code == 200

def test_singouins_squad_accept():
    url      = SEP_URL + '/auth/login'
    response = requests.post(url, json = payload)
    token    = json.loads(response.text)['access_token']
    headers  = json.loads('{"Authorization": "Bearer '+ token + '"}')

    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    pjid     = json.loads(response.text)['payload'][0]['id']
    squadid  = json.loads(response.text)['payload'][0]['squad']

    # We create a PJTestSquadAccept
    url      = SEP_URL + '/mypc'
    response = requests.post(url, json = {'race': '3', 'name': 'PJTestSquadAccept'}, headers=headers)
    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    targetid = json.loads(response.text)['payload'][1]['id']

    # We invite PJTestSquadAccept
    url      = SEP_URL + '/mypc/{}/squad/{}/invite/{}'.format(pjid,squadid,targetid)
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert 'PC successfully invited' in json.loads(response.text)['msg']
    assert response.status_code == 201

    # PJTestSquadAccept accepts the request
    url      = SEP_URL + '/mypc/{}/squad/{}/accept'.format(targetid,squadid)
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert 'PC successfully accepted squad invite' in json.loads(response.text)['msg']
    assert response.status_code == 201

    # We cleanup the PJTestSquadAccept
    url      = SEP_URL + '/mypc/{}'.format(targetid)
    response = requests.delete(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert response.status_code == 200

def test_singouins_squad_decline():
    url      = SEP_URL + '/auth/login'
    response = requests.post(url, json = payload)
    token    = json.loads(response.text)['access_token']
    headers  = json.loads('{"Authorization": "Bearer '+ token + '"}')

    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    pjid     = json.loads(response.text)['payload'][0]['id']
    squadid  = json.loads(response.text)['payload'][0]['squad']

    # We create a PJTestSquadDecline
    url      = SEP_URL + '/mypc'
    response = requests.post(url, json = {'race': '3', 'name': 'PJTestSquadDecline'}, headers=headers)
    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    targetid = json.loads(response.text)['payload'][1]['id']

    # We invite PJTestSquadDecline
    url      = SEP_URL + '/mypc/{}/squad/{}/invite/{}'.format(pjid,squadid,targetid)
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert 'PC successfully invited' in json.loads(response.text)['msg']
    assert response.status_code == 201

    # PJTestSquadDecline declines the request
    url      = SEP_URL + '/mypc/{}/squad/{}/decline'.format(targetid,squadid)
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert 'PC successfully declined squad invite' in json.loads(response.text)['msg']
    assert response.status_code == 201

    # We cleanup the PJTestSquadDecline
    url      = SEP_URL + '/mypc/{}'.format(targetid)
    response = requests.delete(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert response.status_code == 200

def test_singouins_squad_leave():
    url      = SEP_URL + '/auth/login'
    response = requests.post(url, json = payload)
    token    = json.loads(response.text)['access_token']
    headers  = json.loads('{"Authorization": "Bearer '+ token + '"}')

    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    pjid     = json.loads(response.text)['payload'][0]['id']
    squadid  = json.loads(response.text)['payload'][0]['squad']

    # We create a PJTestSquadLeave
    url      = SEP_URL + '/mypc'
    response = requests.post(url, json = {'race': '3', 'name': 'PJTestSquadLeave'}, headers=headers)
    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    targetid = json.loads(response.text)['payload'][1]['id']

    # We invite PJTestSquadLeave
    url      = SEP_URL + '/mypc/{}/squad/{}/invite/{}'.format(pjid,squadid,targetid)
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert 'PC successfully invited' in json.loads(response.text)['msg']
    assert response.status_code == 201

    # PJTestSquadLeave accepts the request
    url      = SEP_URL + '/mypc/{}/squad/{}/leave'.format(targetid,squadid)
    response = requests.post(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert 'PC successfully left' in json.loads(response.text)['msg']
    assert response.status_code == 201

    # We cleanup the PJTestSquadLeave
    url      = SEP_URL + '/mypc/{}'.format(targetid)
    response = requests.delete(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert response.status_code == 200

def test_singouins_squad_delete():
    url      = SEP_URL + '/auth/login'
    response = requests.post(url, json = payload)
    token    = json.loads(response.text)['access_token']
    headers  = json.loads('{"Authorization": "Bearer '+ token + '"}')

    url      = SEP_URL + '/mypc'
    response = requests.get(url, headers=headers)
    pjid     = json.loads(response.text)['payload'][0]['id']
    squadid  = json.loads(response.text)['payload'][0]['squad']

    url      = SEP_URL + '/mypc/{}/squad/{}'.format(pjid,squadid)
    response = requests.delete(url, headers=headers)

    assert json.loads(response.text)['success'] == True
    assert response.status_code == 200
