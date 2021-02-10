# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TkCabezal(models.Model):
    terminal = models.IntegerField(db_column='Terminal', primary_key=True)  # Field name made lowercase.
    ticket = models.IntegerField(db_column='Ticket')  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=2, blank=True, null=True)  # Field name made lowercase.
    rollo = models.CharField(db_column='Rollo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    sucursal = models.IntegerField(db_column='Sucursal', blank=True, null=True)  # Field name made lowercase.
    caja = models.IntegerField(db_column='Caja', blank=True, null=True)  # Field name made lowercase.
    cajero = models.IntegerField(db_column='Cajero', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    intereses = models.DecimalField(db_column='Intereses', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    redondeo = models.DecimalField(db_column='Redondeo', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vuelto = models.DecimalField(db_column='Vuelto', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ivamin = models.DecimalField(db_column='IvaMin', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ivabas = models.DecimalField(db_column='IvaBas', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cierrecaja = models.DateTimeField(db_column='CierreCaja', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    autoriza = models.IntegerField(db_column='Autoriza', blank=True, null=True)  # Field name made lowercase.
    fondocap = models.DecimalField(db_column='FondoCap', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(db_column='Vendedor', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='Cliente', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idlista = models.IntegerField(db_column='idLista', blank=True, null=True)  # Field name made lowercase.
    identidad = models.IntegerField(db_column='idEntidad', blank=True, null=True)  # Field name made lowercase.
    idmoneda = models.IntegerField(db_column='idMoneda', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idrut = models.IntegerField(db_column='idRut', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    domicilio = models.CharField(db_column='Domicilio', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idci = models.IntegerField(db_column='idCI', blank=True, null=True)  # Field name made lowercase.
    cotiz = models.DecimalField(db_column='Cotiz', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    femision = models.DateTimeField(db_column='FEmision', blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipodoc = models.IntegerField(db_column='TipoDoc', blank=True, null=True)  # Field name made lowercase.
    numerodoc = models.CharField(db_column='NumeroDoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cotizventa = models.DecimalField(db_column='CotizVenta', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    difcambio = models.DecimalField(db_column='DifCambio', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(max_length=100, blank=True, null=True)
    idtipoaux = models.IntegerField(db_column='idTipoAux', blank=True, null=True)  # Field name made lowercase.
    idcuenta = models.IntegerField(db_column='idCuenta', blank=True, null=True)  # Field name made lowercase.
    tipoventa = models.IntegerField(db_column='TipoVenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tk_cabezal'
        unique_together = (('terminal', 'ticket'),)


class TkDtosrec(models.Model):
    terminal = models.IntegerField(db_column='Terminal', primary_key=True)  # Field name made lowercase.
    ticket = models.IntegerField(db_column='Ticket')  # Field name made lowercase.
    renglon = models.IntegerField(db_column='Renglon')  # Field name made lowercase.
    n = models.IntegerField()
    valoren = models.IntegerField(db_column='ValorEn', blank=True, null=True)  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tk_dtosrec'
        unique_together = (('terminal', 'ticket', 'renglon', 'n'),)


class TkDtosrecGlobales(models.Model):
    terminal = models.IntegerField(db_column='Terminal', primary_key=True)  # Field name made lowercase.
    ticket = models.IntegerField(db_column='Ticket')  # Field name made lowercase.
    renglon = models.IntegerField(db_column='Renglon')  # Field name made lowercase.
    tipomov = models.CharField(db_column='TipoMov', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tipodr = models.IntegerField(db_column='TipoDR', blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taiva = models.CharField(db_column='TaIVA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    importesiniva = models.DecimalField(db_column='ImporteSinIva', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    importeiva = models.DecimalField(db_column='ImporteIva', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tk_dtosrec_globales'
        unique_together = (('terminal', 'ticket', 'renglon'),)


class TkExtintores(models.Model):
    terminal = models.IntegerField(db_column='Terminal', primary_key=True)  # Field name made lowercase.
    ticket = models.IntegerField(db_column='Ticket')  # Field name made lowercase.
    renglon = models.IntegerField(db_column='Renglon')  # Field name made lowercase.
    idmercaderia = models.IntegerField(db_column='idMercaderia', blank=True, null=True)  # Field name made lowercase.
    nextintor = models.IntegerField(db_column='nExtintor')  # Field name made lowercase.
    matricula = models.CharField(db_column='Matricula', max_length=15, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=15, blank=True, null=True)  # Field name made lowercase.
    recarga = models.CharField(db_column='Recarga', max_length=15, blank=True, null=True)  # Field name made lowercase.
    vtorecarga = models.DateTimeField(db_column='VtoRecarga', blank=True, null=True)  # Field name made lowercase.
    vtohidraulica = models.DateTimeField(db_column='VtoHidraulica', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tk_extintores'
        unique_together = (('terminal', 'ticket', 'renglon', 'nextintor'),)


class TkPagos(models.Model):
    terminal = models.IntegerField(db_column='Terminal', primary_key=True)  # Field name made lowercase.
    ticket = models.IntegerField(db_column='Ticket')  # Field name made lowercase.
    renglon = models.IntegerField(db_column='Renglon')  # Field name made lowercase.
    identidad = models.IntegerField(db_column='idEntidad', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pesos = models.DecimalField(db_column='Pesos', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dolares = models.DecimalField(db_column='Dolares', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dato1 = models.CharField(db_column='Dato1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dato2 = models.CharField(db_column='Dato2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dato3 = models.CharField(db_column='Dato3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dato4 = models.CharField(db_column='Dato4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idconvenio = models.IntegerField(db_column='idConvenio', blank=True, null=True)  # Field name made lowercase.
    idplan = models.IntegerField(db_column='idPlan', blank=True, null=True)  # Field name made lowercase.
    cantcuotas = models.IntegerField(db_column='CantCuotas', blank=True, null=True)  # Field name made lowercase.
    intfinan = models.DecimalField(db_column='IntFinan', max_digits=6, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    intereses = models.DecimalField(db_column='Intereses', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tk_pagos'
        unique_together = (('terminal', 'ticket', 'renglon'),)


class TkRenglones(models.Model):
    terminal = models.IntegerField(db_column='Terminal', primary_key=True)  # Field name made lowercase.
    ticket = models.IntegerField(db_column='Ticket')  # Field name made lowercase.
    renglon = models.IntegerField(db_column='Renglon')  # Field name made lowercase.
    idmercaderia = models.IntegerField(db_column='idMercaderia', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=70, blank=True, null=True)  # Field name made lowercase.
    idmoneda = models.IntegerField(db_column='idMoneda', blank=True, null=True)  # Field name made lowercase.
    preventa = models.DecimalField(db_column='PreVenta', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=12, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idsubfamilia = models.IntegerField(db_column='idSubFamilia', blank=True, null=True)  # Field name made lowercase.
    idproveedor = models.IntegerField(db_column='idProveedor', blank=True, null=True)  # Field name made lowercase.
    prereal = models.DecimalField(db_column='PreReal', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taiva = models.CharField(db_column='TaIva', max_length=1, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=1, blank=True, null=True)  # Field name made lowercase.
    idrenglonasociado = models.IntegerField(db_column='idRenglonAsociado', blank=True, null=True)  # Field name made lowercase.
    idaux1 = models.IntegerField(db_column='idAux1', blank=True, null=True)  # Field name made lowercase.
    idaux2 = models.IntegerField(db_column='idAux2', blank=True, null=True)  # Field name made lowercase.
    dtorec = models.DecimalField(db_column='DtoRec', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    rubro = models.CharField(db_column='Rubro', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tk_renglones'
        unique_together = (('terminal', 'ticket', 'renglon'),)


class TkTransact(models.Model):
    terminal = models.IntegerField(primary_key=True)
    ticket = models.IntegerField()
    renglonpago = models.IntegerField(db_column='RenglonPago')  # Field name made lowercase.
    monfactura = models.IntegerField(db_column='MonFactura', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalgravado = models.DecimalField(db_column='TotalGravado', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totaliva = models.DecimalField(db_column='TotalIva', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    montarjeta = models.IntegerField(db_column='MonTarjeta', blank=True, null=True)  # Field name made lowercase.
    imppago = models.DecimalField(db_column='ImpPago', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    operacion = models.CharField(db_column='Operacion', max_length=3, blank=True, null=True)  # Field name made lowercase.
    esconsfinal = models.TextField(db_column='EsConsFinal', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nroautorizacion = models.CharField(db_column='NroAutorizacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transaccionid = models.DecimalField(db_column='TransaccionId', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tarjetaid = models.IntegerField(db_column='TarjetaId', blank=True, null=True)  # Field name made lowercase.
    tarjetatipo = models.CharField(db_column='TarjetaTipo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tarjetacuentaid = models.IntegerField(db_column='TarjetaCuentaid', blank=True, null=True)  # Field name made lowercase.
    facturanro = models.FloatField(db_column='FacturaNro', blank=True, null=True)  # Field name made lowercase.
    tarjetaalimentacion = models.TextField(db_column='TarjetaAlimentacion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tarjetadocidentidad = models.CharField(db_column='TarjetaDocIdentidad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tarjetanombre = models.CharField(db_column='TarjetaNombre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tarjetatitular = models.CharField(db_column='TarjetaTitular', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaccionfechahora = models.DateTimeField(db_column='TransaccionFechaHora', blank=True, null=True)  # Field name made lowercase.
    tarjetaprestaciones = models.TextField(db_column='TarjetaPrestaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tarjetanro = models.CharField(db_column='TarjetaNro', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tickettransact = models.FloatField(db_column='TicketTransact', blank=True, null=True)  # Field name made lowercase.
    cuotas = models.IntegerField(db_column='Cuotas', blank=True, null=True)  # Field name made lowercase.
    plannombre = models.CharField(db_column='PlanNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plannumero = models.IntegerField(db_column='PlanNumero', blank=True, null=True)  # Field name made lowercase.
    decleymonto = models.DecimalField(db_column='DecLeyMonto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    decleyaplicado = models.TextField(db_column='DecLeyAplicado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    decleynro = models.CharField(db_column='DecLeyNro', max_length=20, blank=True, null=True)  # Field name made lowercase.
    decleyvoucher = models.CharField(db_column='DecLeyVoucher', max_length=100, blank=True, null=True)  # Field name made lowercase.
    trnfactgravado = models.DecimalField(db_column='TrnFactGravado', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    firmarvoucher = models.TextField(db_column='FirmarVoucher', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tarjetamedio = models.CharField(db_column='TarjetaMedio', max_length=30, blank=True, null=True)  # Field name made lowercase.
    terminalid = models.CharField(db_column='Terminalid', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lote = models.FloatField(db_column='Lote', blank=True, null=True)  # Field name made lowercase.
    tipocuenta = models.CharField(db_column='TipoCuenta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trniva = models.DecimalField(db_column='TrnIVA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    appname = models.CharField(db_column='AppName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    propina = models.DecimalField(db_column='Propina', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    plantipo = models.IntegerField(db_column='PlanTipo', blank=True, null=True)  # Field name made lowercase.
    decleyid = models.IntegerField(db_column='DecLeyId', blank=True, null=True)  # Field name made lowercase.
    idasacobrar = models.IntegerField(db_column='idAsACobrar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tk_transact'
        unique_together = (('terminal', 'ticket', 'renglonpago'),)


class TkTransactAnulado(models.Model):
    terminal = models.IntegerField(primary_key=True)
    ticket = models.IntegerField()
    transaccionid = models.DecimalField(db_column='TransaccionId', max_digits=12, decimal_places=0)  # Field name made lowercase.
    monfactura = models.IntegerField(db_column='MonFactura', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalgravado = models.DecimalField(db_column='TotalGravado', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totaliva = models.DecimalField(db_column='TotalIva', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    montarjeta = models.IntegerField(db_column='MonTarjeta', blank=True, null=True)  # Field name made lowercase.
    imppago = models.DecimalField(db_column='ImpPago', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    operacion = models.CharField(db_column='Operacion', max_length=3, blank=True, null=True)  # Field name made lowercase.
    esconsfinal = models.TextField(db_column='EsConsFinal', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nroautorizacion = models.CharField(db_column='NroAutorizacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tarjetaid = models.IntegerField(db_column='TarjetaId', blank=True, null=True)  # Field name made lowercase.
    tarjetatipo = models.CharField(db_column='TarjetaTipo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tarjetacuentaid = models.IntegerField(db_column='TarjetaCuentaid', blank=True, null=True)  # Field name made lowercase.
    facturanro = models.FloatField(db_column='FacturaNro', blank=True, null=True)  # Field name made lowercase.
    tarjetaalimentacion = models.TextField(db_column='TarjetaAlimentacion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tarjetadocidentidad = models.CharField(db_column='TarjetaDocIdentidad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tarjetanombre = models.CharField(db_column='TarjetaNombre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tarjetatitular = models.CharField(db_column='TarjetaTitular', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaccionfechahora = models.DateTimeField(db_column='TransaccionFechaHora', blank=True, null=True)  # Field name made lowercase.
    tarjetaprestaciones = models.TextField(db_column='TarjetaPrestaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tarjetanro = models.CharField(db_column='TarjetaNro', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tickettransact = models.FloatField(db_column='TicketTransact', blank=True, null=True)  # Field name made lowercase.
    cuotas = models.IntegerField(db_column='Cuotas', blank=True, null=True)  # Field name made lowercase.
    anula_tickettransact = models.FloatField(db_column='Anula_TicketTransact', blank=True, null=True)  # Field name made lowercase.
    anula_nroautorizacion = models.CharField(db_column='Anula_NroAutorizacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    anula_transaccionid = models.DecimalField(db_column='Anula_TransaccionId', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    anula_usuario = models.IntegerField(db_column='Anula_Usuario', blank=True, null=True)  # Field name made lowercase.
    anula_autoriza = models.IntegerField(db_column='Anula_Autoriza', blank=True, null=True)  # Field name made lowercase.
    anula_fecha = models.DateTimeField(db_column='Anula_Fecha', blank=True, null=True)  # Field name made lowercase.
    plannombre = models.CharField(db_column='PlanNombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plannumero = models.IntegerField(db_column='PlanNumero', blank=True, null=True)  # Field name made lowercase.
    decleymonto = models.DecimalField(db_column='DecLeyMonto', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    decleyaplicado = models.TextField(db_column='DecLeyAplicado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    decleynro = models.CharField(db_column='DecLeyNro', max_length=20, blank=True, null=True)  # Field name made lowercase.
    decleyvoucher = models.CharField(db_column='DecLeyVoucher', max_length=100, blank=True, null=True)  # Field name made lowercase.
    trnfactgravado = models.DecimalField(db_column='TrnFactGravado', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    firmarvoucher = models.TextField(db_column='FirmarVoucher', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tarjetamedio = models.CharField(db_column='TarjetaMedio', max_length=30, blank=True, null=True)  # Field name made lowercase.
    terminalid = models.CharField(db_column='Terminalid', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lote = models.FloatField(db_column='Lote', blank=True, null=True)  # Field name made lowercase.
    tipocuenta = models.CharField(db_column='TipoCuenta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trniva = models.DecimalField(db_column='TrnIVA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    appname = models.CharField(db_column='AppName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    propina = models.DecimalField(db_column='Propina', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanId', blank=True, null=True)  # Field name made lowercase.
    plantipo = models.IntegerField(db_column='PlanTipo', blank=True, null=True)  # Field name made lowercase.
    decleyid = models.IntegerField(db_column='DecLeyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tk_transact_anulado'
        unique_together = (('terminal', 'ticket', 'transaccionid'),)
