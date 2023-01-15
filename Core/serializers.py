from djoser.serializers import UserSerializer as BaseUserSerializer,          UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer (BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id',  'full_name', 'username', 'password',
                  'email', 'phone_number', 'birth_date', 'gender', 'emp_date', 'address', "is_hr", "salary", 'positions', 'department']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
