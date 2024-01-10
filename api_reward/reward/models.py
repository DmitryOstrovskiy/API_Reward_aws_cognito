from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Wallet(models.Model):
    '''The user wallet holds user token balance
    This address wallet will also be rewarded accordingly '''
    # A wallet address will be created each time user signs up for an account
    # some wallet functionalities will not currently be available until
    # our blockchain is ready hence, their values can be left out blank
    user = models.OneToOneField(User, on_delete=models.SET_NULL,
                                blank=True, null=True)
    wallet_address = models.CharField(max_length=254, blank=True, null=True,
                                      verbose_name='Wallet Address')
    wallet_balance = models.PositiveIntegerField(default=0)
    private_key = models.TextField(blank=True, null=True,
                                   verbose_name='Rrivate Key')
    public_key = models.TextField(blank=True, null=True,
                                  verbose_name='Public Key')
    mnemonic_phrase = models.TextField(blank=True, null=True,
                                       verbose_name='Mnemonic Phrase')

    def __str__(self):
        return self.user.email


class TestCard(models.Model):
    '''A model for adding user test cards
    The reward will be given for adding cards'''
    name = models.TextField(blank=False, null=False,
                            verbose_name='Name of the analysis')
    parameter = models.TextField(blank=False, null=False,
                                 verbose_name='Name of the parameter')
    parameter_value = models.TextField(blank=False, null=False,
                                       verbose_name='Parameter value')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='testcards')

    def __str__(self):
        return self.name
