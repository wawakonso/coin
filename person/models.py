# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from core.models import TrackActivity
from core.helpers import generate_sequence, codify_dob, codify_gender, \
                         codify_citizen, checksum
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError

# Create your models here.

class Person(TrackActivity):

    MASCULIN = 'M'
    FEMININ = 'F'
    GENDER = (
        (MASCULIN,'M'),
        (FEMININ,'F')
    )

    prenom = models.CharField(max_length=128, blank=True)
    nom = models.CharField(max_length=128, blank=False)
    postnom = models.CharField(max_length=128, blank=True)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices = GENDER, default=MASCULIN)
    citizen = models.BooleanField(default=True)

    def __str__(self):
        return self.prenom + ' ' + self.nom + ' '+ self.postnom


class Identification(models.Model):

    person = models.OneToOneField(Person, on_delete=models.CASCADE,
                                  primary_key=True)
    id_num = models.CharField(max_length=13, unique=True)
    seq_num = models.CharField(max_length=4, default=generate_sequence())

    def __str__(self):
        return self.person.prenom + ' ' + self.person.nom + ' ' + self.person.postnom

@receiver(post_save, sender=Person)
def generate_id_number(sender, instance, **kwargs):
    if kwargs['created']:
        # Generate IdNum of the register person
        seq_num = generate_sequence()
        citizen_code = codify_citizen(instance.citizen)
        dob_code = codify_dob(instance.dob)
        gender_code = codify_gender(instance.gender)
        cs = int(dob_code + seq_num)
        chsum = checksum(cs)

        try:
            id_num = citizen_code + dob_code + gender_code + seq_num + str(chsum)
            Identification.objects.create(person = instance, id_num = id_num, seq_num = seq_num)
        except IntegrityError as e:
            instance.save()
