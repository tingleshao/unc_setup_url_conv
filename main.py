url = raw_input().split('http%3A%2F%2F')[1]
new_url = url.replace("%3D", "=")
new_url = new_url.replace("%2F", "/")
new_url = new_url.replace("%3F", "?")
print new_url

