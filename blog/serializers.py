from rest_framework import serializers
from .models import PostObject, KeyWords, Type


class KeyWordsSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)

    class Meta :
        model = KeyWords
        fields = ["name"]

class PostSerializer(serializers.Serializer): 
    title = serializers.CharField(max_length=500)
    subtitle = serializers.CharField(max_length=500)
    type = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
    content = serializers.CharField(max_length=5000)
    status = serializers.BooleanField()
    keywords_set = KeyWordsSerializer(many=True)

    class Meta :
        model = PostObject
        fields = ["title","subtitle", "type", "content", "status", "keywords_set"]
    
    def create(self, validated_data):        
        
        validated_data["type"] = Type.objects.get(id = validated_data.pop("type"))
        keywords_set = validated_data.pop("keywords_set")
        post = PostObject.objects.create(**validated_data)
        for keyword in keywords_set :  
            try :
                post.keywords_set.add(KeyWords.objects.get(name = keyword.get("name")))
            except KeyWords.DoesNotExist :
                key = KeyWords.objects.create(name = keyword.get("name"))
                key.save()
                post.keywords_set.add(key)
        post.save()
        return post

        

