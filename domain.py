from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return 'oh snap, could not obtain domain name' \
				'refer to domain.py, get_domain_name()'


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return 'oh snap, could not obtain sub-domain name' \
				'refer to domain.py, get_sub_domain_name()'
