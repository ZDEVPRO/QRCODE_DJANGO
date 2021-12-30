from home.models import Qrcode


def qrcode(request):
    qr_code_img = Qrcode.objects.all().order_by('-id')
    context = {
        'qr_code_img': qr_code_img,
    }
    return context
