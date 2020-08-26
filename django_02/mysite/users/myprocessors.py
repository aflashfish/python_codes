from .models import User


# 保持登录状态
def front_user(request):
    user_id = request.session.get('user_id')
    # context返回为{}时，表示没有登录
    context = {}
    if user_id:
        try:
            user = User.objects.get(pk=user_id)
            context['front_user'] = user
        except:
            pass
    return context
