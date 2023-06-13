#esto para el programa de p8 donde guardamos el tiempo transcurrido en una variable varchar
#import mysql.connector
import pymysql

class Operacion:

    def abrir(self):
   #     conexion=mysql.connector.connect(host="localhost",
    #                                          user="root",
     #                                         passwd="RG980320",
      #                                        database="Parqueadero1")
        conexion = pymysql.connect(host="localhost",
                           user="Aurelio",
                           passwd="RG980320",
                           database="Parqueadero1")
        return conexion


    def altaRegistroRFID(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into Entradas(Entrada, CorteInc, Placas) values (%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def guardacobro(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        #print(TipoPromocion)
        sql = "update Entradas set vobo = %s, Importe = %s, TiempoTotal = %s, Entrada = %s, Salida = %s,TarifaPreferente = %s, QRPromo = %s where id = %s;"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    #Se agrega Función para validar que la promoción no se aplique doble 15ago22
    def ValidaPromo(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id from Entradas where QRPromo = %s "
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()  


    def BolconCobro(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Importe, Salida, TiempoTotal from Entradas where id=%s"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()  
    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Entrada, Salida from Entradas where id=%s"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id, Entrada, Salida from Entradas"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def recuperar_sincobro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id, Entrada, Salida, Importe from Entradas where CorteInc = 0 and Importe is not null "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def desglose_cobrados(self,Numcorte):
    #def desglose_cobrados(self):            
        cone=self.abrir()
        cursor=cone.cursor()
        #sql="SELECT TarifaPreferente,Entrada,id, Count(*) as cuantos FROM Entradas where Entrada >'2020-08-31 23:59:59' AND Entrada < '2020-09-31 23:59:59'AND TarifaPreferente = 'ADMIN' "
        sql="SELECT Count(*),TarifaPreferente,Importe, Count(*)*Importe  as cuantos FROM Entradas where CorteInc = %s GROUP BY TarifaPreferente,Importe;"
        #sql="SELECT TarifaPreferente,Importe, Count(*) as cuantos FROM Entradas where CorteInc = 6 "
        #"SELECT column1 * column2 FROM tablename;
        #sql="select id, Entrada, Salida, Importe from Entradas where CorteInc = 0 and Importe is not null "
        #cursor.execute(sql)
        cursor.execute(sql,Numcorte)
        cone.close()
        return cursor.fetchall()
    def Autos_dentro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id, Entrada, Placas from Entradas where CorteInc = 0 and Importe is null and Salida is null "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def CuantosAutosdentro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select count(*) from Entradas where CorteInc = 0 and Importe is null and Salida is null "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def Quedados_Sensor(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Quedados from Cortes where Folio=%s"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def NumBolQued(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select NumBolQued from Cortes where Folio=%s"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()
    def EntradasSensor(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select EntSens from AccesosSens where Folio=1"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def SalidasSensor(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select SalSens from AccesosSens where Folio=1"
       #sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def CuantosBoletosCobro(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select count(*) from Entradas where CorteInc = 0 and Importe is not null and Salida is not null "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def BEDCorte(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select count(*) from Entradas where ((vobo is null and TarifaPreferente is null) or (vobo = 'lmf' and TarifaPreferente = ''))"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def BAnteriores(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select count(*) from Entradas where vobo = 'ant' "
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def corte(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select sum(importe) from Entradas where CorteInc = 0"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    def MaxfolioEntrada(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(id) from Entradas;"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def Maxfolio_Cortes(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(Folio) from Cortes;"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def ActualizarEntradasConcorte(self, maxnum):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update Entradas set CorteInc = %s, vobo = %s where TiempoTotal is not null and CorteInc=0;"
        #sql = "update Entradas set CorteInc=%s where TiempoTotal is not null and CorteInc=0;"
        cursor.execute(sql,maxnum)
        cone.commit()
        cone.close()

    def NocobradosAnt(self, vobo):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update Entradas set vobo = %s where Importe is null and CorteInc=0;"
        cursor.execute(sql,vobo)
        cone.commit()
        cone.close()

    def obtenerNumCorte(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(Folio) from Cortes"
        #sql = "update Entradas set CorteInc = 1 WHERE Importe > 0"
        cursor.execute(sql)
        #cone.commit()
        cone.close()
        return cursor.fetchall()
    def MaxnumId(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select max(idInicial) from Cortes"
        #sql = "update Entradas set CorteInc = 1 WHERE Importe > 0"
        cursor.execute(sql)
        #cone.commit()
        cone.close()
        return cursor.fetchall()

    def GuarCorte(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into Cortes(Importe, FechaIni, FechaFin,Quedados,idInicial,NumBolQued) values (%s,%s,%s,%s,%s,%s)"
        #sql = "update Entradas set CorteInc = 1 WHERE Importe > 0"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    def UltimoCorte(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select min(inicio) from MovsUsuarios where CierreCorte is null;"
        #sql="select max(FechaFin) from Cortes;"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
 #####Nuevo rpte Corte 19abr22
    def Cortes_Max(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT max(Salida), max(Corteinc) FROM Entradas where MONTH(Salida)=%s AND YEAR(Salida)=%s "
        #sql="SELECT max(FechaFin), min(FechaFin) FROM Cortes where MONTH(FechaFin)=%s AND YEAR(FechaFin)=%s " 
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
    def Cortes_Min(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT max(FechaIni), min(FechaIni) FROM Cortes where MONTH(FechaIni)=%s AND YEAR(FechaIni)=%s " 
        #sql="SELECT min(Entrada),min(Corteinc) FROM Entradas where MONTH(Entrada)=%s AND YEAR(Entrada)=%s AND CorteInc > 0 "
        #sql="SELECT max(FechaFin), min(FechaFin) FROM Cortes where MONTH(FechaFin)=%s AND YEAR(FechaFin)=%s " 
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
    def Cortes_Folio(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Folio FROM Cortes where FechaIni=%s"
        #sql="SELECT FechaIni, FechaFin FROM Cortes where Folio=%s" 
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
    def Registros_corte(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT id, Entrada, Salida, TiempoTotal, Importe, CorteInc, Placas, TarifaPreferente FROM Entradas where CorteInc > (%s-1) AND CorteInc < (%s+1)"  #Entradas where Entrada >= %s AND Salida <= %s
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()
    def Totales_corte(self, datos1):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT sum(Importe), max(CorteInc), min(CorteInc), Count(TarifaPreferente) FROM Entradas where CorteInc > (%s-1) AND CorteInc < (%s+1)" #Entrada > %s AND Entrada < %s
        cursor.execute(sql,datos1)
        cone.close()
        return cursor.fetchall()
    def Resumen_promo(self, datos1):
        cone=self.abrir()
        cursor=cone.cursor()
        #print('Adentro del query')
        sql="SELECT Count(TarifaPreferente),TarifaPreferente,Importe, sum(Importe) as ImporteTot FROM Entradas where CorteInc > (%s-1) AND CorteInc < (%s+1) GROUP BY TarifaPreferente ORDER BY ImporteTot DESC;"
        #sql="SELECT Count(*),TarifaPreferente,Importe, Count(*)*Importe  as cuantos FROM Entradas where CorteInc = %s GROUP BY TarifaPreferente,Importe;"
        #print(Count(TarifaPreferente)+'  '+TotPromo)
        #sql="SELECT Count(TarifaPreferente),TarifaPreferente,Importe, Count(TarifaPreferente)*Importe as ImporteTot FROM Entradas where CorteInc > (%s-1) AND CorteInc < (%s+1) GROUP BY TarifaPreferente,Importe ORDER BY ImporteTot;"
        cursor.execute(sql,datos1)
        cone.close()
        return cursor.fetchall()   
#####USUARIOS###

    def ConsultaUsuario(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT Id_usuario, Contrasena, Nom_usuario FROM Usuarios WHERE Usuario = %s"
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall() 
    def CajeroenTurno(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT min(id_movs), nombre, inicio, turno, Idusuario FROM MovsUsuarios where CierreCorte is null"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()   
    def IniciosdeTurno(self, dato):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT inicio, usuario FROM MovsUsuarios where inicio > %s" #and CierreCorte = 'No aplica'  Idusuario = %s and 
        cursor.execute(sql, dato)
        cone.close()
        return cursor.fetchall()                 
    def ActuaizaUsuario(self, actual):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="INSERT INTO MovsUsuarios(Idusuario, usuario, inicio, nombre, turno) values (%s,%s,%s,%s,%s)"
        #sql="INSERT INTO PagosPens(idcliente, num_tarjeta, Fecha_pago, Fecha_vigencia, Mensualidad, Monto) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,actual)
        cone.commit()
        cone.close()
    def Cierreusuario(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update MovsUsuarios set CierreCorte = %s where  id_movs = %s;"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    def NoAplicausuario(self, dato):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "update MovsUsuarios set CierreCorte = 'No aplica' where  id_movs > %s;"
        cursor.execute(sql,dato)        
        cone.commit()
        cone.close()    
