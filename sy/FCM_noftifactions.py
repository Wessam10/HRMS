import jwt
# Token generated by simple-jwt-django-rest-framework or any
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4MjkyMjU3LCJpYXQiOjE2NzgyMDU4NTcsImp0aSI6ImVkMDJmNjQ0MzgwYjQ4M2Q4MDk1NThmMjgzNDY0MGZkIiwidXNlcl9pZCI6NCwiaXNfaHIiOmZhbHNlfQ.WqZzJqStj5_-P76gpBecK0XnTVCY3sgCkTc20l5ztnY"

print(jwt.decode(
    token, 'django-insecure-n-a#1$yi9wm05*4lkkjb4axb0xl*o(c+7ti4@xe!cw+am+u7o4', algorithms=["HS256"]))
