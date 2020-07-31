from django.db import models


class System(models.Model):
    initials = models.CharField('Initials', max_length=3)
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return '[' + str(self.initials) + ']' + ' ' + str(self.name)


class Port(models.Model):
    connector = models.IntegerField('Connector Port')
    shutdown = models.IntegerField('Shutdown Port')

    def __str__(self):
        return str(self.connector) + '-' + str(self.shutdown)


class Client(models.Model):
    STATUS = (
        ("1", "OK"),
        ("2", "Suspenso"),
        ("3", "Com Problema")
    )
    name = models.CharField('Name', max_length=100)
    link = models.CharField('Link', max_length=100)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE, default=1)
    version = models.DateField('Version')
    status = models.CharField('Status', choices=STATUS, max_length=1, default='1')

    def __str__(self):
        return str(self.name)
