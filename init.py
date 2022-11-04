from DBQueries import DBQueries
import datetime

dbq = DBQueries()

#dbq.criarAposta("11",5.5,[('538136a794711c8c9bc24b48353c396c','Draw')])
dbq.registerUser("a","a@gm.com","teste","123782",datetime.date(2000,1,1),0,0)
dbq.registerSpecialUser("b","b@gm.com","b",1,0)
dbq.registerSpecialUser("c","c@gm.com","c",0,1)

#dbq.criarAposta("1",10,[('538136a794711c8c9bc24b48353c396c','Draw'),('0db34ba8228c8124f7d026b0ce1724d2','Draw')])
#dbq.atualizaResultadoApostas('538136a794711c8c9bc24b48353c396c','Draw')
dbq.atualizaResultadoApostas('0db34ba8228c8124f7d026b0ce1724d2','Draw')

print(dbq.getGanhos(1))
