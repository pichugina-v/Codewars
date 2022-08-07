def domain_name(url):
    if '//' in url:
        domains = url.split('//')[1].split('/')[0].split('.')
    else:
        domains = url.split('/')[0].split('.')
    if 'www' in domains:
        return domains[1]
    return domains[0]
