# -*- coding: utf-8 -*-
"""
title              :forms
description        :
date               :28.10.16
"""
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Field
from captcha.fields import ReCaptcha

__author__ = 'Vitold Komorovski'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=128,
                           label='Ваше имя',
                           required=True)
    email = forms.EmailField(required=True,
                             label='Ваш email')
    message = forms.CharField(required=True,
                              widget=forms.Textarea,
                              label='Ваше сообщение')
    captcha = ReCaptcha()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'feedback'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_action = '/send_message/'
        self.helper.layout = Layout(
            Field('name', css_class='form-control', wrapper_class="form-group"),
            Field('email', css_class='form-control', wrapper_class="form-group"),
            Field('message', css_class='form-control', wrapper_class="form-group"),
            HTML('<div class="g-recaptcha" data-sitekey="6LfRnAoUAAAAABpcIOkCg5noJw7eDVFnp6QIFFBx"></div>'),
            HTML('<button type="submit"  class="btn btn-white" return false;">Отправить</button>'),

        )