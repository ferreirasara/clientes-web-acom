from django.db import models
from django.db.models import signals


class Server(models.Model):
    name = models.CharField('Name', max_length=100)
    acomServer = models.BooleanField('Acom Server')

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField('Title', max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.title


class System(models.Model):
    initials = models.CharField('Initials', max_length=3)
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return '[' + str(self.initials) + ']' + ' ' + str(self.name)


def system_pre_save(signal, instance, sender, **kwargs):
    instance.initials = instance.initials.upper()


signals.pre_save.connect(system_pre_save, sender=System)


class Port(models.Model):
    STATUS = (
        (1, "Livre"),
        (2, "Em Uso")
    )
    connector = models.IntegerField('Connector Port')
    shutdown = models.IntegerField('Shutdown Port')
    status = models.IntegerField('Status', choices=STATUS, default=1)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.server.name) + ' ' + str(self.connector) + '-' + str(self.shutdown)


class Client(models.Model):
    STATUS = (
        ("1", "Ativo"),
        ("2", "Suspenso"),
        ("3", "Com Erro")
    )
    name = models.CharField('Name', max_length=100)
    link = models.CharField('Link', max_length=100)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE, default=1)
    version = models.DateField('Version')
    status = models.CharField('Status', choices=STATUS, max_length=1, default='1')

    def __str__(self):
        return str(self.name)
