from django.contrib.auth.mixins import UserPassesTestMixin

class GroupMixin(UserPassesTestMixin):
    raise_exception=True

    def test_func(self):
        user=self.request.user
        #print(user.groups.all())
        #return user.groups.all()=='生徒' or user.is_superuser
        return user.groups.filter(name='生徒') and user.pk == self.kwargs['pk'] or user.is_superuser