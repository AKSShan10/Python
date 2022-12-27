courses = {
    "js":"JavaScript 101",
    "python": ["Python 101", 'Python 201'],
    "html":"HTML 101"
}

print(courses.get("js",None))
print(courses.get("cc",None))
print(courses.get("cc","Default text is here"))

if courses.get("css",None):
    print("You are enrolled in CSS 101")