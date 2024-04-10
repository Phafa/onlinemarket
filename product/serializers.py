from rest_framework import serializers
from django.db.models.aggregates import Avg
from .models import Product, ProductReview, ProductRating
from user.models import User

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]

class GetRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ["id","user","rate"]
    user = GetUserSerializer()

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "type", "posted_date", "image"]
    
    def create(self, validated_data):
        user = User.objects.get(id = self.context["user_id"])
        return Product.objects.create(user = user, **validated_data)

class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id","user","title", "description", "price", "type", "posted_date","image","rating"]
    
    rating = serializers.SerializerMethodField(method_name= "rating_calculate")
    user = GetUserSerializer()
    
    def rating_calculate(self,product:Product):
        average = ProductRating.objects.filter(product_id = product.id).aggregate(average=Avg("rate"))
        return average["average"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ["id","user","review", "review_date"]
    
    user = GetUserSerializer()

class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ["id", "review"]
    def create(self, validated_data):
        product_id = self.context["product_id"]
        user = User.objects.get(id = self.context["user_id"])
        return ProductReview.objects.create(product_id= product_id, user = user ,**validated_data)
    
class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ["id", "rate"]
    
    def create(self, validated_data):
        product_id = self.context["product_id"]
        user_id = self.context["user_id"]

        return ProductRating.objects.create(product_id=product_id, user_id=user_id,**validated_data)
