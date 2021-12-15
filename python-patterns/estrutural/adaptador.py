class _Telefone:
    def telefonar(self, ddd, numero):
        print(f'ligando para ({ddd}) {numero}')


class _WhatsupApi:
    def call(self, phone):
        '''Phone must be in format +country code and phone number'''
        print(f'Zap Zap call to {phone}')


class WhatupApi2TelefoneAdapter:

    def __init__(self, whats_api):
        self._whats_api = whats_api

    def telefonar(self, ddd, numero):
        return self._whats_api.call(f'+55{ddd}{numero}')


class _TelegramApi:
    def phone_call(self, country_code, phone):
        print(f'Telegram phone call to {country_code} {phone}')


class TelegramParaTelefoneAdapter(_TelegramApi):
    def telefonar(self, ddd, numero):
        self.phone_call('+55', f'{ddd}{numero}')


class TelegramParaTelefoneMixin:
    def telefonar(self, ddd, numero):
        self.phone_call('+55', f'{ddd}{numero}')


class TelegramParaTelefoneAdapter2(TelegramParaTelefoneMixin, _TelegramApi):
    pass


# telefone = WhatupApi2TelefoneAdapter(_WhatsupApi())
# telefone = TelegramParaTelefoneAdapter()
telefone = TelegramParaTelefoneAdapter2()


if __name__ == '__main__':
    # Imagine em mil lugares diferentes
    telefone.telefonar('12', '2345678')
    telefone.telefonar('12', '1454181')