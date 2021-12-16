from django.contrib.auth.mixins import UserPassesTestMixin

class StudentMixin(UserPassesTestMixin):
    raise_exception=True

    def test_func(self):
        user=self.request.user
        #print(user.groups.all())
        #return user.groups.all()=='生徒' or user.is_superuser
        #return user.groups.filter(name='生徒') and user.pk == self.kwargs['pk'] or user.is_superuser
        return user.category_type.filter(type_name='生徒') and user.pk == self.kwargs['pk'] or user.is_admin

class TeacherMixin(UserPassesTestMixin):
    raise_exception=True
    def test_func(self):
        user=self.request.user
        #return user.groups.filter(name='先生') and user.pk == self.kwargs['pk'] or user.is_superuser
        return user.category_type.filter(type_name='先生') and user.pk == self.kwargs['pk'] or user.is_admin

class ParentsMixin(UserPassesTestMixin):
    raise_exception=True
    def test_func(self):
        user=self.request.user
        #return user.groups.filter(name='保護者') and user.pk == self.kwargs['pk'] or user.is_superuser
        return user.category_type.filter(type_name='保護者') and user.pk == self.kwargs['pk'] or user.is_admin

class TeacherIndexMixin(UserPassesTestMixin):
    raise_exception=True
    def test_func(self):
        user=self.request.user
        #return user.groups.filter(name='先生') and user.pk == self.kwargs['pk'] or user.is_superuser
        return user.category_type.filter(type_name='先生') or user.is_admin

class StudentIndexMixin(UserPassesTestMixin):
    raise_exception=True
    def test_func(self):
        user=self.request.user
        #return user.groups.filter(name='先生') and user.pk == self.kwargs['pk'] or user.is_superuser
        return user.category_type.filter(type_name='生徒') or user.is_admin