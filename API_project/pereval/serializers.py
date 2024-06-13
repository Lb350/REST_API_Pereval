from rest_framework import serializers
from .models import User, Coord, Level, Image, PerevalAdded
from drf_writable_nested import WritableNestedModelSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']

    def save(self, **kwargs):
        self.is_valid()
        user = User.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            new_user = User.objects.create(
                email=self.validated_data.get('email'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
                phone=self.validated_data.get('phone'),
            )
            return new_user


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'spring', 'summer', 'autumn', ]


class ImageSerializer(serializers.ModelSerializer):
    data = serializers.CharField()

    class Meta:
        model = Image
        fields = ['data', 'title']


class PerevalAddedSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    coord = CoordSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)
    status = serializers.CharField()

    class Meta:
        model = PerevalAdded
        fields = ['id', 'status', 'beauty_title', 'title', 'other_title', 'connect', 'add_time', 'user', 'coord',
                  'level', 'images']

    def create(self, validated_data, **kwargs):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coord')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')

        user, created = User.objects.get_or_create(**user_data)
        coord = Coord.objects.create(**coord_data)
        level = Level.objects.create(**level_data)

        pereval = PerevalAdded.objects.create(user=user, coord=coord, level=level, **validated_data)

        for image_data in images_data:
            Image.objects.create(**image_data, pereval=pereval)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.email != data_user['email'],
                instance_user.fam != data_user['fam'],
                instance_user.name != data_user['name'],
                instance_user.otc != data_user['otc'],
                instance_user.phone != data_user['phone']
            ]
            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено': 'Невозможно изменить данные пользователя'})
        return data