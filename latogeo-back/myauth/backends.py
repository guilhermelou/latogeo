from myauth.models import MyUser

class MyUserAuth(object):
	""" A simple backend to authenticate this user."""
	def authenticate(self, username=None, password=None):
		try:
			user = MyUser.objects.get(email=username)
			if user.check_password(password):
				return user
			return None
		except MyUser.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			user = MyUser.objects.get(pk=user_id)
			if user.is_active:
				return user
			return None
		except MyUser.DoesNotExist:
			return None

class MyUserAuthIdHash(object):
	""" A simple backend to authenticate this user."""
	def authenticate(self, id=None, hash=None):
		try:
			user = MyUser.objects.get(id=id)
			if user.confirmation_key_str() == hash:
				return user
			return None
		except MyUser.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			user = MyUser.objects.get(pk=user_id)
			if user.is_active:
				return user
			return None
		except MyUser.DoesNotExist:
			return None

