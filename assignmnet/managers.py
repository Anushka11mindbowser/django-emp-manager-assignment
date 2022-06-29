


from django.contrib.auth.base_user import BaseUserManager



class EmployeeUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email required!")
        if not password:
            raise ValueError("Password required")
        email = self.normalize_email()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_manager(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

    def create_emp(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)


    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'superuser')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff set to True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser set to True')

        if extra_fields.get('role') is not 'is_superuser':
            raise ValueError('The role must be that of superuser')

        return self.create_user(email, password, **extra_fields)
