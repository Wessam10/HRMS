from djoser.serializers import UserSerializer as BaseUserSerializer,          UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer (BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'fullName', 'username', 'password',
                  'phoneNumber', 'birthDate', 'gender',  'emp_date', 'address', "is_hr",  'positions', 'department',  'photo', 'company', 'workdays']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id',  'fullName', 'username', 'password',
                  'email',  'birthDate', 'gender', ]
