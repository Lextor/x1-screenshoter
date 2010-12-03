from registration.forms import RegistrationFormUniqueEmail
import supercaptcha

class SuperCaptchaForm(RegistrationFormUniqueEmail):    
    captcha = supercaptcha.CaptchaField(label=u'no robots here')
